<template>
    <div class="container">
        <h1 class="title">Latest products</h1>
        <div class="columns is-multiline">
            <Products
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product"
            />
        </div>
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import Products from "../components/Products.vue";
export default {
    name: "Latest",
    components: {
        Products,
    },
    data() {
        return {
            products: null,
        };
    },
    methods: {
        getLatestProducts() {
            djangoAPI
                .get("/api/v1/products/latest/")
                .then((latestResponse) => {
                    console.log(latestResponse);
                    this.products = latestResponse.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        setTitle() {
            document.title = "Latest Products | MechMarketEU";
        },
    },
    created() {
        this.getLatestProducts();
        this.setTitle();
    },
};
</script>

<style scoped>
.container {
    min-height: 100%;
    max-width: 100%;
    padding: 30px;
}
.title {
    padding-bottom: 15px;
    border-bottom: 1px solid #ededed;
    margin-bottom: 26px;
}
</style>
