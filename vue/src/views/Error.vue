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
            document.title = "Access Blocked | MechMarketEU";
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
