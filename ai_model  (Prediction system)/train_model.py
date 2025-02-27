import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("enrollment_history.csv")

# Prepare data
df["month"] = pd.to_datetime(df["date"]).dt.month
X = df[["month"]]
y = df["available_spots"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
pickle.dump(model, open("model.pkl", "wb"))