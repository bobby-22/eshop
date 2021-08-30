import axios from "axios";

const djangoAPI = axios.create({
    baseURL: "http://localhost:8000",
});

export { djangoAPI };
