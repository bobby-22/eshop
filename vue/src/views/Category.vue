<template>
<div class="columns is-multiline">
    <Content
        v-for="product in products"
        v-bind:key="product.id"
        v-bind:product="product"
    />
</div>
</template>

<script>
import { djangoAPI } from "../axios"
import Content from '../components/Content.vue'
export default {
  components: { Content },
    name: "Category",
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
            })
        },
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
.columns.is-multiline {
    padding: 30px;
}
</style>
