<template>
    <div class="container">
        <h1 class="title">Home page</h1>
    </div>
</template>

<script>
export default {
    name: "Home",
    methods: {
        setTitle() {
            document.title = "Home Page | MechMarketEU";
        },
    },
    created() {
        this.setTitle();
    },
};
</script>

<style scoped>
.container {
    min-height: 100%;
    padding: 30px;
}
</style>
