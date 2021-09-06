import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Latest from "../views/Latest.vue";
import Details from "../views/Details.vue";
import Category from "../views/Category.vue";
import Search from "../views/Search.vue";
import Saved from "../views/Saved.vue";
import Register from "../views/Register.vue";
import Login from "../views/Login.vue";
import Profile from "../views/Profile.vue";
import New from "../views/New.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/products/latest",
        name: "Latest",
        component: Latest,
    },
    {
        path: "/product/:stripe_product_id",
        name: "Details",
        component: Details,
    },
    {
        path: "/category/:category/products",
        name: "Category",
        component: Category,
    },
    {
        path: "/products/?search=:keyword",
        name: "Search",
        component: Search,
    },
    {
        path: "/products/savedProducts",
        name: "Saved",
        component: Saved,
    },
    {
        path: "/accounts/register",
        name: "Register",
        component: Register,
    },
    {
        path: "/accounts/login",
        name: "Login",
        component: Login,
    },
    {
        path: "/user/:user",
        name: "Profile",
        component: Profile,
    },
    {
        path: "/product/new",
        name: "New",
        component: New,
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
