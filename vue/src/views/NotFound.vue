<template>
    <div class="container">
        <h1 class="title">Page not found</h1>
        <p>Are you sure you entered the right path?</p>
    </div>
</template>

<script>
export default {
    name: "NotFound",
    methods: {
        setTitle() {
            document.title = "Page Not Found | MechMarketEU";
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
    width: 100%;
    padding: 30px;
}
.title {
    border-bottom: 1px solid #ededed;
    padding-bottom: 15px;
    margin-bottom: 20px;
}
</style>
