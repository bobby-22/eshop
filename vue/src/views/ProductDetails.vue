<template>
<div class="container">
    <h1>Title</h1>
    <div id="test" v-for="detail in productDetails" :key="detail.id">
        <p>{{ detail.name }}</p>
    </div>
</div>
</template>

<script>
import { djangoAPI } from "../axios"
export default {
    name: "ProductDetails",
    data() {
        return {
            productDetails: null,
        }
    },
    methods: {
        getDetails() {
            let stripe_product_id = this.$route.params.stripe_product_id
            djangoAPI({
                method: "GET",
                url: `${stripe_product_id}`
            }).then(productDetailsResponse => {
                this.productDetails = productDetailsResponse.data
            })
        },
    },
    created() {
        this.getDetails()
    },
}
</script>

<style>
</style>
