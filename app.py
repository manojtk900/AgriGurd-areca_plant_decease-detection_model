from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import json
import uuid
import logging
from werkzeug.utils import secure_filename

# --------------------------------------------------
# Flask Configuration
# --------------------------------------------------

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

logging.basicConfig(level=logging.INFO)

# --------------------------------------------------
# Load Model
# --------------------------------------------------

MODEL_PATH = "models/plant_disease_model.keras"

if not os.path.exists(MODEL_PATH):
    MODEL_PATH = "models/plant_disease_model.h5"

model = tf.keras.models.load_model(MODEL_PATH)

# --------------------------------------------------
# Load Class Names
# --------------------------------------------------

with open("models/class_indices.json", "r") as f:
    class_indices = json.load(f)

class_names = {v: k for k, v in class_indices.items()}

# --------------------------------------------------
# Load Disease Information
# --------------------------------------------------

with open("data/disease_info.json", "r", encoding="utf-8") as f:
    disease_data = json.load(f)

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def preprocess_image(filepath):

    img = Image.open(filepath).convert("RGB")

    img = img.resize((224, 224))

    img_array = np.array(img, dtype=np.float32)

    img_array /= 255.0

    img_array = np.expand_dims(img_array, axis=0)

    return img_array


def format_disease_name(name):
    """
    Convert model class names into readable names
    """

    return (
        name.replace("_", " ")
            .title()
    )

# --------------------------------------------------
# Routes
# --------------------------------------------------


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return render_template(
            "index.html",
            error="No image uploaded."
        )

    file = request.files["file"]

    if file.filename == "":
        return render_template(
            "index.html",
            error="Please choose an image."
        )

    if not allowed_file(file.filename):
        return render_template(
            "index.html",
            error="Only JPG, JPEG and PNG images are allowed."
        )

    # ------------------------------------
    # Save Uploaded Image
    # ------------------------------------

    filename = secure_filename(file.filename)

    filename = f"{uuid.uuid4().hex}_{filename}"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    # ------------------------------------
    # Image Preprocessing
    # ------------------------------------

    try:

        img_array = preprocess_image(filepath)

    except Exception as e:

        logging.error(e)

        return render_template(
            "index.html",
            error="Invalid image."
        )

    # ------------------------------------
    # Prediction
    # ------------------------------------

    prediction = model.predict(img_array, verbose=0)

    predicted_class = np.argmax(prediction)

    confidence = float(np.max(prediction))

    # ------------------------------------
    # Unknown Image Detection
    # ------------------------------------

    if confidence < 0.75:

        return render_template(
            "index.html",
            prediction="Unknown / Not an Areca Plant",
            confidence=round(confidence * 100, 2),
            image_path=filepath,
            info={}
        )

    # ------------------------------------
    # Disease Information
    # ------------------------------------

    disease_key = class_names[predicted_class]

    disease = format_disease_name(disease_key)

    info = disease_data.get(disease_key, {})
    print(info)

    logging.info(f"Disease : {disease}")
    logging.info(f"Confidence : {confidence*100:.2f}%")

    # ------------------------------------
    # Return Result
    # ------------------------------------

    return render_template(

        "index.html",

        prediction=disease,

        confidence=round(confidence * 100, 2),

        image_path=filepath,

        info=info

    )


# --------------------------------------------------
# Run Flask
# --------------------------------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )