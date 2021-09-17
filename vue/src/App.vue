<template>
    <div class="container">
        <Navbar />
        <router-view />
        <Footer />
    </div>
</template>

<script>
import { djangoAPI } from "./axios";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer.vue";

export default {
    name: "App",
    components: {
        Navbar,
        Footer,
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
                    if (
                        error.response.status === 403 ||
                        error.response.status === 401
                    ) {
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
        this.refreshTokens();
    },
    mounted() {
        setInterval(() => {
            this.refreshTokens();
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
#columns {
    margin-top: 0px;
    margin-bottom: 0px;
}
.pagination {
    margin-top: 18px;
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
