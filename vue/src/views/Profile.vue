<template>
    <div class="container">
        <h1 class="title">
            My products:
            <router-link id="new" to="/product/new">
                <i class="far fa-plus-square"></i>
            </router-link>
        </h1>
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

<style scoped>
.container {
    min-height: 100%;
    padding: 30px;
}
.title {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding-bottom: 15px;
    border-bottom: 1px solid #ededed;
    margin-bottom: 26px;
}
a#new {
    color: #424242;
}
#new:hover {
    color: black;
}
</style>
