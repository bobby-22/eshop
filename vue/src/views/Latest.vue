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
        <nav class="pagination" role="navigation" aria-label="pagination">
            <a class="pagination-previous">Previous</a>
            <a class="pagination-next">Next page</a>
            <ul class="pagination-list">
                <li>
                    <a class="pagination-link" aria-label="Goto page 1">1</a>
                </li>
                <li>
                    <span class="pagination-ellipsis">&hellip;</span>
                </li>
                <li>
                    <a class="pagination-link" aria-label="Goto page 45">45</a>
                </li>
                <li>
                    <a
                        class="pagination-link is-current"
                        aria-label="Page 46"
                        aria-current="page"
                        >46</a
                    >
                </li>
                <li>
                    <a class="pagination-link" aria-label="Goto page 47">47</a>
                </li>
                <li>
                    <span class="pagination-ellipsis">&hellip;</span>
                </li>
                <li>
                    <a class="pagination-link" aria-label="Goto page 86">86</a>
                </li>
            </ul>
        </nav>
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
.title {
    border-bottom: 1px solid #ededed;
    padding-bottom: 15px;
    margin-bottom: 8px;
}
</style>
