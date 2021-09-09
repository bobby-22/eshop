<template>
    <div class="container">
        <div
            class="details"
            v-for="detail in details.slice(0, 1)"
            :key="detail.id"
        >
            <div class="details-left">
                <div class="detail-thumbnail">
                    <img v-bind:src="detail.thumbnail" />
                </div>
                <div class="detail-images">
                    <div
                        class="images"
                        v-for="image in details.slice(1, this.details.length)"
                        :key="image.id"
                    >
                        <img id="image" v-bind:src="image.images" />
                    </div>
                </div>
            </div>

            <div class="details-right">
                <div class="detail-header">
                    <h1 class="title" id="title">{{ detail.title }}</h1>
                    <div class="detail-header-top">
                        <h2 class="title is-5">
                            <i class="fas fa-euro-sign"></i>
                            {{ detail.price }}
                        </h2>
                        <h2 class="title is-5">
                            <i class="fas fa-map-marker-alt"></i>
                            {{ detail.country }}
                        </h2>
                    </div>
                    <div class="detail-header-bottom">
                        <h2 class="title is-6">
                            <i class="fas fa-calendar-alt"></i>
                            {{ detail.date }}
                        </h2>
                        <h2 class="title is-6">
                            <i class="fas fa-user"></i>
                            {{ detail.user }}
                        </h2>
                    </div>
                </div>
                <div class="detail-body">
                    <p>{{ detail.description }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
export default {
    name: "Details",
    data() {
        return {
            details: [],
            product: null,
            modalBoolean: false,
        };
    },
    methods: {
        getDetails() {
            let stripe_product_id = this.$route.params.stripe_product_id;
            djangoAPI({
                method: "GET",
                url: `/product/${stripe_product_id}`,
            })
                .then((detailsResponse) => {
                    console.log(detailsResponse);
                    this.details = detailsResponse.data;
                    for (let i = 0; i < this.details.slice(0, 1).length; i++) {
                        this.product = this.details[i];
                    }
                    document.title = this.product.title;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    created() {
        this.getDetails();
    },
};
</script>

<style scoped>
.container {
    min-height: 100%;
    width: 100%;
    padding: 30px;
}
.details {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.details-left {
    display: flex;
    flex-direction: column;
    flex-basis: 50%;
    margin-right: 30px;
}
.detail-thumbnail > img {
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}
.detail-images {
    display: flex;
    flex-direction: row;
    overflow: scroll;
    overflow-y: hidden;
    column-gap: 5px;
}
#image {
    height: 100px;
}
.details-right {
    flex-basis: 50%;
}
#title {
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 15px;
    margin-bottom: 15px;
}
.detail-header-top {
    display: flex;
    justify-content: space-between;
}
.detail-header-bottom {
    display: flex;
    justify-content: space-between;
    margin-top: -15px;
    margin-bottom: 24px;
}
.title.is-6 {
    margin-bottom: 0px;
}
.detail-body {
    overflow-wrap: break-word;
}
::-webkit-scrollbar {
    widows: 10px;
    height: 10px;
}
::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background: #c2c9d2;
}
@media (max-width: 1024px) {
    .details {
        flex-direction: column;
    }
    .details-left {
        margin-right: 0px;
        margin-bottom: 15px;
    }
}
</style>
