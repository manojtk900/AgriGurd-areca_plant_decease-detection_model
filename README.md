# 🌴 AgriGuard AI - Areca Plant Disease Detection

An AI-powered web application for detecting diseases in areca plants using Deep Learning and Flask. Farmers can upload an image of an areca plant, and the system predicts the disease with a confidence score, providing a foundation for smart agricultural decision-making.

---

## 📌 Features

- 🌿 Areca plant disease detection using Deep Learning
- 📷 Upload plant images through a web interface
- 🤖 TensorFlow/Keras prediction model
- 📊 Displays prediction confidence
- 🔒 Secure image upload handling
- 🖥️ Flask-based web application
- 📱 Responsive design (Upcoming)
- 📄 PDF report generation (Upcoming)
- 🌦️ Weather integration (Upcoming)
- 🔥 Explainable AI using Grad-CAM (Upcoming)

---

## 🖼️ Demo

### Home Page

- Upload an image of an areca plant
- Click **Predict**
- View disease prediction and confidence score

---

## 📂 Project Structure

```
AgriGuard-AI/
│
├── app.py
├── train.py
├── evaluate.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── uploads/
│
├── models/                 # Not included in GitHub
├── Datasets/               # Not included in GitHub
│
└── README.md
```

---

## 🧠 Deep Learning Model

- Framework: TensorFlow / Keras
- Architecture: MobileNetV2 (Transfer Learning)
- Image Size: 224 × 224
- Optimizer: Adam
- Loss Function: Categorical Crossentropy

---

## 🎯 Model Performance

| Metric | Value |
|---------|-------|
| Test Accuracy | **97.61%** |
| Framework | TensorFlow/Keras |
| Language | Python |

---

## 🛠️ Technologies Used

- Python 3.10
- Flask
- TensorFlow
- Keras
- NumPy
- Pillow
- HTML5
- CSS3
- JavaScript

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/manojtk900/AgriGurd-areca_plant_decease-detection_model.git
```

Move into the project directory:

```bash
cd AgriGurd-areca_plant_decease-detection_model
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📷 Usage

1. Launch the application.
2. Upload an areca plant image.
3. Click **Predict**.
4. View:
   - Predicted disease
   - Confidence score
   - Uploaded image

---

## 📁 Dataset

The dataset is **not included** in this repository due to its size.

---

## 📦 Model Files

The trained TensorFlow model is **not included** in this repository.

Place the trained model inside the `models/` directory before running the application.

Example:

```
models/
│
├── plant_disease_model.keras
├── plant_disease_model.h5
└── class_indices.json
```

---

## 🛣️ Future Enhancements

- 🎨 Modern Glassmorphism UI
- 📤 Drag-and-drop image upload
- 📊 Circular confidence meter
- 🌿 Disease description
- ⚠️ Disease severity prediction
- 💊 Organic treatment recommendation
- 🧪 Chemical treatment recommendation
- 🌦️ Weather API integration
- 🔥 Grad-CAM visualization
- 📄 Downloadable PDF reports
- 🗃️ SQLite database
- 📈 Prediction history
- 👤 User authentication
- 🛠️ Admin dashboard
- ☁️ Cloud deployment
- 📱 Mobile-responsive interface

---

## 👨‍💻 Developer

**Manoj T K**

Computer Science & Engineering Student

GitHub: https://github.com/manojtk900

---

## 📜 License

This project is developed for academic, research, and educational purposes.
