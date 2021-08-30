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
                        {{ item.product.name }}
                    </router-link>
                    <a
                        class="far fa-trash-alt"
                        v-on:click="unsaveProduct(item)"
                    ></a>
                </span>
            </div>
            <div class="content" id="content-bottom">
                <div class="split">
                    <span class="subtitle">
                        <i class="fas fa-euro-sign"></i>
                        <span>{{ item.product.price }}</span>
                    </span>
                    <span class="subtitle">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>{{ item.product.location }}</span>
                    </span>
                </div>
                <span>{{ item.product.description }}</span>
            </div>
        </div>
    </div>
</template>

<script>
import { toast } from "bulma-toast";
export default {
    name: "ContentSaved",
    props: {
        initialItem: Object,
    },
    data() {
        return {
            item: this.initialItem,
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

<style lang="scss" scoped>
$content-bottom-border-top-color: #f0f0f0;
$link-blue: dodgerblue;
$link-orange: darksalmon;
$link-grey: #363636;
$link-red: #f14668;
.card {
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
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
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
a {
    color: $link-grey;
}
.far.fa-trash-alt:active,
.far.fa-trash-alt:hover {
    color: $link-red;
}
a:link,
a:visited {
    color: $link-blue;
}
a:active,
a:hover {
    color: $link-orange;
}
#content-bottom {
    border-top: 1px solid $content-bottom-border-top-color;
}
.split {
    display: flex;
    justify-content: space-between;
    margin-top: 5px;
}
.fas {
    margin-right: 5px;
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
}
</style>
