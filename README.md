# Number Plate Detection 🚘

This project implements a number plate detection system using image processing and OCR (Optical Character Recognition) techniques. It allows users to upload an image, processes it to identify the number plate, and extracts the text from the detected plate.

## Features 📋

### Image Preprocessing:
- Resizes the uploaded image.
- Converts the image to grayscale.
- Applies bilateral filtering for smoothening.
- Detects edges using the Canny edge detection algorithm.

### Contour Detection:
- Identifies contours and highlights potential number plates.

### OCR:
- Extracts the text from the detected number plate using Tesseract OCR.

### Interactive UI:
- Streamlit-based web interface for image upload, visualization of processing steps, and downloading the extracted number plate.

## Technologies Used 💻
- Python
- OpenCV for image processing
- Tesseract OCR for text recognition
- Streamlit for the interactive web interface

## Demo 🖼️

1. **Original Image**: Upload an image of a vehicle.
2. **Preprocessing**: View steps like grayscale conversion, edge detection, and contour identification.
3. **Extracted Plate**: Visualize the detected number plate and download the extracted image.
4. **Highlighted Plate**: See the number plate highlighted on the original image.
## Requirements 🛠️
- Python 3.8 or higher

### Libraries:
- opencv-python
- streamlit
- pytesseract
- numpy
- Pillow

## Acknowledgments 🙌
- **Tesseract OCR**: For text extraction.
- **OpenCV**: For powerful image processing tools.

## Author ✨
**Naveen Kumar**  
A data professional passionate about leveraging NLP, machine learning, and image processing to create impactful projects. Connect with me on [LinkedIn](https://www.linkedin.com/in/naveen-kumar1002/).
