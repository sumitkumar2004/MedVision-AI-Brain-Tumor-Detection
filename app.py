from pathlib import Path
from uuid import uuid4
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request
from PIL import Image, UnidentifiedImageError

BASE = Path(__file__).resolve().parent
MODEL_PATH = BASE / "artifacts" / "brain_tumor_clean_finetuned_best.keras"
UPLOADS = BASE / "static" / "uploads"
UPLOADS.mkdir(parents=True, exist_ok=True)
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
CLASSES = ["glioma", "meningioma", "notumor", "pituitary"]
model = None
model_error = None
try:
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
except Exception as exc:
    model_error = f"Could not load model: {exc}"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = model_error
    image_url = None
    if request.method == "POST":
        f = request.files.get("mri_image")
        if not f or not f.filename:
            error = "Please select an MRI image."
        elif Path(f.filename).suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            error = "Use a JPG, JPEG, or PNG image."
        elif model is None:
            error = "Model is not loaded. Check artifacts/model path and terminal output."
        else:
            try:
                im = Image.open(f.stream).convert("RGB").resize((160, 160))
                arr = np.expand_dims(np.asarray(im, dtype=np.float32), 0)
                # Expected project preprocessing: RGB float32 pixels in [0,255].
                scores = np.asarray(model(arr, training=False))[0]
                name = f"{uuid4().hex}.png"
                im.save(UPLOADS / name, format="PNG")
                image_url = "uploads/" + name
                result = {"label": CLASSES[int(np.argmax(scores))],
                          "score": round(float(np.max(scores))*100, 2),
                          "scores": [{"name": CLASSES[i], "score": round(float(scores[i])*100, 2)}
                                     for i in range(len(CLASSES))]}
                error = None
            except (UnidentifiedImageError, OSError, ValueError):
                error = "That file could not be read as an image."
            except Exception:
                app.logger.exception("Inference error")
                error = "Inference failed. Check the terminal for details."
    return render_template("index.html", result=result, error=error,
                           image_url=image_url, model_ready=model is not None)

@app.errorhandler(413)
def too_large(_):
    return render_template("index.html", result=None, error="Maximum upload size is 5 MB.",
                           image_url=None, model_ready=model is not None), 413

@app.get("/health")
def health():
    return {"status": "ok" if model is not None else "model_unavailable",
            "model_loaded": model is not None}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
