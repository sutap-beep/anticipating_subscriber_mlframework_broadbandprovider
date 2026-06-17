# Anticipating Subscriber Churn Through a Predictive Framework for a Fiber Broadband Provider

## 📌 Executive Summary & Business Context
In the highly competitive high-speed fiber broadband sector, customer acquisition costs (CAC) are exceptionally high. Retaining active lines is critical to protecting recurring revenue. A major business vulnerability involves subscribers on rolling, short-tenure "Month-to-Month contracts". These users frequently switch providers the moment promotional discounts or initial billing periods conclude.

Instead of treating churn as a generic data problem, this predictive framework is designed as a strategic commercial tool for the "Retention Marketing Team" and "Chief Marketing Officer (CMO)". By proactively identifying month-to-month broadband accounts with high churn probabilities, the business can execute targeted "Contract-Migration Campaigns"—incentivising high-risk users to transition into stable 12- or 24-month fixed line agreements before they deactivate services.

##  Strategic Business Objectives
1. Identify High-Risk Accounts: Flag rolling month-to-month broadband accounts showing early behavioral triggers of contract non-renewal.
2. Protect Monthly Recurring Revenue (MRR): Quantify total "Revenue at Risk" to justify proactive marketing intervention budgets.
3. Optimise Customer Lifetime Value (CLV): Increase subscriber lifespans by converting short-term accounts into multi-year contractual commitments.

## Industry-Specific KPIs
Progress is tracked using business performance metrics rather than pure algorithmic evaluation:
1. Contract Migration Conversion Rate: The percentage of predicted high-risk month-to-month subscribers successfully moved to fixed terms.
2. Line Deactivation Rate (Subscriber Churn): The monthly percentage reduction in active residential broadband connections.
3. Revenue at Risk (RmR): Total monthly recurring revenue directly tied to accounts flagged with a churn probability over 60%.

## Prescriptive Business Recommendations
Based on the underlying behavioral data analyzed by the predictive engine, the following automated interventions are integrated into the pipeline workflow:

1. Automated Contract Upgrades: Accounts flagged with high churn risks are automatically routed to a retention queue. The system suggests offering a complimentary 3-month network speed upgrade (e.g., from 100Mbps to 500Mbps) conditional on signing a stable 24-month fixed contract.
2. Payment Method Incentivisation: The analytics show a strong correlation between manual digital checkouts/paper billing and high churn rates. The framework recommends offering a one-off RM15 statement credit to high-risk subscribers if they register for automatic credit card or direct debit billing.


--------------------------------------OLD INFORMATION-------------------------------------------
Project Overview:
This project predicts customer churn for a telecom company using machine learning.
The goal is to identify customers who are likely to stop using the service sot that proactive
retention strategies can be applied.

The Project includes:
1. Data exploration and cleaning.
2. Feature engineering.
3. Machine Learning Model Training.
4. Model Evaluation.
5. Interactive Dashboards for Predictions.

Dataset Used:
Kaggle, Telco Customer Churn.

Business Objectives:
1. Predict whether a customer will churn.
2. Identify key factors influencing churn.
3. Help business improve customer retention strategies.

Libraries used/ Tech Stack:
1. Python.
2. Pandas.
3. Matplotlib, Seaborn.
4. Scikit-learn.
5. Streamlit.
6. Joblib.

Project Workflow:
1. Business Understanding.
2. Data Exploratin (EDA).
3. Data Cleaning.
4. Feature Engineering.
5. Model Training (Logistic Regression).
6. Model Evaluation.
7. Prediction System.
8. Interactive Dashboard.

Machine Learning Model:
Algorithm: Logistic Regression.
Target: Customer Churn (Yes/No)
Evaluation Metrics:
1. Accuracy.
2. Confusion Matrix.

Key Insights:
1. Month-to-month contract customers are more likely to churn.
2. Longer tenure reduce churn probability.
3. Payment method and service type influence churn behavior.

Streamlit Dashboard:
1. Input customers details.
2. Predict churn probability.
3. View real-time results.

to run the app:
streamlit run app/app.py

How to run this project:
1. Clone the repository:
git clone https://github.com/

2. Install dependencies:
pip install -r requirements.txt

3. Launch Dashboard:
streamlit run app/app.py

Project Structure:
customer-churn-ai-dashboard/
|
|-- data/
|-- notebooks/
|-- src/
|-- models/
|-- app/
|-- reports/
|-- requirements.txt
|-- README.md

IMPROVEMENTS THAT CAN BE MADE:
1. Using advance model i.e: Random Forest, XGBoost
2. Handle Class Imbalance, SMOTE.
3. Improve Dashboard UI
4. Deploy Online.

Project is tested for deployment using Streamlit Cloud.
bash:
streamlit run app/app.py

LIVE DEMO: STREAMLIT APP
https://customer-churn-ai-dashboard-ucnhm7cqbu5vzeyehtpqid.streamlit.app
