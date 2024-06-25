from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from fastai.learner import load_learner
import os
import tempfile

app = Flask(__name__)

# Laden Sie das Modell
learner = load_learner('export.pkl')

def get_file_path(filename):
    return os.path.join(tempfile.gettempdir(), secure_filename(filename))

def classify_image(image_path):
    label, _, _ = learner.predict(image_path)
    return label

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400 

        image_file = request.files['image']
        if image_file.filename == '': 
            return jsonify({'error': 'No selected file'}), 400 

        try:
            filename = secure_filename(image_file.filename)
            filepath = get_file_path(filename)
            image_file.save(filepath)
            result = classify_image(filepath)
            return render_template('index.html', result=str(result))
        except Exception as e:
            return jsonify({'error': str(e)}), 500 

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
