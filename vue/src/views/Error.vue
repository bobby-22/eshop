<template>
    <div class="container">
        <h1 class="title">Error</h1>
        <p>You are not allowed to perform this action!</p>
    </div>
</template>

<script>
export default {
    name: "Latest",
    methods: {
        setTitle() {
            document.title = "Access blocked | MechMarketEU";
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
    padding-bottom: 15px;
    border-bottom: 1px solid #ededed;
    margin-bottom: 26px;
}
</style>
