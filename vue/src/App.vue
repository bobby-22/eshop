<template>
    <div class="container">
        <Navbar />
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

<style>
html {
    background-color: #f5f5f5
}
</style>
