<template>
    <div class="container">
        <h1 class="title" id="main-title">Home page</h1>
        <div class="categories">
            <div class="grid-item">
                <img
                    src="https://mechmarketstockmedia.s3.eu-central-1.amazonaws.com/stock/cables.jpg"
                />
                <div class="title" id="title">
                    <h1>Cables</h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://mechmarketstockmedia.s3.eu-central-1.amazonaws.com/stock/cases.jpg"
                />
                <div class="title" id="title">
                    <h1>Cases</h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://mechmarketstockmedia.s3.eu-central-1.amazonaws.com/stock/deskmats.jpg"
                />
                <div class="title" id="title">
                    <h1>Deskmats</h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://mechmarketstockmedia.s3.eu-central-1.amazonaws.com/stock/keyboards.jpg"
                />
                <div class="title" id="title">
                    <h1>Keyboards</h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://mechmarketstockmedia.s3.eu-central-1.amazonaws.com/stock/keycaps.jpg"
                />
                <div class="title" id="title">
                    <h1>Keycaps</h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://mechmarketstockmedia.s3.eu-central-1.amazonaws.com/stock/others.jpg"
                />
                <div class="title" id="title">
                    <h1>Others</h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://mechmarketstockmedia.s3.eu-central-1.amazonaws.com/stock/pcbs.jpg"
                />
                <div class="title" id="title">
                    <h1>PCBs</h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://mechmarketstockmedia.s3.eu-central-1.amazonaws.com/stock/switches.jpg"
                />
                <div class="title" id="title">
                    <h1>Switches</h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://mechmarketstockmedia.s3.eu-central-1.amazonaws.com/stock/travelling_cases.jpg"
                />
                <div class="title" id="title">
                    <h1>Travelling cases</h1>
                </div>
            </div>
            <div class="grid-item">
                <img
                    src="https://mechmarketstockmedia.s3.eu-central-1.amazonaws.com/stock/wrist_rests.jpg"
                />
                <div class="title" id="title">
                    <h1>Wrist-rests</h1>
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
    margin-bottom: 26px;
}
.categories {
    display: grid;
    grid-template-columns: auto auto;
    grid-gap: 16px;
}
.grid-item {
    position: relative;
}
.grid-item,
img {
    height: 300px;
    min-width: 100%;
    box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
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
    font-size: 25px;
    padding: 15px;
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.5s, visibility 0.5s;
}
.grid-item:hover #title {
    visibility: visible;
    opacity: 1;
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
