# import streamlit as st
# import tensorflow_hub as hub
# import tensorflow as tf
# import cv2
# import numpy as np
# from PIL import Image
# from io import BytesIO
#
# # Load the style transfer model
# model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
#
# # Function to perform style transfer
# def style_transfer(content_image, style_image):
#     content_image = tf.image.convert_image_dtype(content_image, tf.float32)[tf.newaxis, :]
#     style_image = tf.image.convert_image_dtype(style_image, tf.float32)[tf.newaxis, :]
#     stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
#     return stylized_image
#
# # Streamlit app
# st.title("Image Style Transfer")
#
# # Upload content and style images
# content_image = st.file_uploader("Upload Content Image", type=["jpg", "jpeg", "png"])
# style_image = st.file_uploader("Upload Style Image", type=["jpg", "jpeg", "png"])
#
# if content_image and style_image:
#     # Read and display content and style images
#     content_image = Image.open(content_image).convert("RGB")
#     style_image = Image.open(style_image).convert("RGB")
#
#     st.image(content_image, caption="Content Image", use_column_width=True)
#     st.image(style_image, caption="Style Image", use_column_width=True)
#
#     # Perform style transfer
#     stylized_image = style_transfer(np.array(content_image), np.array(style_image))
#
#     # Display the stylized image
#     st.image(stylized_image.numpy(), caption="Stylized Image", use_column_width=True)
#
#     # Save the stylized image
#     st.markdown("### Save Stylized Image")
#     save_button = st.button("Save Image")
#     if save_button:
#         cv2.imwrite('stylized_image.jpg', cv2.cvtColor(np.squeeze(stylized_image) * 255, cv2.COLOR_RGB2BGR))
#         st.success("Stylized image saved as stylized_image.jpg")

# import streamlit as st
# import tensorflow as tf
# import cv2
# import numpy as np
# from PIL import Image
# import os
# from io import BytesIO
# import requests
#
# # Download and load the style transfer model
# model_url = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
# model_path = 'arbitrary-image-stylization-v1-256'
# model = tf.saved_model.load(model_path)
#
# # Function to perform style transfer
# def style_transfer(content_image, style_image):
#     content_image = tf.image.convert_image_dtype(content_image, tf.float32)[tf.newaxis, :]
#     style_image = tf.image.convert_image_dtype(style_image, tf.float32)[tf.newaxis, :]
#     stylized_image = model(content_image=tf.constant(content_image), style_image=tf.constant(style_image))[0]
#     return stylized_image
#
# # Streamlit app
# st.title("Image Style Transfer")
#
# # Upload content and style images
# content_image = st.file_uploader("Upload Content Image", type=["jpg", "jpeg", "png"])
# style_image = st.file_uploader("Upload Style Image", type=["jpg", "jpeg", "png"])
#
# if content_image and style_image:
#     # Read and display content and style images
#     content_image = Image.open(content_image).convert("RGB")
#     style_image = Image.open(style_image).convert("RGB")
#
#     st.image(content_image, caption="Content Image", use_column_width=True)
#     st.image(style_image, caption="Style Image", use_column_width=True)
#
#     # Perform style transfer
#     stylized_image = style_transfer(np.array(content_image), np.array(style_image))
#
#     # Display the stylized image
#     st.image(stylized_image.numpy(), caption="Stylized Image", use_column_width=True)
#
#     # Save the stylized image
#     st.markdown("### Save Stylized Image")
#     save_button = st.button("Save Image")
#     if save_button:
#         cv2.imwrite('stylized_image.jpg', cv2.cvtColor(np.squeeze(stylized_image) * 255, cv2.COLOR_RGB2BGR))
#         st.success("Stylized image saved as stylized_image.jpg")

import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
import cv2
import numpy as np
from PIL import Image
from io import BytesIO


# Load the style transfer model
model_url = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
model = hub.load(model_url)

# Function to perform style transfer
def style_transfer(content_image, style_image):
    content_image = tf.image.convert_image_dtype(content_image, tf.float32)[tf.newaxis, :]
    style_image = tf.image.convert_image_dtype(style_image, tf.float32)[tf.newaxis, :]
    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
    return stylized_image

# Streamlit app
st.title("Image Style Transfer")

# Upload content and style images
content_image = st.file_uploader("Upload Content Image", type=["jpg", "jpeg", "png"])
style_image = st.file_uploader("Upload Style Image", type=["jpg", "jpeg", "png"])

if content_image and style_image:
    # Read and display content and style images
    content_image = Image.open(content_image).convert("RGB")
    style_image = Image.open(style_image).convert("RGB")

    st.image(np.squeeze(content_image), caption="Content Image", use_column_width=True)
    st.image(np.squeeze(style_image), caption="Style Image", use_column_width=True)

    # Perform style transfer
    stylized_image = style_transfer(np.array(content_image), np.array(style_image))

    # Display the stylized image
    st.image(stylized_image.numpy(), caption="Stylized Image", use_column_width=True)

    # Save the stylized image
    st.markdown("### Save Stylized Image")
    save_button = st.button("Save Image")
    if save_button:
        cv2.imwrite('stylized_image.jpg', cv2.cvtColor(np.squeeze(stylized_image) * 255, cv2.COLOR_RGB2BGR))
        st.success("Stylized image saved as stylized_image.jpg")
