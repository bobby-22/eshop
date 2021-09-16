<template>
    <div class="container">
        <h1 class="title">Latest posts</h1>
        <div class="columns is-multiline is-variable is-2" id="columns">
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
            document.title = "Latest Posts | MechMarketEU";
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
#columns {
    margin-top: 0px;
}
.title {
    border-bottom: 1px solid #ededed;
    padding-bottom: 15px;
    margin-bottom: 8px;
}
</style>
