
# Optical Character Recognition (OCR) with Image Processing

This Python script uses the Tesseract OCR engine along with the OpenCV library for image processing to extract text from images. The script processes images in the "test_images" directory, identifies specific keywords, and crops the region of interest (ROI) based on the identified keywords. 

## Getting Started

To run this script, make sure you have the following prerequisites installed:

- Python 3.x
- Tesseract OCR
- OpenCV
- PIL (Python Imaging Library)

To install the required packages, use the following commands:

```bash
pip3 install pytesseract
pip3 install opencv-python
pip3 install pillow
```
## Note
if you face with this error : tesseract is not installed or it's not in your PATH

you must install tesseract in you machine

For Windows :

[UB Mannheim Tesseract GitHub page](https://github.com/UB-Mannheim/tesseract/wiki).

For MacOs:

```bash
brew install tesseract.
```

For Linux :

```bash
sudo apt-get install tesseract-ocr
```


## Usage

1. Clone the repository to your local machine.
2. Add images to the "test_images" directory that you want to process.
3. Run the script `SignatureDetect.py` to extract text from the images.

The script will automatically create a directory named "Res" and save the cropped images with extracted text.

## Parameters

You can modify the following parameters in the script to adjust the processing:

- `scaleY` - Y-axis scaling factor for the length of the cropped image.
- `scaleXL` - Left X-axis scaling factor for the length of the cropped image.
- `scaleXR` - Right X-axis scaling factor for the length of the cropped image.

Make sure to adjust these parameters based on your image characteristics and specific requirements.

---
