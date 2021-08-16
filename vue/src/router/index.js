import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Latest from "../views/Latest.vue"
import ProductDetails from '../views/ProductDetails.vue'

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
    path: "/:stripe_product_id",
    name: "ProductDetails",
    component: ProductDetails
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
