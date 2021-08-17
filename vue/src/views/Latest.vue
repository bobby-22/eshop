<template>
<div class="columns is-multiline is-vcentered">
    <div v-for="product in latestProducts" :key="product.id" class="column is-one-quarter">
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
                    <div class="split">
                        <span class="subtitle">
                            <i class="fas fa-euro-sign"></i>
                            <span>{{ product.price }}</span>
                        </span>
                        <span class="subtitle">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>{{ product.location }}</span>
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
.card {
    border-radius: 5px;
    box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;

}
.card-image {
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    max-height: 200px;
}
.card-content {
    padding: 15px;
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
</style>
