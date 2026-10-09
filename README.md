# MedVision AI Flask Frontend

## Files
- `app.py`: Flask routes, image validation, model loading, inference and `/health`
- `templates/index.html`: dashboard and prediction results
- `static/css/style.css`: responsive UI
- `static/js/app.js`: drag/drop, preview, upload validation, mobile menu
- `artifacts/`: place your trained model here

## Setup (Windows PowerShell)
From your project directory:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Copy your model to:
`artifacts/brain_tumor_clean_finetuned_best.keras`

Run:
```powershell
python app.py
```
Open `http://127.0.0.1:5000`.

## Important preprocessing note
This app expects RGB, 160×160 images as `float32` values in `[0,255]`, with no additional `/255`, based on the project setup discussed. Verify that this exactly matches the notebook/model preprocessing. Class order is `glioma`, `meningioma`, `notumor`, `pituitary`. Scores are displayed as model scores, not calibrated probabilities.

This is an educational research prototype, not a medical device. Do not use it for diagnosis or clinical decisions. Uploaded previews are saved in `static/uploads/`; add production-grade privacy/security controls before deployment. Flask debug mode is for local development only.
