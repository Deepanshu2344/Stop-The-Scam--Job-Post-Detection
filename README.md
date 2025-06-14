## 🚀 Try It Live  

👉 **Access the deployed app on Streamlit:**  
https://stop-the-scam-job-detection.streamlit.app/

Upload your own CSV job post data and get fraud risk predictions in real time.

---

# 🚨 Spot The Scam: Job Post Fraud Detection

A Machine Learning and Streamlit-based app to detect fraudulent job postings using job description text and structured features.

---

## 📖 Project Overview

Fake job listings are a growing problem on online job boards. Our project uses natural language processing and a classification model to detect potentially fraudulent job posts.  

The model analyzes job descriptions and metadata to classify posts as **Fraudulent** or **Legitimate**. An interactive Streamlit dashboard visualizes the predictions and insights.

---

## ⚙️ Key Features & Technologies Used

- **Python 3**
- **Pandas**, **NumPy** for data manipulation
- **Scikit-learn** for:
  - TF-IDF vectorization  
  - Random Forest Classifier (our final model)  
  - Evaluation metrics (F1-score, confusion matrix, ROC-AUC)
- **Matplotlib**, **Seaborn** for visualizations
- **Streamlit** for creating an interactive dashboard
- **Joblib** for saving the trained model

---

## 📥 Setup Instructions (Step-by-Step)

1. **Clone this repository**
   ```bash
   git clone https://github.com/Deepanshu2344/Spot-The-Scam--Job-Post-Detection.git
   cd Spot-The-Scam
2. Install the dependencies
    ```bash
   pip install -r requirements.txt
3. Run the Streamlit app
   ```bash
   streamlit run streamlit_app.py

---

## 📌 Data Science Focus

**Data Cleaning:** Filled missing text fields with empty strings, dropped job_id.

**Feature Engineering:** Combined multiple text columns, encoded categorical variables.

**Model Selection:** Random Forest Classifier chosen for its robustness with mixed data types and imbalanced data handling.

**Evaluation:** Measured using F1-score due to dataset imbalance. Visualized with confusion matrix and histograms in dashboard.

---

## 📊 Model Behavior & Output
->  The model takes TF-IDF features from job descriptions along with structured metadata.

-> It outputs the probability that a job post is fraudulent.

-> If this probability is high (e.g. above 0.5), the job is flagged as fake.

---

## 📈 Model Evaluation
Model Used: Random Forest Classifier

Why?
-> Excellent with imbalanced data

-> Provides feature importance

-> Robust and interpretable

🔍 Metrics:
-> F1-Score: Your model’s F1-score here

-> ROC-AUC Score

-> Confusion Matrix

---

## 📊 Dashboard & Insights
The Streamlit dashboard includes:
![Screenshot 2025-06-14 205533](https://github.com/user-attachments/assets/de045b5d-ab36-4fb5-923e-36f853b6a95e)

📑 Table of job listings with predictions and fraud probabilities
![Screenshot 2025-06-14 205623](https://github.com/user-attachments/assets/5b23db9f-c4a8-442d-ae17-b4630e59adb9)

📊 Histogram of fraud probabilities
![Screenshot 2025-06-14 205640](https://github.com/user-attachments/assets/8260827c-c020-405f-9a46-2ae712626409)

🥧 Pie chart showing % of real vs fake jobs
![Screenshot 2025-06-14 205629](https://github.com/user-attachments/assets/18b12cc0-25de-488a-902f-938890db8faf)

📈 Top-10 most suspicious job listings
![Screenshot 2025-06-14 205645](https://github.com/user-attachments/assets/60e2d8bb-d847-463a-84c0-4ca132348fae)
