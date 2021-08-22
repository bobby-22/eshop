<template>
<div class="columns is-multiline">
    <Content
        v-for="product in products"
        v-bind:key="product.id"
        v-bind:product="product"
        v-bind:src="product.thumbnail"
    />
</div>
</template>

<script>
import { djangoAPI } from "../axios"
import Content from "../components/Content.vue"
export default {
    name: "Search",
    components: { Content },
    data() {
        return {
            products: null
        }
    },
    methods: {
        getProducts() {
            let keyword = this.$route.params.keyword
            djangoAPI({
                method: "GET",
                url: `/?search=${keyword}`
            }).then(searchResponse => {
                this.products = searchResponse.data
                console.log(this.products)
            })
        },
        getTitle() {
            document.title = `${this.$route.params.keyword} | MechMarketEU`
        }
    },
    created() {
        this.getProducts()
        this.getTitle()
    },
    watch: {
        $route(to, from) {
            if(to.name === "Search") {
                this.getProducts()
                this.getTitle()
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
