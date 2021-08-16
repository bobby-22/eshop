<template>
<div class="container">
    <div v-for="detail in productDetails" :key="detail.id">
        <img v-bind:src="'http://localhost:8000' + detail.image">
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
                console.log(this.productDetails)
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
