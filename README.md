# Kinship Recognition

A Flask web application that uses machine learning to determine if two faces are related (kinship) or not by comparing their image features using cosine similarity.

## Features

- Upload two images to compare
- Extract features using MobileNet pre-trained model
- Calculate cosine similarity between images
- Classify as "Kin" or "Non Kin" based on similarity threshold
- View uploaded images
- Clear images after comparison

## Installation

### Prerequisites
- Python 3.11+
- pip package manager

### Setup

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment (Linux/Mac)
source .venv/bin/activate

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Run Flask app
python app.py

# Open browser and visit
http://localhost:5000
```

## How to Use the App

1. **Upload Images**: Select two image files using the file input
2. **Click Upload**: Upload the images to the server
3. **Preview**: View the uploaded images
4. **Predict**: Click "Predict" to calculate similarity and kinship
5. **Results**: View the cosine similarity score and kinship classification
6. **Clear**: Click "Clear Images" to remove images

## Project Structure

```
kinship-recognition/
├── app.py                 # Flask application
├── model.py               # ML model and similarity computation
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore file
├── static/
│   └── styles.css         # CSS styling
├── templates/
│   └── index.html         # HTML template
└── uploads/               # Uploaded images directory
```

## How It Works

1. Images are preprocessed to 224x224 pixels
2. Features are extracted using MobileNet neural network
3. Cosine similarity is calculated between feature vectors
4. Classification threshold: > 0.35 = "Kin", ≤ 0.35 = "Non Kin"

## API Endpoints

- `GET /` - Main page
- `POST /upload` - Upload two images
- `GET /serve-image/<filename>` - Serve image file
- `POST /predict` - Calculate similarity and classify
- `POST /clear` - Delete uploaded images

## Technologies

- **Backend**: Flask 3.1.2
- **ML Model**: TensorFlow 2.20.0, Keras 3.13.0, MobileNet
- **Similarity**: scikit-learn 1.8.0 cosine similarity
- **Frontend**: HTML, CSS, JavaScript
- **Python**: 3.11+

## Notes

- GPU/CUDA not required (uses CPU by default)
- First prediction may take longer due to model loading
- Images are deleted after prediction
- Maximum file size: 16MB per image
- Supported formats: JPG, JPEG, PNG, GIF
