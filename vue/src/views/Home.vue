<template>
<div class="container">
    <h1 class="title">Home page</h1>
</div>
</template>

<script>
export default {
  name: "Home",
  created() {
      document.title = "Home Page | MechMarketEU"
  }
}
</script>

<style scoped>
.container {
    min-height: 100%;
    padding: 30px;
}
</style>
