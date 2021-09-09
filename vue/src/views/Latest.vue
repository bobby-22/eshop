<template>
    <div class="container">
        <h1 class="title">Latest products:</h1>
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
        getProducts() {
            djangoAPI
                .get("/api/v1/products/latest", {
                    headers: {
                        Authorization: `JWT ${this.$store.state.tokenAccess}`,
                    },
                })
                .then((latestResponse) => {
                    console.log(latestResponse);
                    this.products = latestResponse.data;
                })
                .catch((error) => {
                    console.log(error);
                    if (error) {
                        this.$store.commit("removeCredentialsState");
                        this.$router.push("/accounts/login");
                    }
                });
        },
    },
    created() {
        (document.title = "Latest Products | MechMarketEU"), this.getProducts();
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
