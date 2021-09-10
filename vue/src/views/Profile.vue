<template>
    <div class="container">
        <h1 class="title">
            My products:
            <router-link id="new" to="/product/new">
                <i class="far fa-plus-square"></i>
            </router-link>
        </h1>
        <p v-if="!products.length">No products added...</p>
        <ProductsProfile
            v-for="product in products"
            v-bind:key="product.id"
            v-bind:product="product"
            v-on:deleteProduct="deleteProduct"
        />
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import { toast } from "bulma-toast";
import ProductsProfile from "../components/ProductsProfile.vue";
export default {
    name: "Profile",
    components: {
        ProductsProfile,
    },
    data() {
        return {
            products: [],
        };
    },
    methods: {
        getUserProducts() {
            djangoAPI
                .get("/api/v1/user/" + this.$store.state.currentUserId)
                .then((latestResponse) => {
                    console.log(latestResponse);
                    this.products = latestResponse.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        deleteProduct(product) {
            this.products = this.products.filter((i) => {
                return i.stripe_product_id !== product.stripe_product_id;
            });
            toast({
                message: "Product has been successfully deleted!",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: "bottom-right",
            });
        },
        setTitle() {
            document.title = "My Products | MechMarketEU";
        },
    },
    beforeCreate() {
        this.$store.commit("localStorageSavedCurrentUserId");
    },
    created() {
        this.getUserProducts();
        this.setTitle();
    },
};
</script>

<style scoped>
.container {
    min-height: 100%;
    width: 100%;
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
