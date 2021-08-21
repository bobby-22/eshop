import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Latest from "../views/Latest.vue"
import Details from '../views/Details.vue'
import Category from '../views/Category.vue'

const routes = [
  {
    path: '/',
    name: "Home",
    component: Home
  },
  {
    path: "/latest/",
    name: "Latest",
    component: Latest
  },
  {
    path: "/product/:stripe_product_id",
    name: "Details",
    component: Details
  },
  {
    path: "/category/:category_id",
    name: "Category",
    component: Category
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
