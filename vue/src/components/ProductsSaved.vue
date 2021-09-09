<template>
    <div class="card">
        <div class="card-image">
            <img v-bind:src="item.product.thumbnail" />
        </div>

        <div class="card-content">
            <div class="content" id="title">
                <span class="title is-4">
                    <router-link
                        :to="{
                            name: 'Details',
                            params: {
                                stripe_product_id:
                                    item.product.stripe_product_id,
                            },
                        }"
                    >
                        {{ item.product.title }}
                    </router-link>
                    <a
                        id="unsave"
                        class="fas fa-bookmark"
                        v-on:click="unsaveProduct(item)"
                    ></a>
                </span>
            </div>
            <div class="content" id="content-bottom">
                <div class="split">
                    <span class="subtitle" id="price-country">
                        <div class="price">
                            <i class="fas fa-euro-sign"></i>
                            <span>{{ item.product.price }}</span>
                        </div>
                        <div class="country">
                            <i class="fas fa-calendar-alt" id="date"></i>
                            <span>{{ item.product.date }}</span>
                        </div>
                    </span>
                    <span class="subtitle">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>{{ item.product.country }}</span>
                    </span>
                </div>
                <span class="description">{{ item.product.description }}</span>
            </div>
        </div>
    </div>
</template>

<script>
import { toast } from "bulma-toast";
export default {
    name: "ProductsSaved",
    props: {
        item: Object,
    },
    data() {
        return {
            item: this.item,
        };
    },
    methods: {
        unsaveProduct(item) {
            this.$emit("unsaveProduct", item);
            toast({
                message: "Item has been unsaved!",
                type: "is-danger",
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: "bottom-right",
            });
        },
    },
};
</script>

<style scoped>
.card {
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 5px 0px,
        rgba(0, 0, 0, 0.1) 0px 0px 1px 0px;
    display: flex;
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
a#unsave {
    color: #424242;
    margin-left: 15px;
}
#content-bottom {
    border-top: 1px solid #f0f0f0;
}
.split {
    display: flex;
    justify-content: space-between;
    margin-top: 5px;
}
#price-country {
    display: flex;
}
#date {
    margin-left: 15px;
}
#unsave {
    margin-right: 0px;
}
#unsave:hover {
    color: black;
}
.fas {
    margin-right: 5px;
}
.description {
    overflow-wrap: break-word;
}
@media (max-width: 769px) {
    .card {
        flex-direction: column;
    }
    .card-image > img {
        height: 100%;
        border-bottom-right-radius: 0px;
        border-bottom-left-radius: 0px;
        border-top-right-radius: 5px;
    }
    .split {
        flex-direction: column;
        margin-bottom: 22px;
    }
    #price-country {
        justify-content: space-between;
        margin-bottom: 5px;
    }
}
</style>
