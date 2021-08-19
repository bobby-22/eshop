<template>
<div class="columns is-multiline is-mobile is-vcentered">
    <div v-for="product in latestProducts" :key="product.id" class="column is-one-quarter-desktop is-one-third-tablet is-half-mobile">
        <div class="card">
            <div class="card-image">
                <router-link v-bind:to="product.stripe_product_id">
                    <img v-bind:src="'http://localhost:8000' + product.thumbnail">
                </router-link>
            </div>

            <div class="card-content">
                <div class="content">
                    <span class="title is-5">
                        <router-link v-bind:to="product.stripe_product_id">{{ product.name }}</router-link>
                    </span>
                </div>
                <div class="content" style="border-top: 1px solid #f0f0f0;">
                    <div class="split">
                        <span class="subtitle">
                            <i class="fas fa-euro-sign"></i>
                            <span>{{ product.price }}</span>
                        </span>
                        <span class="subtitle">
                            <i class="fas fa-map-marker-alt"></i>
                            <span style="font-weight:300;">{{ product.location }}</span>
                        </span>
                    </div>
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
        }
    },
    created() {
        this.getProducts()
    }
}
</script>

<style scoped>
.columns.is-multiline.is-vcentered {
    padding: 30px;
}
.column.is-one-quarter-desktop.is-one-third-tablet.is-half-mobile {
    padding: 8px;
}
.card {
    box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
}
.card-content {
    padding: 15px;
}
.content {
    margin: 0px 0px 10px;
}
.split {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0px;
    margin-top: 5px;
    padding-bottom: 0px;
}
.subtitle {
    -webkit-text-size-adjust: none;
    align-items: baseline;
    margin-bottom: 0px;
}
.fas {
    margin-right: 5px;
}
a:link, a:visited {
    color: dodgerblue;
 }
a:active, a:hover {
    color: darksalmon;
}
img {
    height: 200px;
    width: 800px;
    object-fit: cover;
}
</style>
