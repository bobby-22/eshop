<template>
    <div class="container">
        <h1 class="title" id="main-title">Welcome to MechMarketEU</h1>
        <div class="categories">
            <div class="grid-item">
                <img src="https://d25efl8y6peufe.cloudfront.net/cables.jpg" />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: { category: 'Cables', page: 1 },
                            }"
                            >Cables</router-link
                        >
                    </h1>
                </div>
            </div>
            <div class="grid-item">
                <img src="https://d25efl8y6peufe.cloudfront.net/cases.jpg" />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: { category: 'Cases', page: 1 },
                            }"
                            >Cases</router-link
                        >
                    </h1>
                </div>
            </div>
            <div class="grid-item">
                <img src="https://d25efl8y6peufe.cloudfront.net/deskmats.jpg" />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: { category: 'Deskmats', page: 1 },
                            }"
                            >Deskmats</router-link
                        >
                    </h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://d25efl8y6peufe.cloudfront.net/keyboards.jpg"
                />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: { category: 'Keyboards', page: 1 },
                            }"
                            >Keyboards</router-link
                        >
                    </h1>
                </div>
            </div>
            <div class="grid-item">
                <img src="https://d25efl8y6peufe.cloudfront.net/keycaps.jpg" />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: { category: 'Keycaps', page: 1 },
                            }"
                            >Keycaps</router-link
                        >
                    </h1>
                </div>
            </div>
            <div class="grid-item">
                <img src="https://d25efl8y6peufe.cloudfront.net/others.jpg" />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: { category: 'Others', page: 1 },
                            }"
                            >Others</router-link
                        >
                    </h1>
                </div>
            </div>
            <div class="grid-item">
                <img src="https://d25efl8y6peufe.cloudfront.net/pcbs.jpg" />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: { category: 'PCBs', page: 1 },
                            }"
                            >PCBs</router-link
                        >
                    </h1>
                </div>
            </div>
            <div class="grid-item">
                <img src="https://d25efl8y6peufe.cloudfront.net/pcbs.jpg" />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: { category: 'Plates', page: 1 },
                            }"
                            >Plates</router-link
                        >
                    </h1>
                </div>
            </div>
            <div class="grid-item">
                <img src="https://d25efl8y6peufe.cloudfront.net/switches.jpg" />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: { category: 'Switches', page: 1 },
                            }"
                            >Switches</router-link
                        >
                    </h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://d25efl8y6peufe.cloudfront.net/travelling-cases.jpg"
                />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: {
                                    category: 'Travelling-cases',
                                    page: 1,
                                },
                            }"
                            >Travelling cases</router-link
                        >
                    </h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://d25efl8y6peufe.cloudfront.net/wrist-rests.jpg"
                />
                <div class="title" id="title">
                    <h1>
                        <router-link
                            v-bind:to="{
                                name: 'Category',
                                params: { category: 'Wrist-rests', page: 1 },
                            }"
                            >Wrist-rests</router-link
                        >
                    </h1>
                </div>
            </div>
        </div>
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
    width: 100%;
    padding: 30px;
}
#main-title {
    border-bottom: 1px solid #ededed;
    padding-bottom: 15px;
    margin-bottom: 20px;
}
.categories {
    display: grid;
    grid-template-columns: auto auto auto;
    grid-gap: 16px;
    row-gap: 24px;
}
.grid-item {
    position: relative;
}
.grid-item,
img {
    height: 300px;
    min-width: 100%;
    box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
    border-radius: 10px;
}
img {
    object-fit: cover;
}
img:hover {
    -o-transition: 0.5s;
    -ms-transition: 0.5s;
    -moz-transition: 0.5s;
    -webkit-transition: 0.5s;
    transition: 0.5s;
    opacity: 0.7;
}
#title {
    position: absolute;
    bottom: 0px;
    min-width: 100%;
    background: rgb(0, 0, 0);
    background: rgba(0, 0, 0, 0.5);
    color: #f2f2f2;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    font-size: 20px;
    padding: 15px;
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.5s, visibility 0.5s;
}
.grid-item:hover #title {
    visibility: visible;
    opacity: 1;
}
a:link,
a:visited,
a:active {
    color: inherit;
    background: inherit;
    font-size: inherit;
    text-decoration: none;
}
@media (max-width: 769px) {
    .categories {
        grid-template-columns: auto;
    }
    .grid-item,
    img {
        min-height: 100%;
        min-width: 100%;
    }
}
@media (max-width: 1024px) {
    img {
        opacity: 0.85;
    }
    #title {
        visibility: visible;
        opacity: 1;
    }
}
</style>
