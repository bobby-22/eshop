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
                                post_id: product.post_id,
                            },
                        }"
                    >
                        {{ product.title }}
                    </router-link>
                    <span class="actions">
                        <a class="fas fa-bookmark" id="unsave" v-on:click="unsaveProduct()"></a>
                    </span>
                </span>
            </div>
            <div class="content" id="content-bottom">
                <div class="split">
                    <span class="subtitle" id="price-country">
                        <div class="price">
                            <i class="fas fa-euro-sign"></i>
                            <span>{{ product.price }}</span>
                        </div>
                        <div class="country">
                            <i class="fas fa-calendar-alt" id="date"></i>
                            <span>{{ product.date }}</span>
                        </div>
                    </span>
                    <span class="subtitle">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>{{ product.country }}</span>
                    </span>
                </div>
                <span class="description">{{ product.description }}</span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ProductsSaved",
    props: {
        product: Object,
    },
    methods: {
        unsaveProduct() {
            this.$emit("unsaveProduct", this.product);
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
    height: 250px;
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
}
.actions {
    white-space: nowrap;
}
#unsave {
    color: #424242;
    margin-left: 15px;
    margin-right: 0px;
}
#unsave:hover {
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
#price-country {
    display: flex;
}
#date {
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
        flex-direction: column;
        margin-bottom: 22px;
    }
    #price-country {
        justify-content: space-between;
        margin-bottom: 5px;
    }
}
</style>
