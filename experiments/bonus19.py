import streamlit as st
from PIL import Image, ImageFilter

st.subheader("Color to Grayscale Converter")

with st.expander("Start Camera"):
    #Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #Create a pillow image instance
    img = Image.open(camera_image)

    #Convert the pillow image to grayscale
    gray_img = img.convert("L")
    blur_img = img.filter(ImageFilter.BLUR)

    #Render the grayscale image on the webpage
    st.image(gray_img)
    st.image(blur_img)

with st.expander("Upload an image"):
    uploaded_image = st.file_uploader("Upload Image")

    if uploaded_image:
        uimg = Image.open(uploaded_image)
        gray = uimg.convert("L")
        st.image(gray)
