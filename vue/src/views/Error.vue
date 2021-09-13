<template>
    <div class="container">
        <h1 class="title">Error</h1>
        <p>{{ errorMessage }}</p>
    </div>
</template>

<script>
export default {
    name: "Latest",
    data() {
        return {
            errorMessage: null,
        };
    },
    methods: {
        setTitle() {
            if ((this.$router.params = "403")) {
                document.title = `Unauthorized | MechMarketEU`;
                this.errorMessage =
                    "You are not authorized to perform this action!";
            }
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
