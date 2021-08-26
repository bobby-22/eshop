<template>
<div class="column is-one-quarter-desktop is-one-third-tablet">
    <div class="card" v-if="bookmark.items">
        <div class="card-image">
            <router-link :to="{name: 'Details', params: { stripe_product_id: product.stripe_product_id }}">
                <img v-bind:src="product.thumbnail">
            </router-link>
            <div class="bookmark" v-if="checkBookmarkBoolean">
                <a class="far fa-bookmark" v-on:click="addToBookmark" v-bind:class="[{'fas fa-bookmark': savedBoolean}]"></a>
            </div>
        </div>

        <div class="card-content">
            <div class="content">
                <span class="title is-5">
                    <router-link :to="{name: 'Details', params: { stripe_product_id: product.stripe_product_id }}">
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
</template>

<script>
import { toast } from "bulma-toast"
export default {
    name: "Content",
    props: {
        product: Object
    },
    data() {
        return {
            savedBoolean: false,
            checkBookmarkBoolean: false,
            keyword: null,
            bookmark: {
                items: []
            },
        }
    },
    methods: {
        addToBookmark() {
            this.savedBoolean = !this.savedBoolean
            let item = {
                product: this.product,
            }
            this.$store.commit("addToBookmark", item)
            toast({
                message: "Item has been added to bookmark!",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: "bottom-right"
            })
        },
        checkBookmark() {
            let array = JSON.parse(localStorage.getItem("bookmark"))
            let checkBookmarkBoolean = JSON.stringify(array.items).includes(this.product.stripe_product_id)
            this.checkBookmarkBoolean = !checkBookmarkBoolean
        }
    },
    mounted() {
        this.bookmark = this.$store.state.bookmark
        this.checkBookmark()
    }
}
</script>

<style lang="scss" scoped>
$bookmark-color: #616161;
$content-bottom-border-top-color: #f0f0f0;
$link-blue: dodgerblue;
$link-orange: darksalmon;
.column.is-one-quarter-desktop.is-one-third-tablet {
    padding: 8px;
}
.card {
    box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
}
.bookmark {
    position:absolute;
    top: 0;
    right: 0;
}
.bookmark:hover {
    text-shadow: 0px 0px 30px rgba(50, 50, 50, 1)
}
.far.fa-bookmark {
    font-size: 30px;
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
    margin: 0px;
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
