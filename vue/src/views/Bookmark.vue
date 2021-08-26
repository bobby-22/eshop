<template>
<div class="container">
    <h1 class="title">Bookmarked products:</h1>
    <ContentBookmark
        v-for="item in bookmark.items"
        v-bind:key="item.product.id"
        v-bind:initialItem="item"
        v-on:removeBookmark="removeBookmark"
    />
</div>
</template>

<script>
import ContentBookmark from "../components/ContentBookmark"
export default {
    name: "Bookmark",
    components: {
        ContentBookmark
    },
    data() {
        return {
            bookmark: {
                items: []
            }
        }
    },
    methods: {
        updateBookmark() {
            localStorage.setItem("bookmark", JSON.stringify(this.$store.state.bookmark))
        },
        removeBookmark(item) {
            this.bookmark.items = this.bookmark.items.filter(i => {
                return i.product.stripe_product_id !== item.product.stripe_product_id
            })
            this.updateBookmark()
            this.$router.go(0);
        }
    },
    mounted() {
        this.bookmark = this.$store.state.bookmark
    }
}
</script>

<style scoped>
.container {
    min-height: 100%;
    padding: 30px
}
</style>
