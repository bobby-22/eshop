<template>
<div class="container">
    <div class="details" v-for="detail in productDetails" :key="detail.id">
        <div class="details-left">
            <div class="detail-thumbnail">
                <img v-bind:src="'http://localhost:8000' + detail.thumbnail">
            </div>
            <div class="detail-images">
                <img v-bind:src="'http://localhost:8000' + detail.image">
                <img v-bind:src="'http://localhost:8000' + detail.image">
                <img v-bind:src="'http://localhost:8000' + detail.image">
                <img v-bind:src="'http://localhost:8000' + detail.image">
                <img v-bind:src="'http://localhost:8000' + detail.image">
            </div>
        </div>

        <div class="details-right">
            <div class="detail-header">
                <p>{{ detail.name }}</p>
                <p>{{ detail.date }}</p>
                <p>{{ detail.location}}</p>
            </div>
            <div class="detail-content">
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
            product: null,
            modalBoolean: false
        }
    },
    methods: {
        getDetails() {
            let stripe_product_id = this.$route.params.stripe_product_id
            djangoAPI({
                method: "GET",
                url: `/product/${stripe_product_id}`
            }).then(productDetailsResponse => {
                this.productDetails = productDetailsResponse.data
                for (let i = 0; i < this.productDetails.length; i++) {
                    this.product = this.productDetails[i]
                }
                document.title = this.product.name + " | MechMarketEU"
            })
        }
    },
    created() {
        this.getDetails()
    },
    mounted() {
        window.scrollTo(0, 0)
    }
}
</script>

<style lang="scss" scoped>
$scrollbar-thumb-color: #c2c9d2;
.container {
    padding: 30px
}
.details {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.details-left {
    display: flex;
    flex-direction: column;
    flex-basis: 50%;
    margin-right: 30px;
}
.detail-thumbnail > img {
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}
.detail-images {
    display:flex;
    flex-direction: row;
    overflow: scroll;
    overflow-y: hidden;
}
.detail-images > img {
    height: 100px;
    margin-right: 5px;
}
.details-right {
    flex-basis: 50%;
}
::-webkit-scrollbar {
    widows: 10px;
    height: 10px;
}
::-webkit-scrollbar-thumb {
    border-radius: 5px;
    background: $scrollbar-thumb-color;
}
@media (max-width: 1024px) {
    .details {
        flex-direction: column;
    }
    .details-left {
        margin-right: 0px;
        margin-bottom: 30px;
    }
}
</style>
