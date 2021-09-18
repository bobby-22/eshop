<template>
    <div class="container">
        <h1 class="title">
            Searched keyword: "{{ keyword }}" ({{ count }} results)
        </h1>
        <div class="columns is-multiline is-variable is-2" id="columns">
            <Products
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product"
                v-bind:src="product.thumbnail"
            />
        </div>
        <nav class="pagination" role="navigation">
            <a
                class="pagination-previous"
                v-if="!(currentPage == 1)"
                v-on:click="selectPage(currentPage - 1)"
                >Previous</a
            >
            <a
                class="pagination-next"
                v-on:click="selectPage(currentPage + 1)"
                v-if="!(currentPage == lastPage)"
                >Next page</a
            >
            <ul class="pagination-list" v-if="lastPage > 5">
                <li v-if="currentPage < 5">
                    <a
                        class="pagination-link"
                        v-for="page in 5"
                        :key="page.id"
                        v-bind:class="{
                            'is-current': page == currentPage,
                        }"
                        v-on:click="selectPage(page)"
                        >{{ page }}</a
                    >
                    <span class="pagination-ellipsis">&hellip;</span>
                    <a
                        class="pagination-link"
                        v-bind:class="{
                            'is-current': lastPage == currentPage,
                        }"
                        v-on:click="selectPage(lastPage)"
                        >{{ lastPage }}</a
                    >
                </li>
                <li v-else-if="currentPage < lastPage - 3">
                    <a class="pagination-link" v-on:click="selectPage(1)">{{
                        1
                    }}</a>
                    <span class="pagination-ellipsis">&hellip;</span>
                    <a
                        class="pagination-link"
                        v-on:click="selectPage(previousPage)"
                        >{{ previousPage }}</a
                    >
                    <a
                        class="pagination-link"
                        v-bind:class="{
                            'is-current': currentPage,
                        }"
                        v-on:click="selectPage(currentPage)"
                        >{{ currentPage }}</a
                    >
                    <a
                        class="pagination-link"
                        v-on:click="selectPage(nextPage)"
                        >{{ nextPage }}</a
                    >
                    <span class="pagination-ellipsis">&hellip;</span>
                    <a
                        class="pagination-link"
                        v-bind:class="{
                            'is-current': lastPage == currentPage,
                        }"
                        v-on:click="selectPage(lastPage)"
                        >{{ lastPage }}</a
                    >
                </li>
                <li v-else-if="currentPage > lastPage - 4">
                    <a class="pagination-link" v-on:click="selectPage(1)">{{
                        1
                    }}</a>
                    <span class="pagination-ellipsis">&hellip;</span>
                    <a
                        class="pagination-link"
                        v-for="index in 5"
                        v-bind:key="index.id"
                        v-bind:class="{
                            'is-current': lastPage - 5 + index == currentPage,
                        }"
                        v-on:click="selectPage(lastPage - 5 + index)"
                        >{{ lastPage - 5 + index }}</a
                    >
                </li>
            </ul>
            <ul class="pagination-list" v-else>
                <li>
                    <a
                        class="pagination-link"
                        v-for="page in lastPage"
                        :key="page.id"
                        v-bind:class="{
                            'is-current': page == currentPage,
                        }"
                        v-on:click="selectPage(page)"
                        >{{ page }}</a
                    >
                </li>
            </ul>
        </nav>
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import Products from "../components/Products.vue";
export default {
    name: "Search",
    components: {
        Products,
    },
    data() {
        return {
            products: [],
            keyword: null,
            count: null,
            lastPage: null,
            currentPage: null,
            nextPage: null,
            previousPage: null,
        };
    },
    methods: {
        getSearchProducts() {
            djangoAPI({
                method: "GET",
                url: `/api/v1/search/?page=${this.$route.params.page}&search=${this.$route.params.keyword}`,
            })
                .then((searchResponse) => {
                    console.log(searchResponse);
                    this.products = searchResponse.data.results;
                    this.count = searchResponse.data.count;
                    this.lastPage = Math.ceil(searchResponse.data.count / 21);
                    this.currentPage = Number(this.$route.params.page);
                    this.nextPage = Number(this.$route.params.page) + 1;
                    this.previousPage = Number(this.$route.params.page) - 1;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        selectPage(page) {
            djangoAPI
                .get(
                    `/api/v1/search/?page=${this.$route.params.page}&search=${this.$route.params.keyword}`
                )
                .then((getPageResponse) => {
                    console.log(getPageResponse);
                    this.$router.replace({ params: { page: page } });
                    window.scrollTo(0, 0);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        getKeyword() {
            return (this.keyword = this.$route.params.keyword);
        },
        setTitle() {
            document.title = `${this.$route.params.keyword} - Page ${this.$route.params.page} | MechMarketEU`;
        },
    },
    created() {
        this.getSearchProducts();
        this.getKeyword();
        this.setTitle();
    },
    watch: {
        $route(to, from) {
            if (to.name === "Search") {
                this.getSearchProducts();
                this.getKeyword();
                this.setTitle();
            }
        },
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
    margin-bottom: 8px;
}
</style>
