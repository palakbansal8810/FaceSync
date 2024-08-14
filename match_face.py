import numpy as np
from scipy.spatial.distance import euclidean

def match_face(new_face_embedding, known_embeddings):
    matches = {}
    min_distance = 1.4
    matched_face = None

    # Print shape for debugging
    print(f"New face embedding shape: {new_face_embedding.shape}")

    # Flatten the new face embedding if necessary
    # if new_face_embedding.ndim > 1:
    #     new_face_embedding = new_face_embedding.flatten()

    for known_face, known_embedding in known_embeddings.items():
        # Print shape for debugging
        print(f"Known face embedding shape: {known_embedding.shape}")

        # Flatten the known embedding if necessary
        # if known_embedding.ndim > 1:
        #     known_embedding = known_embedding.flatten()

        # Ensure both embeddings are 1-D arrays
        # if new_face_embedding.ndim != 1 or known_embedding.ndim != 1:
        #     raise ValueError("Embeddings should be 1-D arrays.")

        distance = euclidean(new_face_embedding, known_embedding)
        if distance < min_distance:
            min_distance = distance
            matched_face = known_face
            matches[known_face] = distance

    return matches
