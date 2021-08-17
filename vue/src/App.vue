<template>
    <div class="container">
        <Navbar />
        <transition name="animation">
            <router-view/>
        </transition>
    </div>
</template>

<script>
import Navbar from "./components/Navbar"

export default {
    name: "App",
    components: {
        Navbar
    },
}
</script>

<style lang="scss">
@import "../node_modules/bulma";

</style>
