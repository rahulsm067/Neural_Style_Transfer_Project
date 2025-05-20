import streamlit as st
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import io

# Function to load image and preprocess
def load_image(image_file):
    img = Image.open(image_file).convert('RGB')
    img = np.array(img).astype(np.float32)[np.newaxis, ...] / 255.0
    return img

# Resize style image to 256x256 as required by model
def resize_style_image(image):
    return tf.image.resize(image, (256, 256))

# Load model once
@st.cache_resource
def load_model(model_path):
    return hub.load(model_path)

# Style transfer function
def transfer_style(content_img, style_img, model):
    outputs = model(tf.constant(content_img), tf.constant(style_img))
    stylized_image = outputs[0]
    return stylized_image[0].numpy()

# Streamlit UI
st.title("🎨 Neural Style Transfer App")

# File uploader
content_file = st.file_uploader("Upload Content Image", type=["jpg", "jpeg", "png"])
style_file = st.file_uploader("Upload Style Image", type=["jpg", "jpeg", "png"])

# Pretrained model path (update this to your local directory if needed)
#model_path = "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2"
model_path = "C:/Users/visha/Neural-Style-Transfer/model"  


if content_file and style_file:
    st.subheader("Original Images")
    col1, col2 = st.columns(2)
    with col1:
        st.image(content_file, caption="Content Image", use_container_width=True)
    with col2:
        st.image(style_file, caption="Style Image", use_container_width=True)

    # Load and preprocess images
    content_img = load_image(content_file)
    style_img = load_image(style_file)
    style_img = resize_style_image(style_img)

    # Load model
    st.info("Loading model...")
    model = load_model(model_path)

    # Stylize
    st.info("Applying style transfer...")
    stylized_output = transfer_style(content_img, style_img, model)

    # Display result
    st.subheader("Stylized Output")
    st.image(np.clip(stylized_output, 0, 1), use_container_width=True)
