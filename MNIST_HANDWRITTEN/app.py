import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2

# Load the trained model
model = tf.keras.models.load_model("handwritten.model")

# Function to preprocess the image
def preprocess_image(image):
   # Resize the image to 28x28 pixels
    image = image.resize((28, 28))
    # Convert the image to grayscale
    image = image.convert('L')
    # Convert the image to numpy array
    image = np.array(image)
    # Normalize the image
    image = image / 255.0
    # Reshape the image to match the input shape of the model
    image = image.reshape(1, 28, 28, 1)
    return image

# Streamlit app
def main():
    st.title("MNIST Handwritten Digit Recognition")
    st.write("Upload a picture of a handwritten digit (0-9) and I'll predict it for you.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Make prediction
        prediction = model.predict(processed_image)
        predicted_digit = np.argmax(prediction)

        st.write("")
        st.write("Classifying...")
        st.write(f"Predicted Digit: {predicted_digit}")

if __name__ == "__main__":
    main()
