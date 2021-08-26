import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Latest from "../views/Latest.vue"
import Details from '../views/Details.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Bookmark from '../views/Bookmark.vue'
import Register from '../views/Register.vue'

const routes = [
  {
    path: '/',
    name: "Home",
    component: Home
  },
  {
    path: "/products/latest",
    name: "Latest",
    component: Latest
  },
  {
    path: "/product/:stripe_product_id",
    name: "Details",
    component: Details
  },
  {
    path: "/category/:category_id/products",
    name: "Category",
    component: Category
  },
  {
    path: "/products/?search=:keyword",
    name: "Search",
    component: Search
  },
  {
    path: "/products/bookmark",
    name: "Bookmark",
    component: Bookmark
  },
  {
    path: "/accounts/register",
    name: "Register",
    component: Register
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
