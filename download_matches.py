import zipfile
from flask import send_file
import os 

def download_album():
    # Define the path to the output folder
    output_folder = 'static/results'
    zip_filename = 'matched_faces.zip'
    zip_path = os.path.join('static', zip_filename)
    
    # Create a zip file
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(output_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, output_folder)
                zipf.write(file_path, arcname=arcname)
    
    # Send the zip file to the user
    return send_file(zip_path, as_attachment=True, download_name=zip_filename)