<template>
<div class="columns is-multiline" >
    <div class="column is-12">
        <h1 class="title">Bookmark</h1>
    </div>
    <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="wishLength">
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total</th>
                    <th></th>
                </tr>
            </thead>

            <tbody>
                <BookmarkItem
                    v-for="item in wish.items"
                    v-bind:key="item.product.id"
                    v-bind:initialItem="item"
                />
            </tbody>
        </table>
    </div>
</div>
</template>

<script>
export default {
    name: "Bookmark",
}
</script>

<style>
.columns.is-multiline {
    padding: 30px;
}
</style>