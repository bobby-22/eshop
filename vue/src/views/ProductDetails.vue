<template>
<div class="container">
    <div class="holder" v-for="detail in productDetails" :key="detail.id">
        <div class="left">
            <img v-bind:src="'http://localhost:8000' + detail.thumbnail">
        </div>
        <div class="right">
            <div class="content-header">
                <p>{{ detail.name }}</p>
                <p>{{ detail.date }}</p>
                <p>{{ detail.location}}</p>
            </div>
            <div class="content-others">
                <p>{{ detail.description }}</p>
            </div>
        </div>
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
        }
    },
    created() {
        this.getDetails()
    }
}
</script>

<style scoped>
.container {
    padding: 30px
}
.holder {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.left {
    flex: 0 0 500px;
    margin-right: 50px;
}
</style>
