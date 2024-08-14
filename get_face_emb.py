import numpy as np
from deepface import DeepFace


def get_face_embedding(image_path):
    try:
        # Extract embedding for the new image
        result = DeepFace.represent(img_path=image_path, model_name='VGG-Face')
        # Assuming the embedding is the first result
        return np.array(result[0]['embedding'])
    except Exception as e:
        print(f"Error extracting embedding: {e}")
        return None