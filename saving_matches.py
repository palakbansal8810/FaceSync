import os
import shutil
import re

def matches_folder(matches, destination_folder):
    # Extract keys from the matches dictionary
    matches = list(matches.keys())
    result = []

    for match in matches:
        # Remove the '.npy' extension
        match = match.replace('.npy', '')

        # Remove the '_face_x' pattern using regular expressions
        match = re.sub(r'_face_\d+', '', match)
        
        # Construct the file path with the cleaned-up name
        match = ''.join(['static/photos/', match])

        result.append(match)

    # Create the directory if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Move each file to the new directory
    for file in result:
        if os.path.isfile(file):
            shutil.move(file, os.path.join(destination_folder, os.path.basename(file)))
        else:
            print(f"File {file} does not exist.")
    
    return result

