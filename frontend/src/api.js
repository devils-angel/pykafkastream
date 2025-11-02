import axios from "axios";

const API = axios.create({
  baseURL: "http://flask-app:5000/", // your Flask backend
});

export const loginUser = (data) => API.post("/login", data);
export const registerUser = (data) => API.post("/register", data);
export const fetchData = () => API.get("/data");