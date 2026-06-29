import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

model = joblib.load("../models/random_forest_model.pkl")

df = pd.read_csv("../data/processed_dataset.csv")

# CHURN DISTRIBUTION VISUALIZATION
st.subheader("Subscriber Churn Distribution")

fig, ax = plt.subplots(figsize=(8, 6))

df['Churn'] = df['Churn'].map({0: 'No', 1: 'Yes'})

df['Churn'].value_counts().plot(
    kind="bar",
    ax=ax
)
ax.set_xlabel("Churn")
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.set_ylabel("Number of Subscriber")
ax.set_title("Subscriber Churn Distribution")

st.pyplot(fig)

# MONTHLY CHARGES DISTRIBUTION VISUALIZATION
st.subheader("Monthly Charges Distribution")

fig, ax = plt.subplots(figsize=(8, 6))

ax.hist(df['MonthlyCharges'], bins=20)

ax.set_xlabel("Monthly Charges")
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.set_ylabel("Number of Customers")
ax.set_title("Distribution of Monthly Charges")

st.pyplot(fig)

# FEATURE IMPORTANCE VISUALIZATION
X = df.drop("Churn", axis=1)

feature_importance = pd.DataFrame({
    "Feature":X.columns,
    "Importance":model.feature_importances_
}).sort_values("Importance",ascending=False)

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

st.subheader("Feature Importance")

fig, ax = plt.subplots(figsize=(8, 6))

ax.barh(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

ax.invert_yaxis()

st.pyplot(fig)


# INTERACTIVE FEATURES 
tenure = st.slider("Tenure", 0, 72, 12)

monthly_charges = st.slider("Monthly Charges", 0, 150, 70)

total_charges = st.slider("Total Charges", 0, 10000, 1000)

labels = {"Month-to-Month": 0,
          "1 Year": 1,
          "2 Year": 2
          }

contract = st.selectbox(
    "Contract Type",
    options = labels.keys()
)

# Example simplified input
input_data = pd.DataFrame({
    # For weak correlation, value is set to 0,1, some cases 2. 
    "gender": [1], 
    "SeniorCitizen": [0],
    "Partner": [1],
    "Dependents": [0],
    "tenure": [tenure],
    "PhoneService": [1],
    "MultipleLines": [0],
    "InternetService": [1],
    "OnlineSecurity": [0],
    "OnlineBackup": [1],
    "DeviceProtection": [0],
    "TechSupport": [0],
    "StreamingTV": [1],
    "StreamingMovies": [1],
    "Contract": labels[contract],
    "PaperlessBilling": [1],
    "PaymentMethod": [2],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})

# PREDICTION
prediction = model.predict(input_data)

probability = model.predict_proba(input_data)

if prediction[0] == 1:
    st.error("Customer is likely to churn")
else:
    st.success("Customer is likely to stay")


st.write("Churn Probability:", probability[0][1])


