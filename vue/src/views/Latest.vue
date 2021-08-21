<template>
<div class="columns is-multiline">
    <Cards
        v-for="product in products"
        v-bind:key="product.id" 
        v-bind:product="product"
    />
</div>
</template>

<script>
import { djangoAPI } from "../axios"
import Content from "../components/Content.vue"
export default {
    name: "Latest",
    components: { Content },
    data() {
        return {
            products: null
        }
    },
    methods: {
        getProducts() {
            djangoAPI
                .get('/latest/')
                .then(latestResponse => {
                    this.products = latestResponse.data
                })
        }
    },
    created() {
        document.title = "Latest Products | MechMarketEU",
        this.getProducts()
    }
}
</script>

<style scoped>
.columns.is-multiline {
    padding: 30px;
}
</style>
