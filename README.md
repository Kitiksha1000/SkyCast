# SkyCast - Space Mission Outcome Prediction

## Description: 
SkyCast is a machine learning project designed to predict the outcome of space missions, classifying them as "Success" or "Failure." The project leverages extensive feature engineering and model tuning techniques to deliver highly accurate predictions. It was developed and showcased as a finalist (Rank 6) in the SkyCast competition, part of IITM BS's Margazhi'25 fest, which focused on predicting the outcomes of rocket launches.

## Features and Data Engineering
1. Feature Extraction: Key features such as mission category, launch date, country, and time of launch were extracted and processed to enhance the dataset.

2. Preprocessing: Data preprocessing steps, including scaling, encoding, and transformation, were applied using machine learning pipelines to ensure consistency and readiness for model training.

3. Redundancy Removal: Redundant features were identified and removed by detecting multicollinearity, with Chi-square tests applied to streamline the dataset.

4. Feature Creation: Additional features were created, such as grouping countries based on launch location and extracting time-based features like year and month, to provide more relevant information for model prediction.

## Model Building
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

## Performance Metrics
The final XGBoost model achieved:

* Training Set F1-Score: 0.95285
* Test Set F1-Score: 0.95006


