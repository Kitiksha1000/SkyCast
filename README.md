# 🚀 SkyCast - Space Mission Outcome Prediction

## Kaggle Competition Link- https://www.kaggle.com/competitions/sky-cast-margazhi-25/leaderboard


## 📝 Project Overview 
SkyCast is a machine learning project designed to predict the outcome of space missions, classifying them as "Success" or "Failure". This end-to-end pipeline leverages advanced feature engineering, robust preprocessing, and cutting-edge classification models.

The project initially ranked **8th** on the public leaderboard and moved up to an impressive **6th position after the final presentation and evaluation**, securing a **finalist spot** in the SkyCast competition, part of IITM BS's Margazhi'25 fest.



## ⚙️ Features & Data Engineering
1. Feature Extraction: Key features such as mission category, launch date, country, and time of launch were extracted and processed to enhance the dataset.

2. Preprocessing: Data preprocessing steps, including scaling, encoding, and transformation, were applied using machine learning pipelines to ensure consistency and readiness for model training.

3. Redundancy Removal: Redundant features were identified and removed by detecting multicollinearity, with Chi-square tests applied to streamline the dataset.

4. Feature Creation: Additional features were created, such as grouping countries based on launch location and extracting time-based features like year and month, to provide more relevant information for model prediction.

## 🤖 Model Building
1. Stratified Sampling: Applied stratified sampling techniques to ensure balanced class distribution in both training and test sets.

2. Baseline Models: Tested six baseline models for classification:
   
  * Support Vector Classifier (SVC)
  * XGBoost
  * LightGBM
  * Random Forest Classifier
  * Logistic Regression
  * K-Nearest Neighbors (KNN)

3. Hyperparameter Tuning (HPT): Performed hyperparameter tuning (HPT) on several models:

* Random Forest Classifier: Achieved an F1-score of 0.948.
* XGBoost: Achieved the best performance with an F1-score of 0.952.
* SVC and Logistic Regression: Hyperparameter tuning was also performed on these models for further optimization.

4. Ensemble Methods: Implemented ensemble techniques to improve model performance:

* Bagging, Boosting, and Voting were explored, with Gradient Boosting achieving an F1-score of 0.949.

## 📈 Final Results
The final XGBoost model achieved:

* Training Set F1-Score: 0.95285
* Test Set F1-Score: 0.95006


## 🧪 Gradio App: Interactive UI Deployment  

To make the model accessible to users, a Gradio-based web app was developed. The app allows users to input details such as:

- Company Name
- Rocket Status
- Year and Month of Launch
- Rocket Type
- Country of Launch

And receive an instant "Yes/No" prediction on mission success.

### 💻 How it works:

- User fills dropdowns (from a pre-validated list of options).
- Backend uses saved .pkl files (model + pipeline) to transform and predict.
- Outputs user-friendly prediction.

Note: App was built using Gradio and tested locally in Google Colab. It can also be deployed on Hugging Face Spaces for public sharing.

---

## 📁 Project Structure

app.py                  # Gradio app  
model2.pkl              # Saved XGBoost model  
pipeline.pkl            # Preprocessing pipeline  
requirements.txt        # Dependencies  
screenshots/            # Screenshots of app  
recordings/             # Screen recording (optional)  
README.md               # Project overview  

---

## 🪄 Steps to Reproduce Locally

1. Clone repo
2. Install requirements:
   pip install -r requirements.txt
3. Run the app:
   python app.py

---

## 🖼️ Screenshots

Add screenshots of your Gradio UI here  
(Place them in the /screenshots folder)

---

## 🎥 Screen Recording

Upload a short demo of your Gradio UI interaction  
(Place it in the /recordings folder)

---

## 🧠 Tech Stack

- Python, Pandas, Scikit-learn, XGBoost, Gradio
- Feature Engineering, Pipelines, Model Serialization (joblib)
- UI with Gradio + Local Testing in Google Colab
