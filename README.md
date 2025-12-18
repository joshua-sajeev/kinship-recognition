# Kinship Recognition

A Flask web application that uses machine learning to determine if two faces are related by comparing their image features using cosine similarity.

## Features

- Upload two images to compare
- Extract features using MobileNet pre-trained model
- Calculate cosine similarity between images
- Classify as "Kin" or "Non Kin" based on similarity threshold
- Docker support for easy deployment

## Installation

### Prerequisites
- Python 3.11 (required, will not work with other Python versions)
- Docker (optional)

### Local Setup

```bash
# Ensure you have Python 3.11 installed
python3 --version  # Should show Python 3.11.x

# Create and activate virtual environment
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Docker Setup

```bash
# Build and run
docker build -t kinship-recognition .
docker run -p 5000:5000 kinship-recognition
```

## Usage

### Run Locally

```bash
source .venv/bin/activate
python app.py
# Visit http://localhost:5000
```

### Run with Docker

```bash
docker run -p 5000:5000 kinship-recognition
# Visit http://localhost:5000
```

## How to Use

1. Upload two image files
2. Click "Upload" to save images
3. Click "Predict" to get the similarity score and kinship classification
4. Click "Clear Images" to remove images

## Project Structure

```
kinship-recognition/
├── app.py              # Flask application
├── model.py            # ML model and similarity computation
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── .gitignore          # Git ignore file
├── static/
│   └── styles.css      # CSS styling
├── templates/
│   └── index.html      # HTML template
└── uploads/            # Uploaded images directory
```

## How It Works

1. Images are preprocessed to 224x224 pixels
2. Features extracted using MobileNet neural network
3. Cosine similarity calculated between feature vectors
4. Classification: > 0.35 = "Kin", ≤ 0.35 = "Non Kin"

## API Endpoints

- `GET /` - Main page
- `POST /upload` - Upload two images
- `GET /serve-image/<filename>` - Serve image file
- `POST /predict` - Calculate similarity and classify
- `POST /clear` - Delete uploaded images

## Technologies

- Flask 3.1.2
- TensorFlow 2.20.0
- MobileNet (feature extraction)
- scikit-learn (cosine similarity)
- Python 3.11 (required)
- Docker

## Notes

- **Python 3.11 required** - Will not work with Python 3.10, 3.12, or other versions
- Maximum file size: 16MB per image
- Supported formats: JPG, JPEG, PNG, GIF
- First prediction may take longer due to model loading
- Images are automatically deleted after prediction
- CPU only (GPU not required)
