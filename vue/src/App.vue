<template>
    <div class="container">
        <Navbar />
        <router-view/>
        <Footer />
    </div>
</template>

<script>
import Navbar from "./components/Navbar"
import Footer from "./components/Footer.vue"

export default {
    name: "App",
    components: {
        Navbar,
        Footer
    }
}
</script>

<style lang="scss">
@import "../node_modules/bulma";
.container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100vh;
}
@media (max-width: 1024px) {
    .container {
        height: 100%;
    }
}
</style>
