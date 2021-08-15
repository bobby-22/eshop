<template>
<div class="columns is-multiline">
    <div v-for="product in products" :key="product.id" class="column is-one-third">
        <div class="card">
            <div class="card-image">
                <figure class="image">
                    <span>{{ product.thumbnail.url }}</span>
                </figure>
            </div>
            <div class="card-content">
                <div class="content">
                    <span class="title is-4">
                        <router-link v-bind:to="product.stripe_product_id">{{ product.name }}</router-link>
                    </span>
                </div>
                <div class="content">
                    <span class="subtitle">{{ product.price }}€</span>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import { getAPI } from "../axios"
export default {
    name: "Latest",
    data() {
        return {
            products: []
        }
    },
    created() {
        getAPI
            .get('/latest/',)
            .then(response => {this.products = response.data})
    }
}
</script>

<style>
</style>
