import pickle
import numpy as np

# Load Model
model = pickle.load(open("model.pkl", "rb"))

# Predict for next 6 months
future_months = np.array([[i] for i in range(1, 7)])
predictions = model.predict(future_months)

# Output Predictions
for month, spots in zip(range(1, 7), predictions):
    print(f"Month {month}: {int(spots)} spots available")