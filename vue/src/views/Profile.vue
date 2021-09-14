<template>
    <div class="container">
        <h1 class="title">
            My products
            <router-link id="create" to="/products/create">
                <i class="far fa-plus-square"></i>
            </router-link>
        </h1>
        <p v-if="!products.length">No products added...</p>
        <AccountsProfile
            v-for="product in products"
            v-bind:key="product.id"
            v-bind:product="product"
            v-on:deleteProduct="deleteProduct"
        />
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import { toast } from "bulma-toast";
import AccountsProfile from "../components/AccountsProfile.vue";
export default {
    name: "Profile",
    components: {
        AccountsProfile,
    },
    data() {
        return {
            products: [],
        };
    },
    methods: {
        refreshTokens() {
            let tokenRefresh = this.$store.state.tokenRefresh;
            djangoAPI
                .post("/api/v1/accounts/refresh/", { refresh: tokenRefresh })
                .then((tokensResponse) => {
                    console.log(tokensResponse);
                    this.$store.commit(
                        "saveTokenAccessState",
                        tokensResponse.data.access
                    );
                    this.$store.commit(
                        "saveTokenRefreshState",
                        tokensResponse.data.refresh
                    );
                })
                .catch((error) => {
                    console.log(error);
                    if (error) {
                        this.$store.commit("removeCredentialsState");
                        this.$router.push("/accounts/login");
                    }
                });
        },
        getUserProducts() {
            djangoAPI
                .get(
                    "/api/v1/accounts/profile/" +
                        this.$store.state.currentUserId,
                    {
                        headers: {
                            Authorization: `JWT ${this.$store.state.tokenAccess}`,
                        },
                    }
                )
                .then((profileResponse) => {
                    console.log(profileResponse);
                    this.products = profileResponse.data;
                })
                .catch((error) => {
                    console.log(error);
                    if (error.response.status === 403) {
                        this.$store.commit("removeCredentialsState");
                        this.$router.push({
                            name: "Error",
                            params: {
                                message: "403",
                            },
                        });
                    }
                });
        },
        deleteProduct(product) {
            this.products = this.products.filter((i) => {
                return i.stripe_product_id !== product.stripe_product_id;
            });
            toast({
                message: "Product has been successfully deleted!",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: "bottom-right",
            });
        },
        setTitle() {
            document.title = "My Products | MechMarketEU";
        },
    },
    beforeCreate() {
        this.$store.commit("localStorageSavedTokens");
        this.$store.commit("localStorageSavedCurrentUserId");
    },
    created() {
        this.refreshTokens();
        this.getUserProducts();
        this.setTitle();
    },
    mounted() {
        setInterval(() => {
            this.refreshTokens();
        }, 250000);
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
a#create {
    color: #424242;
}
#create:hover {
    color: black;
}
</style>
