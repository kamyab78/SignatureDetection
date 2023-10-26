try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import cv2
import os

please = 0
sign = 0
above = 0

images_dir = "test_images"
input_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), images_dir
)

for filename in os.listdir(input_path):

    if ".jpg" in filename:
        print("file ", filename)
        img = cv2.imread(os.path.join(input_path,filename))
    else:
        continue
    h, w, _ = img.shape 

    data = pytesseract.image_to_data(Image.open(os.path.join(input_path,filename)))

    pleaseCd = [0, 0, 0, 0]
    aboveCd = [0, 0, 0, 0]

    for d in data.splitlines():
        d = d.split("\t")
        if len(d) == 12:

            if d[11].lower() == "please":
                pleaseCd[0] = int(d[6])
                pleaseCd[1] = int(d[7])
                pleaseCd[2] = int(d[8])
                pleaseCd[3] = int(d[9])
                please = please + 1
            if d[11].lower() == "sign":
                sign = sign + 1
            if d[11].lower() == "above":
                aboveCd[0] = int(d[6])
                aboveCd[1] = int(d[7])
                aboveCd[2] = int(d[8])
                aboveCd[3] = int(d[9])
                above = above + 1

    lengthSign = aboveCd[0] + aboveCd[3] - pleaseCd[0]
    scaleY = 2
    scaleXL = 2.5
    scaleXR = 0.5

    lengthSignCd = [0, 0, 0, 0]

    lengthSignCd[0] = int(pleaseCd[0] - lengthSign * 2.5)
    lengthSignCd[1] = int(pleaseCd[1] - lengthSign * 2)

    img = cv2.rectangle(
        img,
        (lengthSignCd[0], lengthSignCd[1]),
        (
            lengthSignCd[0] + int((scaleXL + scaleXR + 1) * lengthSign),
            lengthSignCd[1] + int(scaleY * lengthSign),
        ),
        (255, 255, 255),
        2,
    )
    cropImg = img[
        lengthSignCd[1] : lengthSignCd[1] + int(scaleY * lengthSign),
        lengthSignCd[0] : lengthSignCd[0]
        + int((scaleXL + scaleXR + 1) * lengthSign),
    ]

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Res")
    if not os.path.exists(path):
        os.makedirs(path)

    s1 = "Result_" + filename
    if cropImg.size!=0:
        cv2.imwrite(os.path.join(path, s1), cropImg)
