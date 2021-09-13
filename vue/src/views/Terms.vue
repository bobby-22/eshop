<template>
    <div class="container">
        <h1 class="title">Terms and Conditions</h1>
        <p>Terms</p>
    </div>
</template>

<script>
export default {
    name: "Terms",
    methods: {
        setTitle() {
            document.title = "Terms and Conditions | MechMarketEU";
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
