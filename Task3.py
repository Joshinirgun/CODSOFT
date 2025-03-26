from keras.models import load_model
import numpy as np
import cv2
import os
from scipy.spatial.distance import cosine

# Load the pretrained FaceNet model
model_path = "facenet_keras.h5"  # Download from: https://github.com/nyoki-mtl/keras-facenet
if not os.path.exists(model_path):
    print("Error: FaceNet model file is missing!")
    exit()

model = load_model(model_path)
print("✅ FaceNet model loaded successfully!")
