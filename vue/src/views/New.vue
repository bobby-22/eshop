<template>
    <div class="container">
        <form class="form" v-on:submit.stop.prevent="submitRegister">
            <h1 class="title">
                New product
                <i class="fas fa-plus"></i>
            </h1>
            <div class="field">
                <label class="label">Title</label>
                <div class="control has-icons-left has-icons-right">
                    <input
                        class="input"
                        type="text"
                        v-model="title"
                        v-on:input="countCharacters()"
                    />
                    <span class="icon is-small is-left">
                        <i class="fas fa-heading"></i>
                    </span>
                    <span
                        class="icon is-small is-right has-text-danger"
                        v-if="this.titleLength > 50"
                    >
                        {{ this.titleLength }}
                    </span>
                    <span class="icon is-small is-right" v-else>
                        {{ this.titleLength }}
                    </span>
                </div>
                <p class="help is-danger" v-if="errorTitleBoolean">
                    <i class="fas fa-exclamation-circle"></i>
                    {{ this.errorMessageTitle }}
                </p>
            </div>
            <div class="container-column">
                <div class="field" id="price">
                    <label class="label">Price</label>
                    <div class="control has-icons-left">
                        <input class="input" type="number" v-model="price" />
                        <span class="icon is-small is-left">
                            <i class="fas fa-euro-sign"></i>
                        </span>
                    </div>
                    <p class="help is-danger" v-if="errorPriceBoolean">
                        <i class="fas fa-exclamation-circle"></i>
                        {{ this.errorMessagePrice }}
                    </p>
                </div>
                <div class="field" id="country">
                    <label class="label">Country</label>
                    <div class="control has-icons-left has-icons-right">
                        <input
                            class="input"
                            type="text"
                            v-model="country"
                            v-on:input="countCharacters()"
                        />
                        <span class="icon is-small is-left">
                            <i class="fas fa-map-marker-alt"></i>
                        </span>
                        <span
                            class="icon is-small is-right has-text-danger"
                            v-if="this.countryLength > 25"
                        >
                            {{ this.countryLength }}
                        </span>
                        <span class="icon is-small is-right" v-else>
                            {{ this.countryLength }}
                        </span>
                    </div>
                    <p class="help is-danger" v-if="errorCountryBoolean">
                        <i class="fas fa-exclamation-circle"></i>
                        {{ this.errorMessageCountry }}
                    </p>
                </div>
                <div class="field" id="category">
                    <label class="label">Category</label>
                    <div class="control has-icons-left">
                        <div class="select">
                            <select v-model="category">
                                <option disabled value="">
                                    Select category
                                </option>
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
                        <p class="help is-danger" v-if="errorCategoryBoolean">
                            <i class="fas fa-exclamation-circle"></i>
                            {{ this.errorMessageCategory }}
                        </p>
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
                <p class="help is-danger" v-if="errorDescriptionBoolean">
                    <i class="fas fa-exclamation-circle"></i>
                    {{ this.errorMessageDescription }}
                </p>
            </div>
            <div class="field">
                <div class="file has-name is-fullwidth">
                    <label class="file-label">
                        <input
                            class="file-input"
                            type="file"
                            accept="image/*"
                            name="thumbnail"
                            v-on:change="uploadThumbnail"
                        />
                        <span class="file-cta">
                            <span class="file-icon">
                                <i class="fas fa-image"></i>
                            </span>
                            <span class="file-label">Choose a thumbnail</span>
                        </span>
                        <span class="file-name" v-if="!thumbnail">
                            No thumbnail uploaded
                        </span>
                        <span class="file-name" v-else>
                            {{ thumbnail.name }}
                        </span>
                    </label>
                </div>
                <p class="help is-danger" v-if="errorThumbnailBoolean">
                    <i class="fas fa-exclamation-circle"></i>
                    {{ this.errorMessageThumbnail }}
                </p>
            </div>
            <div class="field">
                <div class="file has-name is-fullwidth">
                    <label class="file-label">
                        <input
                            class="file-input"
                            type="file"
                            accept="image/*"
                            name="images"
                            v-on:change="uploadImage"
                            multiple
                        />
                        <span class="file-cta">
                            <span class="file-icon">
                                <i class="fas fa-images"></i>
                            </span>
                            <span class="file-label">Choose images</span>
                        </span>
                        <span class="file-name" v-if="!images">
                            No images uploaded
                        </span>
                        <span
                            class="file-name"
                            v-else
                            v-for="image in images"
                            :key="image.id"
                        >
                            {{ image.name }}
                        </span>
                    </label>
                </div>
                <p class="help is-danger" v-if="errorImagesBoolean">
                    <i class="fas fa-exclamation-circle"></i>
                    {{ this.errorMessageImages }}
                </p>
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
            thumbnail: null,
            images: null,
            stripe_product_id: null,
            errors: [],
            errorTitleBoolean: false,
            errorCountryBoolean: false,
            errorPriceBoolean: false,
            errorCategoryBoolean: false,
            errorDescriptionBoolean: false,
            errorThumbnailBoolean: false,
            errorImagesBoolean: false,

            errorMessageTitle: null,
            errorMessagePrice: null,
            errorMessageCountry: null,
            errorMessageCategory: null,
            errorMessageDescription: null,
            errorMessageThumbnail: null,
            errorMessageImages: null,

            titleLength: null,
            countryLength: null,
        };
    },
    methods: {
        checkErrors() {
            if (!this.title) {
                this.errorTitleBoolean = true;
                this.errorMessageTitle = "Title cannot be empty";
            } else if (this.title.length > 50) {
                this.errorTitleBoolean = true;
                this.errorMessageTitle =
                    "Title cannot be longer than 50 characters";
            } else {
                this.errorTitleBoolean = false;
            }
            if (!this.price) {
                this.errorPriceBoolean = true;
                this.errorMessagePrice = "Price cannot be empty";
            } else {
                this.errorPriceBoolean = false;
            }
            if (!this.country) {
                this.errorCountryBoolean = true;
                this.errorMessageCountry = "Country cannot be empty";
            } else if (this.country.length > 25) {
                this.errorCountryBoolean = true;
                this.errorMessageCountry =
                    "Country cannot be longer than 25 characters";
            } else {
                this.errorCountryBoolean = false;
            }
            if (!this.category) {
                this.errorCategoryBoolean = true;
                this.errorMessageCategory = "Category cannot be empty";
            } else {
                this.errorCategoryBoolean = false;
            }
            if (!this.description) {
                this.errorDescriptionBoolean = true;
                this.errorMessageDescription = "Description cannot be empty";
            } else {
                this.errorDescriptionBoolean = false;
            }
            if (!this.thumbnail) {
                this.errorThumbnailBoolean = true;
                this.errorMessageThumbnail = "Upload a thumbnail";
            } else {
                this.errorThumbnailBoolean = false;
            }
            if (!this.images) {
                this.errorImagesBoolean = true;
                this.errorMessageImages = "Upload some images";
            } else {
                this.errorImagesBoolean = false;
            }
        },
        countCharacters() {
            let titleLength = 0;
            let countryLength = 0;
            for (let i = 0; i < this.title.length; i++) {
                titleLength++;
            }
            for (let j = 0; j < this.country.length; j++) {
                countryLength++;
            }
            this.titleLength = titleLength;
            this.countryLength = countryLength;
        },
        uploadThumbnail(event) {
            this.thumbnail = event.target.files[0];
        },
        uploadImage(event) {
            this.images = event.target.files;
        },
        submitNewProduct() {
            this.checkErrors();
            let product = new FormData();
            product.append("title", this.title);
            product.append("price", this.price);
            product.append("country", this.country);
            product.append("category", this.category);
            product.append("owner", this.$store.state.currentUserId);
            product.append("description", this.description);
            product.append("thumbnail", this.thumbnail);
            if (this.thumbnail == null) {
                this.errors.push("ahoj");
            }
            djangoAPI
                .post("/ahoj/new/", product)
                .then((newProductResponse) => {
                    this.stripe_product_id =
                        newProductResponse.data.stripe_product_id;
                    this.uploadImages();
                    console.log(newProductResponse);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        uploadImages() {
            let images = new FormData();
            for (let i = 0; i < this.images.length; i++) {
                images.append("stripe_product_id", this.stripe_product_id);
                images.append("images", this.images[i]);
            }
            djangoAPI
                .post("/dobry/new/", images)
                .then((newProductImagesResponse) => {
                    console.log(newProductImagesResponse);
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
                });
        },
    },
    beforeCreate() {
        this.$store.commit("localStorageSavedCurrentUserId");
    },
    created() {
        this.countCharacters();
        document.title = "New Product | MechMarketEU";
    },
};
</script>

<style scoped>
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
    text-align: center;
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
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
    -webkit-appearance: none;
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
