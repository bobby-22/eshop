<template>
<div class="columns is-multiline">
    <div v-for="product in latestProducts" :key="product.id" class="column is-one-quarter-desktop is-one-third-tablet">
        <div class="card">
            <div class="card-image">
                <router-link :to="{name: 'ProductDetails', params: { stripe_product_id: product.stripe_product_id }}">
                    <img v-bind:src="'http://localhost:8000' + product.thumbnail">
                </router-link>
                <a v-on:click="addToWish" class="far fa-bookmark"></a>
            </div>

            <div class="card-content">
                <div class="content">
                    <span class="title is-5">
                        <router-link :to="{name: 'ProductDetails', params: { stripe_product_id: product.stripe_product_id }}">
                            {{ product.name }}
                        </router-link>
                    </span>
                </div>
                <div class="content" id="content-bottom">
                    <div class="split">
                        <span class="subtitle">
                            <i class="fas fa-euro-sign"></i>
                            <span>{{ product.price }}</span>
                        </span>
                        <span class="subtitle">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>{{ product.location }}</span>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import { djangoAPI } from "../axios"
import { toast } from "bulma-toast"
export default {
    name: "LatestProducts",
    data() {
        return {
            latestProducts: null
        }
    },
    methods: {
        getProducts() {
            djangoAPI
                .get('/latest-products/')
                .then(latestProductsResponse => {
                    this.latestProducts = latestProductsResponse.data
                })
        },
        addToWish() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }
            const item = {
                product: this.latestProducts,
                quantity: this.quantity
            }
            this.$store.commit("addToWish", item)
            toast({
                message: "This product was added to your wishlist!",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: "bottom-right"
            })
        }
    },
    created() {
        document.title = "Latest Products | MechMarketEU",
        this.getProducts()
    }
}
</script>

<style lang="scss" scoped>
$bookmark-color: #616161;
$content-bottom-border-top-color: #f0f0f0;
$link-blue: dodgerblue;
$link-orange: darksalmon;
.columns.is-multiline {
    padding: 30px;
}
.column.is-one-quarter-desktop.is-one-third-tablet.is-half-mobile {
    padding: 8px;
}
.card {
    box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
}
.far.fa-bookmark {
    position: absolute;
    right: 0;
    font-size: 25px;
    color: $bookmark-color;
    margin: 5px;
}
.card-content {
    padding: 15px;
}
.content {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin: 0px 0px 10px;
}
#content-bottom {
    border-top: 1px solid $content-bottom-border-top-color;
}
.split {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0px;
    margin-top: 5px;
    padding-bottom: 0px;
}
.subtitle {
    -webkit-text-size-adjust: none;
    align-items: baseline;
    margin-bottom: 0px;
}
.fas {
    margin-right: 5px;
}
a:link, a:visited {
    color: $link-blue;
 }
a:active, a:hover {
    color: $link-orange;
}
img {
    position: relative;
    height: 200px;
    width: 800px;
    object-fit: cover;
}
@media (max-width: 769px) {
    img {
        height: 100%;
    }
}
</style>
