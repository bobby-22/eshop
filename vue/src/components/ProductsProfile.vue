<template>
    <div class="card">
        <div class="card-image">
            <img v-bind:src="product.thumbnail" />
        </div>

        <div class="card-content">
            <div class="content" id="title">
                <span class="title is-4">
                    <router-link
                        v-bind:to="{
                            name: 'Details',
                            params: {
                                stripe_product_id: product.stripe_product_id,
                            },
                        }"
                        v-on:click="getProductData"
                    >
                        {{ product.title }}
                    </router-link>
                    <span class="actions">
                        <router-link
                            class="fas fa-edit"
                            id="update"
                            v-on:click="getProductData(product)"
                            v-bind:to="{
                                name: 'ProductsUpdate',
                                params: {
                                    stripe_product_id:
                                        product.stripe_product_id,
                                },
                            }"
                        ></router-link>
                        <a
                            class="fas fa-trash-alt"
                            id="delete"
                            v-on:click="deleteProduct"
                        ></a>
                    </span>
                </span>
            </div>
            <div class="content" id="content-bottom">
                <div class="split">
                    <span class="subtitle">
                        <i class="fas fa-euro-sign"></i>
                        <span>{{ product.price }}</span>
                    </span>
                    <span class="subtitle">
                        <i class="fas fa-calendar-alt"></i>
                        <span>{{ product.date }}</span>
                    </span>
                </div>
                <div class="description">{{ product.description }}</div>
            </div>
        </div>
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
export default {
    name: "ProductsProfile",
    props: {
        product: Object,
    },
    data() {
        return {
            images: [],
        };
    },
    methods: {
        deleteProduct() {
            djangoAPI
                .delete(
                    `/api/v1/products/${this.product.stripe_product_id}/delete/`
                )
                .then((deletedProductResponse) => {
                    console.log(deletedProductResponse);
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$emit("deleteProduct", this.product);
        },
        getImages() {
            let stripe_product_id = this.product.stripe_product_id;
            djangoAPI({
                method: "GET",
                url: `/api/v1/products/${stripe_product_id}/images/`,
            })
                .then((imagesResponse) => {
                    console.log(imagesResponse);
                    this.images = imagesResponse.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        getProductData(product) {
            this.$store.commit("saveProductDataState", product);
            this.$store.commit("saveImagesCloudState", this.images);
        },
    },
    created() {
        this.getImages();
    },
};
</script>

<style scoped>
.card {
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 5px 0px,
        rgba(0, 0, 0, 0.1) 0px 0px 1px 0px;
    display: flex;
    height: 250px;
    justify-content: space-between;
    margin-bottom: 16px;
}
.card-image {
    display: flex;
    flex-basis: 30%;
}
.card-image > img {
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 0px;
    height: 250px;
    width: 1000px;
    object-fit: cover;
}
.card-content {
    display: flex;
    flex-direction: column;
    flex-basis: 70%;
    padding: 15px;
}
#title {
    margin-bottom: 15px;
}
.title {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.actions {
    white-space: nowrap;
}
#update,
#delete {
    color: #424242;
    margin-left: 15px;
    margin-right: 0px;
}
#delete:hover {
    color: black;
}
#content-bottom {
    border-top: 1px solid #f0f0f0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.split {
    display: flex;
    justify-content: space-between;
    margin-top: 5px;
}
#country {
    margin-left: 15px;
}
.fas {
    margin-right: 5px;
}
.description {
    white-space: pre-line;
}
@media (max-width: 769px) {
    .card {
        flex-direction: column;
        height: auto;
    }
    .card-image > img {
        height: 100%;
        border-bottom-right-radius: 0px;
        border-bottom-left-radius: 0px;
        border-top-right-radius: 5px;
    }
    .split {
        flex-direction: row;
    }
}
</style>
