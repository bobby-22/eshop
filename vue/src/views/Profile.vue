<template>
    <div class="container">
        <h1 class="title">My products:</h1>
        <ProductsProfile
            v-for="product in products"
            v-bind:key="product.id"
            v-bind:product="product"
        />
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import ProductsProfile from "../components/ProductsProfile.vue";
export default {
    name: "Profile",
    components: {
        ProductsProfile,
    },
    data() {
        return {
            products: null,
        };
    },
    methods: {
        getProducts() {
            djangoAPI
                .get("/user/" + this.$store.state.currentUserId)
                .then((latestResponse) => {
                    console.log(latestResponse);
                    this.products = latestResponse.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    beforeCreate() {
        this.$store.commit("localStorageSavedCurrentUserId");
    },
    created() {
        (document.title = "My Products | MechMarketEU"), this.getProducts();
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
