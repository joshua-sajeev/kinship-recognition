from flask import Flask, render_template, redirect, request, send_from_directory
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename
import os
from model import compute_cosine_similarity

app = Flask(__name__)
app.config['UPLOAD_DIRECTORY'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB
app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']

@app.route('/')
def index():
  files = os.listdir(app.config['UPLOAD_DIRECTORY'])
  images = []

  for file in files:
    if os.path.splitext(file)[1].lower() in app.config['ALLOWED_EXTENSIONS']:
      images.append(file)
  
  return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload():
  try:
    file = request.files['file1']

    if file:
      extension = os.path.splitext(file.filename)[1].lower()

      if extension not in app.config['ALLOWED_EXTENSIONS']:
        return 'File is not an image.'
        
      file.save(os.path.join(
        app.config['UPLOAD_DIRECTORY'],
        secure_filename(file.filename)
      ))
  
    file = request.files['file2']

    if file:
      extension = os.path.splitext(file.filename)[1].lower()

      if extension not in app.config['ALLOWED_EXTENSIONS']:
        return 'File is not an image.'
        
      file.save(os.path.join(
        app.config['UPLOAD_DIRECTORY'],
        secure_filename(file.filename)
      ))
  except RequestEntityTooLarge:
    return 'File is larger than the 16MB limit.'
  
  return redirect('/')

@app.route('/serve-image/<filename>', methods=['GET'])
def serve_image(filename):
  return send_from_directory(app.config['UPLOAD_DIRECTORY'], filename)


@app.route('/predict', methods=['POST'])
def predict():
    files = os.listdir(app.config['UPLOAD_DIRECTORY'])
    images = [file for file in files if os.path.splitext(file)[1].lower() in app.config['ALLOWED_EXTENSIONS']]
    
    if len(images) != 2:
        return 'Please upload exactly two images.'
    
    image_path1 = os.path.join(app.config['UPLOAD_DIRECTORY'], images[0])
    image_path2 = os.path.join(app.config['UPLOAD_DIRECTORY'], images[1])
    
    similarity,kinship_label = compute_cosine_similarity(image_path1, image_path2)

    for image in images:
        os.remove(os.path.join(app.config['UPLOAD_DIRECTORY'], image))
    
    return render_template('index.html', cosine_similarity=similarity, kinship_label=kinship_label)
@app.route('/clear', methods=['POST'])
def clear_images():
    files = os.listdir(app.config['UPLOAD_DIRECTORY'])
    for file in files:
        if os.path.splitext(file)[1].lower() in app.config['ALLOWED_EXTENSIONS']:
            os.remove(os.path.join(app.config['UPLOAD_DIRECTORY'], file))
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
