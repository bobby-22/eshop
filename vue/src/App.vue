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

export default {
    name: "App",
    components: {
        Navbar,
        Footer,
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
