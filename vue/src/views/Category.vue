<template>
    <div class="container">
        <h1 class="title">Category {{ this.$route.params.category_id }}:</h1>
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
    name: "Category",
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
            let category = this.$route.params.category;
            djangoAPI({
                method: "GET",
                url: `/category/${category}`,
            })
                .then((categoryResponse) => {
                    console.log(categoryResponse);
                    this.products = categoryResponse.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    created() {
        (document.title = "Category | MechMarketEU"), this.getProducts();
    },
    watch: {
        $route(to, from) {
            if (to.name === "Category") {
                this.getProducts();
            }
        },
    },
};
</script>

<style lang="scss" scoped>
$title-border-top-color: #ededed;
.container {
    min-height: 100%;
    padding: 30px;
}
.title {
    padding-bottom: 15px;
    border-bottom: 1px solid $title-border-top-color;
    margin-bottom: 26px;
}
</style>
