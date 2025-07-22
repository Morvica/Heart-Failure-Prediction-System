#  Heart Failure Prediction Web App

This project is a machine learning-powered web application that predicts whether a patient with heart failure is likely to **survive** or **die**, based on clinical records. It provides a simple and interactive interface to input patient details.

---

##  Project Overview

Heart failure is a life-threatening condition that requires timely and accurate diagnosis. This web application uses a trained **XGBoost Classifier** model to help predict patient outcomes based on clinical parameters. 

---

##  Features

-  Predicts survival or death of heart failure patients
-  Displays probability of death
-  Uses all 12 clinical features
-  Built using Python, Flask, and scikit-learn
-  Easy to run locally — no external services required

---

##  Machine Learning Details

- **Model Used**: XGBoostClassifier  
- **Preprocessing**: StandardScaler for feature scaling  
- **Techniques**: SMOTE (for class imbalance), Hyperparameter Tuning  
- **Evaluation Metrics**:
  - Accuracy
  - Precision
  - Recall (important to catch life-risk cases)
  - F1 Score
  - ROC AUC Score

---

## 💻 How to Run This Project

### 1. Clone the Repository

```bash
```

### 2. Install Dependencies

Make sure python is installed then run:
```bash
```

if requirments,txt doesn't exist then manually install the dependencies
```bash
```

### 3. Start the Web app

```bash
python app.py
```

## Sample Output

![Uploading Screenshot 2025-07-22 231001.png…]()


