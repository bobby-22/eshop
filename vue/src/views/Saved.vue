<template>
    <div class="container">
        <h1 class="title">Saved products:</h1>
        <p v-if="!this.savedProducts.length">No products saved...</p>

        <ProductsSaved
            v-for="product in savedProducts"
            v-bind:key="product.id"
            v-bind:product="product"
            v-on:unsaveProduct="unsaveProduct"
        />
    </div>
</template>

<script>
import { toast } from "bulma-toast";
import ProductsSaved from "../components/ProductsSaved";
export default {
    name: "Saved",
    components: {
        ProductsSaved,
    },
    data() {
        return {
            savedProducts: [],
        };
    },
    methods: {
        unsaveProduct(product) {
            this.savedProducts = this.savedProducts.filter((i) => {
                return i.stripe_product_id !== product.stripe_product_id;
            });
            this.$store.commit("updateSavedProductsState", product);
            toast({
                message: "Product has been unsaved!",
                type: "is-danger",
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: "bottom-right",
            });
        },
    },
    created() {
        document.title = "Saved Products | MechMarketEU";
        this.savedProducts = this.$store.state.savedProducts;
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
    padding-bottom: 15px;
    border-bottom: 1px solid #ededed;
    margin-bottom: 26px;
}
</style>
