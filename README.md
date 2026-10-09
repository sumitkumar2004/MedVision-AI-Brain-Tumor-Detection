# MedVision AI — Brain Tumor Detection

### Deep Learning-Based Brain MRI Classification Using CNN and Flask

MedVision AI is a machine learning research project that classifies brain MRI images into four categories using a trained deep learning model. The project integrates a TensorFlow/Keras model with a Flask web application to provide an interactive interface for uploading MRI images and viewing classification results.

> **Disclaimer:** This project is intended for educational and research purposes only. It is not a medical diagnostic tool and must not be used to make clinical decisions.

---

## Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Classification Categories](#-classification-categories)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Model Information](#-model-information)
- [Installation and Setup](#-installation-and-setup)
- [Run the Application](#-run-the-application)
- [How to Use](#-how-to-use)
- [Input Requirements](#-input-requirements)
- [Model Performance](#-model-performance)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

## Project Overview

Brain tumors are abnormal growths of cells within the brain or surrounding tissues. MRI scans are widely used by medical professionals to examine brain structures and investigate potential abnormalities.

**MedVision AI** demonstrates how deep learning can be applied to brain MRI image classification. The application accepts an MRI image, preprocesses it into the format expected by the trained model, generates class predictions, and displays the results through a web interface.

The project combines image processing, deep learning inference, and web development in a single application.

### Project Objectives

- Build a brain MRI image classification application using TensorFlow and Keras.
- Process input images into the model's required dimensions and format.
- Predict one of four brain MRI categories.
- Integrate the trained model with a Flask backend.
- Develop an interactive and responsive web interface.
- Demonstrate the practical integration of machine learning and web technologies.

---

## Key Features

- **Deep Learning Classification:** Uses a trained TensorFlow/Keras model to classify brain MRI images.
- **Four-Class Prediction:** Supports glioma, meningioma, no-tumor, and pituitary categories.
- **Image Upload:** Allows users to submit MRI images through a web interface.
- **Image Preprocessing:** Resizes uploaded images to the model's expected input dimensions.
- **Prediction Results:** Displays the predicted class and model output scores.
- **Interactive Interface:** Provides a browser-based dashboard for interacting with the model.
- **Flask Integration:** Connects the frontend with the machine learning inference pipeline.
- **Input Validation:** Handles supported image uploads and common upload errors.

---

##  Classification Categories

The model predicts one of the following four categories:

| Class | Description |
|---|---|
| `glioma` | MRI image category associated with glioma |
| `meningioma` | MRI image category associated with meningioma |
| `notumor` | MRI image category labeled as no tumor |
| `pituitary` | MRI image category associated with pituitary tumors |

The predicted category represents the model's classification output. It does not establish whether a person has a medical condition.

---

##  Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Deep Learning Framework | TensorFlow |
| Model API | Keras |
| Backend | Flask |
| Image Processing | Pillow (PIL) |
| Numerical Computing | NumPy |
| Frontend | HTML5, CSS3, JavaScript |
| Development Environment | Visual Studio Code |
| Version Control | Git and GitHub |

---

##  Project Structure

The project is organized as follows:

```text
MED VISION AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── artifacts/
│   └── brain_tumor_clean_finetuned_best.keras
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── app.js
│   │
│   └── uploads/
│
├── brain-tumor-mri-dataset/
│   └── Training and testing image folders
│
└── .venv/
    └── Python virtual environment
```

**Note:** The trained model, dataset, and virtual environment may be excluded from the GitHub repository because of their size or other distribution considerations. Their presence on the local machine is required where the application or training workflow depends on them. The exact dataset folder structure may vary.

---

##  Model Information

The application loads a previously trained Keras model for inference.

**Model file:**

`artifacts/brain_tumor_clean_finetuned_best.keras`

### Expected Input Format

| Property | Configuration |
|---|---|
| Image dimensions | 160 × 160 pixels |
| Color format | RGB |
| Data type | Float32 |
| Input pixel range | 0–255 |
| Number of output classes | 4 |

The preprocessing configuration above reflects the expected input format of the current model. Uploaded images should be prepared consistently with the preprocessing used during training.

### Inference Workflow

1. The user uploads a brain MRI image.
2. The Flask application validates the uploaded file.
3. The image is converted to RGB.
4. The image is resized to 160 × 160 pixels.
5. The processed image is passed to the trained model.
6. The model produces class scores.
7. The application displays the predicted class and available scores.

**Important:** Model scores are not necessarily calibrated probabilities and should not be interpreted as clinical confidence.

---

##  Installation and Setup

### Prerequisites

Install the following software before running the application:

- Python 3.10 or another Python version compatible with the installed TensorFlow release.
- Git.
- Visual Studio Code or another code editor.
- The trained Keras model file.

### Step 1: Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/sumitkumar2004/MedVision-AI-Brain-Tumor-Detection.git
```

Navigate to the project directory:

```bash
cd MedVision-AI-Brain-Tumor-Detection
```

### Step 2: Create a Virtual Environment

On Windows:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked by your PowerShell execution policy, you can use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

Install the packages listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

The dependency file should include the application's required packages, such as Flask, TensorFlow, NumPy, and Pillow.

### Step 4: Add the Trained Model

Place the trained model in the following location:

```text
artifacts/brain_tumor_clean_finetuned_best.keras
```

Ensure the filename and folder path match the configuration in `app.py`.

If the model is not included in the cloned repository, obtain it from your own trusted project files. The application cannot perform predictions without a compatible model file.

---

## 🚀 Run the Application

Once the dependencies are installed and the model is in place, start the Flask server:

```bash
python app.py
```

Open the following address in your browser:

**http://127.0.0.1:5000**

The application should load locally if the server starts successfully.

To stop the development server, press `Ctrl + C` in the terminal.

---

##  How to Use

1. Start the Flask application.
2. Open the local application URL in your browser.
3. Navigate to the image upload area.
4. Select a supported brain MRI image.
5. Submit the image for classification.
6. Review the predicted category and the displayed model scores.

Use only appropriate sample images for testing. Do not upload identifiable patient images or other sensitive medical information to a public or untrusted deployment.

---

##  Input Requirements

For best compatibility with the current inference pipeline:

- Use a valid brain MRI image.
- Use a supported image format, such as JPEG or PNG, if accepted by the application.
- Ensure the image contains a visible MRI scan rather than unrelated content.
- Avoid corrupted, empty, or excessively large files.
- Follow the model's expected image preprocessing format.

Resizing an image allows it to fit the model's input dimensions, but it does not guarantee that the image is medically suitable or that the model will classify it correctly.

---

##  Model Performance

The model was evaluated as part of the project's experimental workflow.

Previously recorded evaluation results include:

| Evaluation | Reported accuracy |
|---|---:|
| Validation | 90.45% |
| Deduplicated test evaluation | Approximately 88.57% |

These values are project-specific experimental results and should be interpreted in the context of the dataset, its class distribution, preprocessing, and evaluation procedure.

They do not establish clinical effectiveness or real-world diagnostic accuracy. Reproduce the evaluation on the final model and dataset before presenting these values as verified results in a formal report.

---

##  Limitations

- The model's performance depends on the quality and representativeness of its training data.
- Predictions may be incorrect for images from different scanners, hospitals, populations, or acquisition protocols.
- Dataset imbalance, duplicate images, and data leakage can affect evaluation results.
- Resizing and preprocessing may remove or alter image details.
- The model may not generalize to images outside the training distribution.
- Output scores should not be treated as calibrated clinical probabilities.
- The application has not been established as a clinically validated diagnostic system.
- A successful prediction does not replace professional medical assessment.

**This project must not be used to diagnose, rule out, or treat a medical condition.**

---

##  Future Enhancements

Potential improvements include:

- Add model evaluation reports with precision, recall, F1-score, and confusion matrices.
- Implement Grad-CAM visualizations for model interpretability.
- Improve upload validation and error handling.
- Add automated unit and integration tests.
- Improve accessibility and responsive design.
- Add model versioning and reproducible evaluation scripts.
- Explore external-dataset validation and generalization testing.
- Add secure deployment configuration and privacy-conscious data handling.
- Optimize inference performance for suitable hardware.
- Document dataset provenance, licensing, and training methodology.

---

##  Author

**Sumit Kumar**

Computer Science and Engineering | Machine Learning | Data Science | Python Development

GitHub: [@sumitkumar2004](https://github.com/sumitkumar2004)

Project repository: [MedVision-AI-Brain-Tumor-Detection](https://github.com/sumitkumar2004/MedVision-AI-Brain-Tumor-Detection)

---

##  License

No license has been specified for this project yet.

Before distributing the project publicly, choose an appropriate license and verify that you have permission to redistribute the model, dataset, and any third-party assets. Until a license is added, others should not assume that they have permission to reuse or redistribute the project.

---

##  Support

If you find this project useful for learning about machine learning, deep learning, and Flask application development, consider starring the repository.

Thank you for visiting **MedVision AI — Brain Tumor Detection**!
