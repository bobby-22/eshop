<template>
<div class="container">
    <div class="columns is-multiline">
        <Content
            v-for="product in products"
            v-bind:key="product.id"
            v-bind:product="product"
        />
    </div>
</div>
</template>

<script>
import { djangoAPI } from "../axios"
import Content from '../components/Content.vue'
export default {
    name: "Category",
    components: {
        Content
    },
    data() {
        return {
            products: null
        }
    },
    methods: {
        getProducts() {
            let category_id = this.$route.params.category_id
            djangoAPI({
                method: "GET",
                url: `/category/${category_id}`
            }).then(categoryResponse => {
                this.products = categoryResponse.data
                console.log(this.products)
            })
        }
    },
    created() {
        document.title = "Category | MechMarketEU",
        this.getProducts()
    },
    watch: {
        $route(to, from) {
            if(to.name === "Category") {
                this.getProducts()
            }
        }
    }
}
</script>

<style scoped>
.container {
    min-height: 100%;
    padding: 30px;
}
</style>
