import pickle
import numpy as np

MODEL_PATH = "ai_model/model.pkl"

def predict_availability():
    """ Predicts future seat availability based on trends """
    try:
        model = pickle.load(open(MODEL_PATH, "rb"))
        future_months = np.array([[i] for i in range(1, 7)])
        predictions = model.predict(future_months)

        return [{"month": i+1, "available_spots": int(pred)} for i, pred in enumerate(predictions)]
    except Exception as e:
        return {"error": str(e)}