

# 👥 FaceSync

**FaceSync** is a Flask-based face recognition web application that allows users to upload a query image and an album of photos to find face matches.

---

## 🚀 Features

* Upload a single image (query face).
* Upload multiple images (photo album).
* Detect faces from album photos.
* Compute face embeddings using deep learning.
* Match the uploaded face against detected faces in the album.
* Download matched face images individually or all at once.
* Responsive interface with a loader during processing.

---

## 🧠 How It Works

1. **Face Detection** – Extracts faces from album images using the `extract_faces` module.
2. **Embedding Generation** – Embeddings for all faces are generated using a pre-trained model (`vgg_face_weights.h5`).
3. **Face Matching** – Computes similarity between the uploaded face and the album embeddings.
4. **Results** – Matched faces are displayed and made available for download.

---

## 📁 Project Structure

```
FaceSync/
├── app.py                        # Main Flask application
├── templates/
│   └── index.html               # Frontend HTML interface
├── static/
│   ├── css/styles.css           # Styling
│   ├── uploads/                 # Temporary storage for uploaded query image
│   ├── photos/                  # Temporary storage for uploaded album
│   ├── output_faces/            # Extracted faces from album
│   ├── embedding_output/        # Saved embeddings
│   └── results/                 # Matched results
├── extracting_faces.py
├── embeddings.py
├── load_embeddings.py
├── match_face.py
├── get_face_emb.py
├── saving_matches.py
├── del_directory.py
└── vgg_face_weights.h5          # Pre-trained VGG face model weights
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/FaceSync.git
cd FaceSync
```

### 2. Install Dependencies

Make sure you’re using a virtual environment:

```bash
pip install -r requirements.txt
```

> You must include a `requirements.txt` file with packages like `Flask`, `numpy`, `opencv-python`, etc.

### 3. Add Model Weights

Place `vgg_face_weights.h5` in the project root. This file is required for generating embeddings.

---

## ▶️ Running the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📸 Usage

1. Upload a query face image.
2. Upload multiple album photos.
3. Click **Upload** to start matching.
4. Matched results will appear with options to:

   * Download individual matches
   * Download all matches as a ZIP

---

## 📂 Output

* Matches are saved in `static/results/`.
* Extracted faces from album are saved in `static/output_faces/`.
* Embeddings are stored in `static/embedding_output/`.

---

## 🧽 Cleanup

Each upload session clears the following directories automatically:

* `static/uploads/`
* `static/photos/`
* `static/output_faces/`
* `static/embedding_output/`
* `static/results/`

---

## 📌 Requirements


> See `requirements.txt` 

---

