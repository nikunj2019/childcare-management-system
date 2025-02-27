import { useEffect, useState } from "react";
import { getPredictions } from "../services/api";

const Predictions = () => {
  const [predictions, setPredictions] = useState([]);

  useEffect(() => {
    getPredictions().then((res) => setPredictions(res.data));
  }, []);

  return (
    <div>
      <h2 className="text-xl font-bold mb-2">📊 Future Availability Predictions</h2>
      <ul className="bg-white p-4 rounded shadow-md">
        {predictions.map((pred, index) => (
          <li key={index} className="border-b py-2">
            {pred.month}: {pred.available_spots} spots available
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Predictions;