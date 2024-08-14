import numpy as np
import os
from deepface import DeepFace


def compute_embeddings(image_path):
    try:
        # Compute face embeddings
        embeddings = DeepFace.represent(img_path=image_path, model_name='VGG-Face')
        return embeddings
    except ValueError as e:
        print(f"Error processing {image_path}: {e}")
        return None

def save_embeddings(image_path, output_folder):
    embeddings = compute_embeddings(image_path)
    if embeddings:
        for i, embedding in enumerate(embeddings):
            embedding_path = os.path.join(output_folder, f"{os.path.basename(image_path)}.npy")
            np.save(embedding_path, embedding, allow_pickle=True)  # Save with pickling enabled
            print(f"Saved embedding to {embedding_path}")
    else:
        print(f"No embeddings saved for {image_path}")

