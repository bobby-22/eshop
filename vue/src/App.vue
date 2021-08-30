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
            let tokenRefresh = JSON.parse(localStorage.getItem("tokenRefresh"));
            djangoAPI
                .post("/accounts/refresh/", { refresh: tokenRefresh })
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
                });
        },
    },
    mounted() {
        setInterval(() => {
            this.refreshToken();
        }, 50000);
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
.title {
    color: black;
}
::selection {
    background-color: #fbe38b;
}
</style>
