import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Terms from "../views/Terms.vue";
import Error from "../views/Error.vue";
import Latest from "../views/Latest.vue";
import Details from "../views/Details.vue";
import Category from "../views/Category.vue";
import Search from "../views/Search.vue";
import Saved from "../views/Saved.vue";
import Register from "../components/Register.vue";
import Login from "../components/Login.vue";
import Profile from "../views/Profile.vue";
import User from "../views/User.vue";
import ProductsCreate from "../components/ProductsCreate.vue";
import ProductsUpdate from "../components/ProductsUpdate.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/terms/",
        name: "Terms",
        component: Terms,
    },
    {
        path: "/error/:message/",
        name: "Error",
        component: Error,
    },
    {
        path: "/products/latest/",
        name: "Latest",
        component: Latest,
    },
    {
        path: "/products/:stripe_product_id/",
        name: "Details",
        component: Details,
    },
    {
        path: "/products/category/:category/",
        name: "Category",
        component: Category,
    },
    {
        path: "/products/?search=:keyword/",
        name: "Search",
        component: Search,
    },
    {
        path: "/products/saved/",
        name: "Saved",
        component: Saved,
    },
    {
        path: "/accounts/register/",
        name: "Register",
        component: Register,
    },
    {
        path: "/accounts/login/",
        name: "Login",
        component: Login,
    },
    {
        path: "/accounts/profile/:profile/",
        name: "Profile",
        component: Profile,
    },
    {
        path: "/accounts/user/:user/",
        name: "User",
        component: User,
    },
    {
        path: "/products/create/",
        name: "ProductsCreate",
        component: ProductsCreate,
    },
    {
        path: "/products/:stripe_product_id/update/",
        name: "ProductsUpdate",
        component: ProductsUpdate,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
