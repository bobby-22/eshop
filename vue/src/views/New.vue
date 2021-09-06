<template>
    <div class="container">
        <form class="form" v-on:submit.stop.prevent="submitRegister">
            <h1 class="title">
                New product
                <i class="fas fa-plus"></i>
            </h1>
            <div class="notification is-danger" v-if="errors.length">
                <p id="error" v-for="error in errors" v-bind:key="error">
                    {{ error }}
                </p>
            </div>
            <div class="field">
                <label class="label">Title</label>
                <div class="control has-icons-left">
                    <input class="input" type="text" v-model="title" />
                    <span class="icon is-small is-left">
                        <i class="fas fa-heading"></i>
                    </span>
                </div>
            </div>
            <div class="container-column">
                <div class="field" id="price">
                    <label class="label">Price</label>
                    <div class="control has-icons-left">
                        <input class="input" type="text" v-model="price" />
                        <span class="icon is-small is-left">
                            <i class="fas fa-euro-sign"></i>
                        </span>
                    </div>
                </div>
                <div class="field" id="country">
                    <label class="label">Country</label>
                    <div class="control has-icons-left">
                        <input class="input" type="text" v-model="country" />
                        <span class="icon is-small is-left">
                            <i class="fas fa-map-marker-alt"></i>
                        </span>
                    </div>
                </div>
                <div class="field" id="category">
                    <label class="label">Category</label>
                    <div class="control has-icons-left">
                        <div class="select">
                            <select v-model="category">
                                <option disabled value="">Select category</option>
                                <option>Cables</option>
                                <option>Cases</option>
                                <option>Deskmats</option>
                                <option>Keyboards</option>
                                <option>Keycaps</option>
                                <option>Others</option>
                                <option>PCBs</option>
                                <option>Plates</option>
                                <option>Travelling-cases</option>
                                <option>Wrist-rests</option>
                            </select>
                        </div>
                        <span class="icon is-small is-left">
                            <i class="fas fa-list"></i>
                        </span>
                    </div>
                </div>
            </div>
            <div class="field">
                <span class="label">Description</span>
                <div class="control">
                    <textarea
                        class="textarea"
                        type="text"
                        v-model="description"
                    ></textarea>
                </div>
            </div>
            <div class="field">
                <div class="file has-name is-fullwidth">
                    <label class="file-label">
                        <input
                            class="file-input"
                            type="file"
                            name="thumbnail"
                        />
                        <span class="file-cta">
                            <span class="file-icon">
                                <i class="fas fa-image"></i>
                            </span>
                            <span class="file-label">Choose a thumbnail</span>
                        </span>
                        <span class="file-name">
                            Screen Shot 2017-07-29 at 15.54.25.png
                        </span>
                    </label>
                </div>
            </div>
            <div class="field">
                <div class="file has-name is-fullwidth">
                    <label class="file-label">
                        <input
                            class="file-input"
                            type="file"
                            name="thumbnail"
                        />
                        <span class="file-cta">
                            <span class="file-icon">
                                <i class="fas fa-images"></i>
                            </span>
                            <span class="file-label">Choose images</span>
                        </span>
                        <span class="file-name">
                            Screen Shot 2017-07-29 at 15.54.25.png
                        </span>
                    </label>
                </div>
            </div>
            <div class="field">
                <div class="control">
                    <button
                        class="button is-link"
                        v-on:click="submitNewProduct"
                    >
                        Create
                    </button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import { toast } from "bulma-toast";
export default {
    name: "New",
    data() {
        return {
            title: "",
            price: "",
            country: "",
            category: "",
            description: "",
            errors: [],
        };
    },
    methods: {
        submitNewProduct() {
            let product = {
                title: this.title,
                price: this.price,
                country: this.country,
                category: this.category,
                description: this.description,
            };
            djangoAPI
                .post("/testing/new/", product)
                .then((newProductResponse) => {
                    console.log(newProductResponse);
                    toast({
                        message: "Product was successfully added!",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                    this.$router.push("/user/" + this.$store.state.currentUser);
                })
                .catch((error) => {
                    console.log(error);
                    this.errors.splice(0, this.errors.length);
                    for (let property in error.response.data) {
                        this.errors.push(`${error.response.data[property]}`);
                    }
                });
        },
    },
    created() {
        document.title = "New Product | MechMarketEU";
    },
};
</script>

<style lang="scss" scoped>
.container {
    min-height: 100%;
    display: flex;
    justify-content: space-around;
    margin: 30px 300px 30px 300px;
}
.form {
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
    border-radius: 10px;
    padding: 30px;
}
#error {
    text-align: left;
}
.title {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.input {
    height: 100%;
}
.container-column {
    display: flex;
    flex-wrap: wrap;
    column-gap: 5px;
}
#price,
#country {
    flex-grow: 1;
}
select {
    height: 37px;
    line-height: normal;
}
#category {
    margin-bottom: 10px;
}
@media (max-width: 1024px) {
    .container {
        justify-content: start;
        margin: 0px;
    }
    .form {
        box-shadow: none;
        border-radius: 0px;
    }
}
</style>
