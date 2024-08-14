import cv2
import os

def extract_faces(input_folder, output_folder):
    """
    Extract faces from images in the input folder and save them to the output folder.

    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder where extracted faces will be saved.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Load the pre-trained Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        # Construct full file path
        file_path = os.path.join(input_folder, filename)
        
        # Check if the file is an image
        if not (filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.jpeg')):
            print(f"Skipping non-image file: {filename}")
            continue
        
        # Read the image
        image = cv2.imread(file_path)
        if image is None:
            print(f"Error: Image {file_path} not found or cannot be opened.")
            continue
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        if len(faces) == 0:
            print(f"No faces found in {file_path}.")
            continue
        
        # Save each detected face
        for i, (x, y, w, h) in enumerate(faces):
            # Extract face region
            face_image = image[y:y+h, x:x+w]
            
            # Construct path for saving the face image
            face_image_filename = f"{os.path.splitext(filename)[0]}_face_{i+1}.jpg"
            face_image_path = os.path.join(output_folder, face_image_filename)
            
            # Save the face image
            cv2.imwrite(face_image_path, face_image)
            print(f"Saved face to {face_image_path}")

