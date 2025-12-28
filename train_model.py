import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
conn = sqlite3.connect("metrics.db")
df = pd.read_sql(
    "SELECT cpu, memory, disk, network, swap FROM metrics",
    conn
)
model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

model.fit(df)

joblib.dump(model, "failure_model.pkl")

print("Model trained and saved")
