# 🌴 AgriGuard AI

> AI-Powered Areca Plant Disease Detection and Agricultural Advisory System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

AgriGuard AI is a deep learning–based web application that detects diseases in **Areca (Betel Nut) plants** using image classification.

The application predicts the disease from an uploaded image and provides:

- 🌿 Disease prediction
- 📊 Prediction confidence
- 🩺 Symptoms
- 🌱 Organic treatment recommendations
- 💊 Chemical treatment recommendations
- 🛡 Prevention methods
- 💡 Farmer tips

This project aims to assist farmers with quick and accessible disease diagnosis.

---

## ✨ Features

- AI-based disease detection
- Modern responsive Flask web interface
- Drag & Drop image upload
- Image preview
- Confidence score
- Disease knowledge base (JSON)
- Organic treatment suggestions
- Chemical treatment suggestions
- Prevention recommendations
- Farmer advisory tips
- Secure image upload
- Unknown image handling

---

## 🧠 Diseases Supported

| Disease |
|----------|
| Healthy Leaf |
| Healthy Nut |
| Healthy Trunk |
| Healthy Foot |
| Bud Borer |
| Yellow Leaf Disease |
| Stem Cracking |
| Stem Bleeding |
| Mahali (Koleroga) |

---

## 🛠 Tech Stack

- Python
- Flask
- TensorFlow / Keras
- NumPy
- Pillow
- HTML5
- CSS3
- JavaScript

---

## 📂 Project Structure

```
AgriGuard-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── disease_info.json
│
├── models/
│   ├── plant_disease_model.keras
│   ├── plant_disease_model.h5
│   └── class_indices.json
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── uploads/
│
├── templates/
│   └── index.html
│
├── train.py
├── evaluate.py
│
└── Datasets/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/manojtk900/AgriGurd-areca_plant_decease-detection_model.git
```

Go to the project

```bash
cd AgriGurd-areca_plant_decease-detection_model
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📊 Model Information

Model: CNN (TensorFlow / Keras)

Input Size:

```
224 × 224 × 3
```

Prediction Classes:

```
9 Classes
```

Image Preprocessing:

- RGB Conversion
- Resize (224 × 224)
- Pixel Normalization
- Batch Dimension Expansion

---

## 🌿 Prediction Output

The system displays

- Disease Name
- Confidence Score
- Disease Status
- Severity
- Affected Part
- Symptoms
- Organic Treatment
- Chemical Treatment
- Prevention
- Farmer Tips

---

## 📸 Screenshots

Add screenshots here.

Example:

```
screenshots/home.png
screenshots/result.png
```

---

## 🔮 Future Improvements

- SQLite prediction history
- PDF report generation
- Weather API integration
- Grad-CAM explainable AI
- Farmer dashboard
- User authentication
- Admin panel
- Mobile optimization
- REST API
- Deployment on Render / Azure / AWS

---

## 👨‍💻 Developer

**Manoj T K**

Computer Science & Engineering

GitHub

https://github.com/manojtk900

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
