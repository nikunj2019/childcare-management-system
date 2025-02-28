import axios from "axios";

const API_URL = "https://3.22.233.33:8000";

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  return await axios.post(`${API_URL}/upload/`, formData);
};

export const getEnrollments = async () => {
  return await axios.get(`${API_URL}/enrollments/`);
};

export const getPredictions = async () => {
  return await axios.get(`${API_URL}/predict/`);
};