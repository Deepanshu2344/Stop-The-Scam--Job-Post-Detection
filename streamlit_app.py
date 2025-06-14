import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load trained model
model = joblib.load('fraud_detector.pkl')

st.title('🔍 Job Scam Detector Dashboard')

# File uploader
uploaded_file = st.file_uploader("Upload a Job Listings CSV file", type="csv")

if uploaded_file:
    # Read uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data Preview")
    st.dataframe(df.head())

    # Fill missing values
    text_columns = ['title', 'location', 'department', 'salary_range', 'company_profile',
                    'description', 'requirements', 'benefits']

    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].fillna('')

    # Combine text columns for prediction
    df['combined_text'] = df['title'] + ' ' + df['location'] + ' ' + df['company_profile'] + ' ' + df['description'] + ' ' + df['requirements'] + ' ' + df['benefits']

    # Make predictions
    predictions = model.predict(df['combined_text'])
    probabilities = model.predict_proba(df['combined_text'])[:, 1]

    df['Prediction'] = predictions
    df['Fraud_Probability'] = probabilities

    # Display results
    st.subheader("Prediction Results")
    st.dataframe(df[['title', 'location', 'Prediction', 'Fraud_Probability']])

    # Pie chart of fraud vs genuine
    st.subheader("Job Distribution (Fraud vs Genuine)")
    pie_data = df['Prediction'].value_counts()
    labels = ['Genuine', 'Fraud']
    colors = ['#00cc99', '#ff6666']
    plt.figure(figsize=(4, 4))
    plt.pie(pie_data, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.axis('equal')
    st.pyplot(plt)

    # Histogram of fraud probabilities
    st.subheader("Fraud Probability Distribution")
    plt.figure(figsize=(6, 3))
    plt.hist(df['Fraud_Probability'], bins=20, color='purple')
    plt.xlabel('Fraud Probability')
    plt.ylabel('Number of Job Listings')
    st.pyplot(plt)

    # Top-10 most suspicious job posts
    st.subheader("Top-10 Most Suspicious Job Posts")
    top_10 = df.sort_values('Fraud_Probability', ascending=False).head(10)
    st.dataframe(top_10[['title', 'location', 'Fraud_Probability']])

else:
    st.info('Upload a job listings CSV file to begin fraud detection.')

st.caption("Built with ❤️ by Deepanshu for Anveshan Hackathon June 2025")
