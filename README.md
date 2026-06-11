# 🩺 Multiple Disease Prediction System

A Machine Learning and Streamlit-based web application that predicts the likelihood of three major diseases:

* Diabetes Prediction
* Heart Disease Prediction
* Parkinson's Disease Prediction

The application provides an easy-to-use interface where users can enter medical parameters and receive instant predictions powered by trained Machine Learning models.

---

## 🚀 Features

### Diabetes Prediction

Predicts whether a person is diabetic based on clinical measurements such as:

* Pregnancies
* Glucose Level
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

### Heart Disease Prediction

Predicts the likelihood of heart disease using medical attributes including:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise Induced Angina
* Oldpeak
* Slope
* CA
* Thal

### Parkinson's Disease Prediction

Predicts Parkinson's Disease using biomedical voice measurements such as:

* MDVP:Fo(Hz)
* MDVP:Fhi(Hz)
* MDVP:Flo(Hz)
* Jitter Measures
* Shimmer Measures
* NHR
* HNR
* RPDE
* DFA
* Spread1
* Spread2
* D2
* PPE

---

## 🛠️ Technologies Used

* Python
* Machine Learning
* Scikit-learn
* NumPy
* Pandas
* Pickle
* Streamlit
* Streamlit Option Menu

---

## 📊 Machine Learning Models

| Disease                        | Algorithm                    |
| ------------------------------ | ---------------------------- |
| Diabetes Prediction            | Support Vector Machine (SVM) |
| Heart Disease Prediction       | Support Vector Machine (SVM) |
| Parkinson's Disease Prediction | Support Vector Machine (SVM) |

---


## 📂 Project Structure


MULTIPLE_DISEASE_PREDICTION/
│
├── app.py
├── requirements.txt
├── README.md
│
├── savedModels/
│   ├── diabetes.sav
│   ├── heart.sav
│   └── parkinsons.sav
│
├── Dataset/
│   ├── diabetes.csv
│   ├── heart.csv
│   └── parkinsons.csv
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd MULTIPLE_DISEASE_PREDICTION
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📋 Requirements

```text
streamlit
streamlit-option-menu
numpy
pandas
scikit-learn
```

---

## 🎯 Project Objectives

* Apply Machine Learning algorithms to healthcare datasets.
* Build a real-world disease prediction application.
* Develop an interactive web application using Streamlit.
* Demonstrate end-to-end Machine Learning deployment skills.

---

## 🔮 Future Improvements

* Add more disease prediction models.
* Improve model accuracy through hyperparameter tuning.
* Integrate database support.
* Deploy using Streamlit Community Cloud.
* Add patient report generation functionality.

---

## 👨‍💻 Author

**Chetan Auti**

Aspiring Data Scientist | Machine Learning Enthusiast | Python Developer

---

## ⭐ Acknowledgements

Special thanks to the open-source community and healthcare datasets that made this project possible.

If you found this project useful, consider giving it a ⭐ on GitHub.
