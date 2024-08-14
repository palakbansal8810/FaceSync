import os
import io
import zipfile
from flask import Flask, render_template, request, redirect, url_for, send_file
import urllib.parse
from werkzeug.utils import secure_filename
from extracting_faces import extract_faces
from embeddings import compute_embeddings, save_embeddings
from load_embeddings import load_embeddings
from match_face import match_face
from get_face_emb import get_face_embedding
from saving_matches import matches_folder
from del_directory import clear_directory
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['UPLOAD_ALBUM'] = 'static/photos/'

def ensure_directory_exists(directory):
    os.makedirs(directory, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    ensure_directory_exists(app.config['UPLOAD_ALBUM'])
    ensure_directory_exists(app.config['UPLOAD_FOLDER'])
    
    if request.method == 'POST':
        if 'file' not in request.files and 'album' not in request.files:
            return redirect(request.url)
        
        # Handle single image upload
        file = request.files['file']
        
        if file.filename != '':
            filename = secure_filename(file.filename)
            # Clear the upload directory before saving a new file
            clear_directory(app.config['UPLOAD_FOLDER'])
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            new_image_path = file_path
        else:
            new_image_path = None
        
        # Handle album upload
        album_files = request.files.getlist('album')
        if album_files:
            # Clear the album directory before saving new files
            clear_directory(app.config['UPLOAD_ALBUM'])
            for album_file in album_files:
                album_filename = secure_filename(album_file.filename)
                # Retry mechanism to avoid PermissionError
                for _ in range(5):  # Retry up to 5 times
                    try:
                        album_file_path = os.path.join(app.config['UPLOAD_ALBUM'], album_filename)
                        album_file.save(album_file_path)
                        break  # Exit loop if successful
                    except PermissionError:
                        time.sleep(1)  # Wait for 1 second before retrying

        input_folder = app.config['UPLOAD_ALBUM']
        output_folder = 'static/results'
        faces_folder = 'static/output_faces'
        embedding_folder = 'static/embedding_output'
        vgg_face_weights_path = 'vgg_face_weights.h5'

        ensure_directory_exists(faces_folder)
        ensure_directory_exists(embedding_folder)
        ensure_directory_exists(output_folder)
        
        # Clear directories before processing new data
        clear_directory(faces_folder)
        clear_directory(embedding_folder)
        clear_directory(output_folder)

        extract_faces(input_folder, faces_folder)

        for file_name in os.listdir(faces_folder):
            file_path = os.path.join(faces_folder, file_name)
            if os.path.isfile(file_path): 
                save_embeddings(file_path, embedding_folder)

        known_embeddings = load_embeddings(embedding_folder)

        if new_image_path:
            new_face_embedding = get_face_embedding(new_image_path)

            if new_face_embedding is not None:
                matches = match_face(new_face_embedding, known_embeddings)
                print(matches)
                result = matches_folder(matches, output_folder)
                base_names = [os.path.basename(file_path).split('_')[0] for file_path in result]
                result_list = [f'results/{names}' for names in base_names]
                # URL encode filenames
                encoded_result_list = [urllib.parse.quote(img) for img in result_list]
            else:
                encoded_result_list = []
            
            return render_template('index.html', matches=encoded_result_list)

    return render_template('index.html', matches=[])

@app.route('/download_all')
def download_all():
    output_folder = 'static/results'
    # Create an in-memory zip file
    memory_zip = io.BytesIO()
    with zipfile.ZipFile(memory_zip, 'w') as zip_file:
        for filename in os.listdir(output_folder):
            file_path = os.path.join(output_folder, filename)
            zip_file.write(file_path, filename)
    memory_zip.seek(0)
    return send_file(memory_zip, download_name='all_matches.zip', as_attachment=True)

# New endpoint to download a single file
@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join('static/results', filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return redirect(url_for('index'))


