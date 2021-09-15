<template>
    <div class="container">
        <h1 class="title">{{ username }}'s products</h1>
        <p v-if="!products.length">No products added...</p>
        <AccountsUser
            v-for="product in products"
            v-bind:key="product.id"
            v-bind:product="product"
            v-on:deleteProduct="deleteProduct"
        />
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import AccountsUser from "../components/AccountsUser.vue";
export default {
    name: "User",
    components: {
        AccountsUser,
    },
    data() {
        return {
            products: [],
            username: this.$route.params.user,
        };
    },
    methods: {
        getUserProducts() {
            djangoAPI
                .get("/api/v1/accounts/user/" + this.$route.params.user)
                .then((profileResponse) => {
                    console.log(profileResponse);
                    this.products = profileResponse.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        setTitle() {
            document.title = `${this.$route.params.user}'s Posts | MechMarketEU`;
        },
    },
    created() {
        this.getUserProducts();
        this.setTitle();
    },
};
</script>

<style scoped>
.container {
    min-height: 100%;
    width: 100%;
    padding: 30px;
}
.title {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding-bottom: 15px;
    border-bottom: 1px solid #ededed;
    margin-bottom: 26px;
}
</style>
