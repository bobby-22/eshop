<template>
    <div class="container">
        <h1 class="title">Saved products:</h1>
        <ProductsSaved
            v-for="item in savedProducts.items"
            v-bind:key="item.product.id"
            v-bind:item="item"
            v-on:unsaveProduct="unsaveProduct"
        />
    </div>
</template>

<script>
import ProductsSaved from "../components/ProductsSaved";
export default {
    name: "Saved",
    components: {
        ProductsSaved,
    },
    data() {
        return {
            savedProducts: {
                items: [],
            },
        };
    },
    methods: {
        updateSavedProducts() {
            localStorage.setItem(
                "savedProducts",
                JSON.stringify(this.$store.state.savedProducts)
            );
        },
        unsaveProduct(item) {
            this.savedProducts.items = this.savedProducts.items.filter((i) => {
                return (
                    i.product.stripe_product_id !==
                    item.product.stripe_product_id
                );
            });
            this.updateSavedProducts();
            this.$router.go(0);
        },
    },
    created() {
        document.title = "Saved Products | MechMarketEU";
        this.savedProducts = this.$store.state.savedProducts;
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
