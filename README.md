Single Digit Classification Model with MNIST Dataset

This repository contains a single digit classification model trained on the MNIST dataset. The model is implemented using TensorFlow and Keras, and it can classify handwritten digits (0-9) with high accuracy.

Usage:

1. Installation:

Clone the repository to your local machine:

git clone https://github.com/snaper20/SINGLE-DIGIT-CLASSIFICATION.git
cd single-digit-classification


2. Running the Streamlit App:

Navigate to the directory containing the Streamlit app:

cd streamlit-app

Run the Streamlit app:

streamlit run app.py

The app will launch in your default web browser. You can use the app to upload images of handwritten digits and see the model's predictions.

3. Testing the Model:

You can test the model's accuracy using your own handwritten digit images. Place the images in the 'digits' directory.

Run the following command to test the model:

python test_model.py

The script will load the images from the 'digits' directory, predict the digits using the trained model, and display the predictions along with the ground truth labels.

Additional Information:

- The model architecture and training code are located in the 'MNIST' directory.
- Pretrained model weights are available in the 'MNIST' directory.
- Sample handwritten digit images are provided in the 'digits' directory for testing purposes.

