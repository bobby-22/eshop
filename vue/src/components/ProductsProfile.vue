<template>
    <div class="card">
        <div class="card-image">
            <img v-bind:src="product.thumbnail" />
        </div>

        <div class="card-content">
            <div class="content" id="title">
                <span class="title is-4">
                    <router-link
                        :to="{
                            name: 'Details',
                            params: {
                                stripe_product_id: product.stripe_product_id,
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
                        <span id="price">{{ product.price }}</span>
                        <i class="fas fa-map-marker-alt"></i>
                        <span>{{ product.location }}</span>
                    </span>
                    <span class="subtitle">
                        <i class="fas fa-calendar-alt"></i>
                        <span>{{ product.date }}</span>
                    </span>
                </div>
                <span>{{ product.description }}</span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ProductsProfile",
    props: {
        product: Object,
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
#price {
    margin-right: 15px;
}
a {
    color: $link-grey;
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
