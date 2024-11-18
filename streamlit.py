import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pytesseract

# Setting up the Tesseract command path
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\jayas\\OneDrive\\Desktop\\New folder\\number_plate_detector"

# Configure Streamlit app
st.set_page_config(page_title="Number Plate Detector 🚗", layout="wide", page_icon="🚘")

# Set background color
st.markdown(
    """
    <style>
    body {
        background-color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("Number Plate Detector 🚘")
st.write("Upload an image, and we'll detect the number plate using OCR techniques.")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Load the image
    image = np.array(Image.open(uploaded_file))
    st.image(image, caption="Uploaded Image 📷", use_column_width=True)
    
    # Resize image
    resized_image = cv2.resize(image, (800, 600))
    st.image(resized_image, caption="Resized Image 🔄", use_column_width=True)
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    st.image(gray_image, caption="Gray Image Output 🖤", use_column_width=True)
    
    # Apply bilateral filter
    smooth_image = cv2.bilateralFilter(gray_image, 11, 17, 9)
    st.image(smooth_image, caption="Smooth Image Output 🎨", use_column_width=True)
    
    # Edge detection
    edge_image = cv2.Canny(smooth_image, 30, 200)
    st.image(edge_image, caption="Border (Edge) Image Output ✂️", use_column_width=True)
    
    # Contour detection
    cnts, _ = cv2.findContours(edge_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contour_image = resized_image.copy()
    cv2.drawContours(contour_image, cnts, -1, (0, 255, 0), 3)
    st.image(contour_image, caption="All Contours Image Output 🌀", use_column_width=True)
    
    # Filter for the number plate
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
    screen_cnt = None
    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4:
            screen_cnt = approx
            x, y, w, h = cv2.boundingRect(c)
            new_image = resized_image[y:y+h, x:x+w]
            st.image(new_image, caption="Extracted Number Plate Output 🛑", use_column_width=True)
            st.download_button(
                label="Download Number Plate Image 📥",
                data=cv2.imencode('.png', new_image)[1].tobytes(),
                file_name="number_plate.png",
                mime="image/png"
            )
            break

    # Highlight the number plate on the original image
    if screen_cnt is not None:
        cv2.drawContours(resized_image, [screen_cnt], -1, (0, 255, 0), 3)
        st.image(resized_image, caption="Highlighted Number Plate Output ✅", use_column_width=True)
    else:
        st.write("No number plate detected ❌.")
