import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

st.set_page_config(layout="wide", page_title="Background_Remover")

st.write("## Remove background from your image")
st.write(
    ": Try uploading an image to watch the background removed."
)
st.sidebar.write("## Upload :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Convert the fixed image to bytes for download
def convert_image_to_bytes(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

# Process and display images, including a download button
def fix_image(upload=None):
    # Load the image based on the upload or default to a sample image
    image = Image.open(upload) if upload else Image.open("image.jpg")

    col1.write("### Original Image :camera:")
    col1.image(image, use_column_width=True)

    # Remove the background
    fixed = remove(image)
    
    col2.write("### Fixed Image :wrench:")
    col2.image(fixed, use_column_width=True)

    # Convert the processed image to bytes for downloading
    image_bytes = convert_image_to_bytes(fixed)

    # Create a download button for the fixed image
    st.write("### Download the fixed image")
    st.download_button(
        label="Download fixed image",
        data=image_bytes,
        file_name="fixed.png",
        mime="image/png"
    )

# Layout for displaying images
col1, col2 = st.columns(2)

# Upload widget in the sidebar
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Validate and process the uploaded file
if my_upload:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image()  # Load and process the default image if no file is uploaded
