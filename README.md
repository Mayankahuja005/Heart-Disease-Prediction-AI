# Heart-Disease-Prediction-AI

A machine learning web application built with **Python, Streamlit, and KNN** that predicts the risk of heart disease based on user-provided health parameters.

## 🚀 Features

* ❤️ Heart disease risk prediction
* 🧠 K-Nearest Neighbors (KNN) machine learning model
* 📊 User-friendly Streamlit interface
* 🎛️ Interactive health parameter inputs
* ⚡ Real-time prediction
* 🎨 Clean and responsive UI
* 📦 Pre-trained model and scaler included

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Scikit-learn**
* **Joblib**
* **KNN (K-Nearest Neighbors)**

## 📁 Project Structure

```text
Heart-Disease-Prediction-AI/
│
├── app.py
├── KNN_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Mayankahuja005/Heart-Disease-Prediction-AI.git
```

Go to the project directory:

```bash
cd Heart-Disease-Prediction-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 Machine Learning Model

The application uses a **K-Nearest Neighbors (KNN)** classifier for prediction.

Before prediction, user input is processed and transformed using the saved **scaler**, and the input columns are arranged according to the trained model's expected columns.

## 📊 Input Parameters

The application takes the following information:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak
* ST Slope

## ⚠️ Disclaimer

This application is developed for **educational and demonstration purposes only**. The prediction should not be considered a medical diagnosis or a substitute for professional medical advice.

## 👨‍💻 Author

**Mayank Ahuja**

B.Tech – Artificial Intelligence & Machine Learning
