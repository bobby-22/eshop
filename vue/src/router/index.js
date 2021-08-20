import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Latest from "../views/Latest.vue"
import ProductDetails from '../views/ProductDetails.vue'
import Category from '../views/Category.vue'

const routes = [
  {
    path: '/',
    name: "Home",
    component: Home
  },
  {
    path: "/latest-products/",
    name: "LatestProducts",
    component: Latest
  },
  {
    path: "/product/:stripe_product_id",
    name: "ProductDetails",
    component: ProductDetails
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
