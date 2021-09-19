import axios from "axios";

const djangoAPI = axios.create({
    baseURL: "https://mechmarketeu.herokuapp.com/",
});

export { djangoAPI };
