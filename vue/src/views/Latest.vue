<template>
<div class="columns is-multiline is-vcentered">
    <div v-for="product in latestProducts" :key="product.id" class="column is-one-third">
        <div class="card">
            <div class="card-image">
                <figure id="thumbnail" class="image">
                    <img v-bind:src="'http://localhost:8000' + product.thumbnail">
                </figure>
            </div>
            <div class="card-content">
                <div class="content">
                    <span class="title is-5">
                        <router-link v-bind:to="product.stripe_product_id">{{ product.name }}</router-link>
                    </span>
                </div>
                <div class="content">
                    <span class="subtitle">{{ product.price }}€</span>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import { djangoAPI } from "../axios"
export default {
    name: "LatestProducts",
    data() {
        return {
            latestProducts: null
        }
    },
    methods: {
        getProducts() {
            djangoAPI
                .get('/latest-products/',)
                .then(latestProductsResponse => {
                    this.latestProducts = latestProductsResponse.data
                    console.log(this.latestProducts)
                })
        },
    },
    created() {
        this.getProducts()
    }
}
</script>

<style scoped>
.card {
    border-radius: 5px;
}
.card-image {
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    height: 200px;
}
.content {
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin-bottom: 0px;
}
.card-content {
    padding: 15px;
}
a:link, a:visited {
    color: dodgerblue;
 }
a:active, a:hover {
  color: darksalmon;
}

</style>
