<template>
    <div class="column is-one-quarter-desktop is-one-third-tablet">
        <div class="card" v-if="savedProducts.items">
            <div class="card-image" style="border-radius: 10px">
                <router-link
                    v-bind:to="{
                        name: 'Details',
                        params: {
                            stripe_product_id: product.stripe_product_id,
                        },
                    }"
                >
                    <img
                        style="
                            border-top-right-radius: 10px;
                            border-top-left-radius: 10px;
                        "
                        v-bind:src="product.thumbnail"
                    />
                </router-link>
                <div class="bookmark" v-if="checkSavedBoolean">
                    <div class="bookmark" v-if="savedBoolean">
                        <a
                            class="fas fa-bookmark"
                            v-on:click="unsaveProduct"
                            v-bind:class="[{ 'far fa-bookmark': savedBoolean }]"
                        ></a>
                    </div>
                    <div class="notSaved" v-else>
                        <a
                            class="far fa-bookmark"
                            v-on:click="saveProduct"
                            v-bind:class="[{ 'fas fa-bookmark': savedBoolean }]"
                        ></a>
                    </div>
                </div>
            </div>

            <div class="card-content">
                <div class="content">
                    <span class="title is-5">
                        <router-link
                            :to="{
                                name: 'Details',
                                params: {
                                    stripe_product_id:
                                        product.stripe_product_id,
                                },
                            }"
                        >
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
import { toast } from "bulma-toast";
export default {
    name: "Products",
    props: {
        product: Object,
    },
    data() {
        return {
            savedBoolean: false,
            checkSavedBoolean: false,
            keyword: null,
            savedProducts: {
                items: [],
            },
        };
    },
    methods: {
        saveProduct() {
            this.savedBoolean = !this.savedBoolean;
            let item = {
                product: this.product,
            };
            this.$store.commit("saveProductState", item);
            toast({
                message: "Item has been saved!",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: "bottom-right",
            });
        },
        updateSavedProducts() {
            localStorage.setItem(
                "savedProducts",
                JSON.stringify(this.$store.state.savedProducts)
            );
        },
        unsaveProduct() {
            this.savedBoolean = !this.savedBoolean;
            let item = {
                product: this.product,
            };
            this.savedProducts.items = this.savedProducts.items.filter((i) => {
                return (
                    i.product.stripe_product_id !==
                    item.product.stripe_product_id
                );
            });
            toast({
                message: "Item has been unsaved!",
                type: "is-danger",
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: "bottom-right",
            });
            this.updateSavedProducts();
        },
        checkBookmark() {
            let array = JSON.parse(localStorage.getItem("savedProducts"));
            let checkSavedBoolean = JSON.stringify(array.items).includes(
                this.product.stripe_product_id
            );
            this.checkSavedBoolean = !checkSavedBoolean;
        },
    },
    created() {
        this.savedProducts = this.$store.state.savedProducts;
        this.checkBookmark();
    },
};
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
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
}
.bookmark {
    position: absolute;
    top: 0;
    right: 0;
}
.bookmark:hover {
    text-shadow: 0px 0px 30px rgba(50, 50, 50, 1);
}
.far.fa-bookmark {
    border-radius: 5px;
    opacity: 0.3;
    background: white;
    font-size: 25px;
    color: $bookmark-color;
    padding: 5px;
    margin: 10px;
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
a:link,
a:visited {
    color: $link-blue;
}
a:active,
a:hover {
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
