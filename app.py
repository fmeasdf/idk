from flask import Flask, request, jsonify
from fastai.vision.all import *

app = Flask(__name__)

# Lade das exportierte Modell
path_to_export = "/Users/eneastibal/downloads/export.pkl"
learn_inf = load_learner(path_to_export)

@app.route('/classify', methods=['POST'])
def classify_animal():
    try:
        # Lade das Bild von der Anfrage
        image_file = request.files['image']
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(tempfile.gettempdir(), filename)
        image_file.save(image_path)

        # Mache eine Vorhersage
        label, _, _ = learn_inf.predict(image_path)

        return jsonify({"label": str(label)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
