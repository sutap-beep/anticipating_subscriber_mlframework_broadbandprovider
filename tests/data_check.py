import pandas as pd

df = pd.read_csv("data/telco-customer-churn.csv")

# Simple automated test
assert df.isnull().sum().sum() == 0, "Dataset contains missing values!"

print("All tests passed!")