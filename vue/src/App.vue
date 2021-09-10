<template>
    <div class="container">
        <Navbar />
        <router-view />
        <Footer />
    </div>
</template>

<script>
import Navbar from "./components/Navbar";
import Footer from "./components/Footer.vue";
import { djangoAPI } from "./axios";

export default {
    name: "App",
    components: {
        Navbar,
        Footer,
    },
    methods: {
        refreshToken() {
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
    },
    beforeCreate() {
        this.$store.commit("localStorageSavedTokens");
    },
    created() {
        this.refreshToken();
    },
    mounted() {
        setInterval(() => {
            this.refreshToken();
        }, 250000);
    },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";
.container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}
::selection {
    background-color: #fbe38b;
}
a:link,
a:visited {
    color: dodgerblue;
}
a:active,
a:hover {
    color: darksalmon;
}
</style>
