from extracting_faces import extract_faces
import os
from embeddings import compute_embeddings
from embeddings import save_embeddings
from load_embeddings import load_embeddings
from get_face_emb import get_face_embedding
from match_face import match_face
from saving_matches import matches_folder
from del_directory import clear_directory

if __name__=='__main__':
    
    input_folder='photos'
    output_folder='results'

    faces_folder = 'output_faces'
    embedding_folder = 'embedding_output'
    vgg_face_weights_path = 'facenet_keras_weights.h5'

    new_image_path=input("Image Path\n")
    clear_directory(faces_folder)
    clear_directory(embedding_folder)
    # if os.path.isdir(input_folder)==False:
    extract_faces(input_folder,faces_folder)
    os.makedirs(embedding_folder, exist_ok=True)
    
    for file_name in os.listdir(faces_folder):
        file_path = os.path.join(faces_folder, file_name)
        if os.path.isfile(file_path): 
            save_embeddings(file_path, embedding_folder)
        
    known_embeddings = load_embeddings(embedding_folder)

    # Get embedding for the new image
    new_face_embedding = get_face_embedding(new_image_path)

    if new_face_embedding is not None:
        # Match the new face embedding with known embeddings
        matches = match_face(new_face_embedding, known_embeddings)
        result=matches_folder(matches,output_folder)
        base_names = [os.path.basename(file_path).split('_')[0] for file_path in result]
        for names in base_names:
            print(f'photos/{names}.jpg')
        if matches:
            print(f"Matched faces: {matches}")
        else:
            print("No matches found within the threshold.")
    else:
        print("Failed to get the embedding for the new image.")
    imgs=os.listdir(output_folder)
    for img in imgs:
        img_path=''.join(['results/',img])
        print(img_path)
  

