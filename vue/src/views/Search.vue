<template>
    <div class="container">
        <h1 class="title">Searched keyword: "{{ keyword }}"</h1>
        <div class="columns is-multiline">
            <Products
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product"
                v-bind:src="product.thumbnail"
            />
        </div>
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import Products from "../components/Products.vue";
export default {
    name: "Search",
    components: {
        Products,
    },
    data() {
        return {
            products: null,
            keyword: null,
        };
    },
    methods: {
        getProducts() {
            let keyword = this.$route.params.keyword;
            djangoAPI({
                method: "GET",
                url: `/search/?search=${keyword}`,
            })
                .then((searchResponse) => {
                    console.log(searchResponse);
                    this.products = searchResponse.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        getTitle() {
            document.title = `${this.$route.params.keyword} | MechMarketEU`;
        },
        getKeyword() {
            return (this.keyword = this.$route.params.keyword);
        },
    },
    created() {
        this.getProducts();
        this.getTitle();
        this.getKeyword();
    },
    watch: {
        $route(to, from) {
            if (to.name === "Search") {
                this.getProducts();
                this.getTitle();
                this.getKeyword();
            }
        },
    },
};
</script>

<style scoped>
.container {
    min-height: 100%;
    min-width: 100%;
    padding: 30px;
}
.title {
    padding-bottom: 15px;
    border-bottom: 1px solid #ededed;
    margin-bottom: 26px;
}
</style>
