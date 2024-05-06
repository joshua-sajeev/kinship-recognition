import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.applications import MobileNet
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_image(image_path):
    # Load and resize image using TensorFlow functions
    image = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image, channels=3)  # Adjust channels if needed
    image = tf.image.resize(image, (224, 224))  # Resize to target size
    image = tf.cast(image, tf.float32)  # Convert image to float32
    image = image / 255.0  # Normalize pixel values to [0, 1]
    return image

def compute_cosine_similarity(image_path1, image_path2):
    input_shape = (224, 224, 3)
    # Load pre-trained VGG16 model
    base_model = MobileNet(weights='imagenet', include_top=False, input_shape=input_shape)
    
    # Preprocess images
    image_a = preprocess_image(image_path1)
    image_b = preprocess_image(image_path2)

    # Add batch dimension since VGG16 expects batch input
    image_a = np.expand_dims(image_a, axis=0)
    image_b = np.expand_dims(image_b, axis=0)

    # Extract features using VGG16
    features_a = base_model.predict(image_a)
    features_b = base_model.predict(image_b)

    # Reshape features to 1D arrays
    features_a = features_a.reshape(features_a.shape[0], -1)
    features_b = features_b.reshape(features_b.shape[0], -1)

    # Compute cosine similarity
    cosine_sim = cosine_similarity(features_a, features_b)
    
    kin  = None
    if cosine_sim[0][0] > 0.35:
        kin = "Kin"
    else:
        kin = "Non Kin"
    return cosine_sim[0][0],kin

# # Example usage:
# image_path1 = "../Pictures/will.jpg"
# image_path2 = "../Pictures/jaden.jpg"
# similarity_score = compute_cosine_similarity(image_path1, image_path2)
# print("Cosine Similarity:", similarity_score)

