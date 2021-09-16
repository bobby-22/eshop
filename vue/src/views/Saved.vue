<template>
    <div class="container">
        <h1 class="title">Saved posts</h1>
        <p v-if="!this.savedProducts.length">No posts saved...</p>

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
            savedProducts: this.$store.state.savedProducts,
        };
    },
    methods: {
        unsaveProduct(product) {
            this.savedProducts = this.savedProducts.filter((i) => {
                return i.post_id !== product.post_id;
            });
            this.$store.commit("updateSavedProductsState", product);
            toast({
                message: "Post has been unsaved!",
                type: "is-danger",
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: "bottom-right",
            });
        },
        setTitle() {
            document.title = "Saved Posts | MechMarketEU";
        },
    },
    beforeCreate() {
        this.$store.commit("localStorageSavedProducts");
    },
    created() {
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
    border-bottom: 1px solid #ededed;
    padding-bottom: 15px;
    margin-bottom: 20px;
}
</style>
