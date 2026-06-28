import pandas as pd


def test_no_missing_values():
    df = pd.read_csv("../data/telco-customer-churn.csv")
    assert df.isnull().sum().sum() == 0, "Dataset contains missing values!"
    print("All tests passed!")