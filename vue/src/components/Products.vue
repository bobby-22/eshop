<template>
    <div class="column is-one-third-desktop is-half-tablet">
        <div class="card" v-if="savedProducts">
            <div class="card-image" style="border-radius: 10px">
                <router-link
                    v-bind:to="{
                        name: 'Details',
                        params: {
                            post_id: product.post_id,
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
                <div class="content" id="content-title">
                    <span class="title is-5">
                        <router-link
                            :to="{
                                name: 'Details',
                                params: {
                                    post_id: product.post_id,
                                },
                            }"
                        >
                            {{ product.title }}
                        </router-link>
                    </span>
                </div>
                <div class="content" id="content-bottom">
                    <div class="split">
                        <span class="subtitle">
                            <i class="fas fa-euro-sign"></i>
                            <span>{{ product.price }}</span>
                        </span>
                        <span class="subtitle" id="country">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>{{ product.country }}</span>
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
            savedProducts: this.$store.state.savedProducts,
            keyword: null,
            savedBoolean: false,
            checkSavedBoolean: false,
        };
    },
    methods: {
        saveProduct() {
            this.savedBoolean = !this.savedBoolean;
            this.$store.commit("saveProductState", this.product);
            toast({
                message: "Post has been saved!",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: "bottom-right",
            });
        },
        unsaveProduct() {
            this.savedBoolean = !this.savedBoolean;
            this.savedProducts = this.savedProducts.filter((i) => {
                return i.post_id !== this.product.post_id;
            });
            this.$store.commit("updateSavedProductsState", this.product);
            toast({
                message: "Post has been unsaved!",
                type: "is-danger",
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: "bottom-right",
            });
        },
        checkBookmark() {
            let array = JSON.parse(localStorage.getItem("savedProducts"));
            let checkSavedBoolean = JSON.stringify(array).includes(
                this.product.post_id
            );
            this.checkSavedBoolean = !checkSavedBoolean;
        },
    },
    beforeCreate() {
        this.$store.commit("localStorageSavedProducts");
    },
    created() {
        this.checkBookmark();
    },
};
</script>

<style scoped>
.card {
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
}
.bookmark {
    position: absolute;
    top: 0;
    right: 0;
}
.far.fa-bookmark {
    border-radius: 7px;
    opacity: 0.3;
    background: #fafafa;
    transition: opacity 0.5s;
    font-size: 25px;
    color: #616161;
    padding: 6px;
    margin: 10px;
}
.far.fa-bookmark:hover {
    color: black;
    opacity: 0.7;
}
.card-content {
    padding: 15px;
}
.content {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin: 0px 0px 15px;
}
#content-bottom {
    border-top: 1px solid #f0f0f0;
    margin: 0px;
}
.split {
    display: flex;
    justify-content: space-between;
    margin-top: 5px;
    padding-bottom: 1px;
}
.subtitle {
    -webkit-text-size-adjust: none;
    margin-bottom: 0px;
}
#country {
    white-space: nowrap;
    text-overflow: ellipsis;
    margin-left: 15px;
}
.fas {
    margin-right: 5px;
}
.card-image {
    height: 200px;
}
img {
    position: relative;
    height: 200px;
    width: 800px;
    object-fit: cover;
}
@media (min-width: 1024px) and (max-width: 1215px) {
    #country {
        overflow: hidden;
    }
}
@media (max-width: 769px) {
    img {
        min-height: 100%;
    }
    #content-title {
        overflow: visible;
        white-space: pre-line;
    }
    #country {
        overflow: hidden;
    }
}
</style>
