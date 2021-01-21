import axios from "axios";
import { BASE_URL } from "../services/ApiEndpoints";

const API = axios.create({
  baseURL: BASE_URL,
  params: {},
});

export default API;
