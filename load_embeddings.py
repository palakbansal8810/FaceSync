import numpy as np
from scipy.spatial.distance import euclidean
from deepface import DeepFace
import os

def load_embeddings(embedding_folder):
    embeddings = {}
    for file_name in os.listdir(embedding_folder):
        if file_name.endswith('.npy'):
            file_path = os.path.join(embedding_folder, file_name)
            # Load the .npy file and extract the embedding array
            embedding_data = np.load(file_path, allow_pickle=True).item()
            embedding_array = np.array(embedding_data['embedding'])
            
            # Print shape for debugging
            print(f"Loaded embedding shape for {file_name}: {embedding_array.shape}")
            
            # Flatten the embedding to ensure it's 1-D
            # if embedding_array.ndim > 1:
            #     embedding_array = embedding_array.flatten()
                
            embeddings[file_name] = embedding_array
    return embeddings