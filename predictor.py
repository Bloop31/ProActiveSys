import sqlite3
import pandas as pd
import joblib
from root_cause import identify_root_cause

# Load trained model
model = joblib.load("failure_model.pkl")

conn = sqlite3.connect("metrics.db")

def predict_failure():
    df = pd.read_sql(
        "SELECT cpu, memory, disk, network, swap FROM metrics ORDER BY timestamp DESC LIMIT 1",
        conn
    )

    prediction = model.predict(df)[0]

    if prediction == -1:
        cause = identify_root_cause(df.iloc[0])
        return {
            "status": "FAILURE RISK",
            "root_cause": cause
        }
    else:
        return {
            "status": "NORMAL",
            "root_cause": None
        }
