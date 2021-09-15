<template>
    <div class="container">
        <form class="form" @submit.prevent>
            <h1 class="title">
                Update "{{ product.title }}"
                <i class="far fa-edit"></i>
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
                        v-if="titleLength > 50"
                    >
                        {{ titleLength }}
                    </span>
                    <span class="icon is-small is-right" v-else>
                        {{ titleLength }}
                    </span>
                </div>
                <p class="help is-danger" v-if="errorTitleBoolean">
                    <i class="fas fa-exclamation-circle"></i>
                    {{ errorMessageTitle }}
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
                        {{ errorMessagePrice }}
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
                            v-if="countryLength > 25"
                        >
                            {{ countryLength }}
                        </span>
                        <span class="icon is-small is-right" v-else>
                            {{ countryLength }}
                        </span>
                    </div>
                    <p class="help is-danger" v-if="errorCountryBoolean">
                        <i class="fas fa-exclamation-circle"></i>
                        {{ errorMessageCountry }}
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
                            {{ errorMessageCategory }}
                        </p>
                    </div>
                </div>
            </div>
            <div class="field">
                <span class="label">Description</span>
                <div class="control">
                    <textarea
                        class="textarea"
                        rows="10"
                        type="text"
                        v-model="description"
                    ></textarea>
                </div>
                <p class="help is-danger" v-if="errorDescriptionBoolean">
                    <i class="fas fa-exclamation-circle"></i>
                    {{ errorMessageDescription }}
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
                        <span
                            class="file-name"
                            id="thumbnail"
                            v-if="!thumbnail"
                        >
                            <img v-bind:src="thumbnailCloud" />
                            <span class="thumbnail-name">
                                {{ thumbnailCloud }}
                            </span>
                        </span>
                        <span class="file-name" v-else>
                            {{ thumbnail.name }}
                        </span>
                    </label>
                </div>
            </div>
            <div class="field">
                <div class="file has-name is-fullwidth is-boxed" id="images">
                    <label class="file-label">
                        <input
                            class="file-input"
                            type="file"
                            accept="image/*"
                            name="images"
                            v-on:change="uploadImages"
                            multiple
                        />
                        <span class="file-cta">
                            <span class="file-icon">
                                <i class="fas fa-images"></i>
                            </span>
                            <span class="file-label">Choose images</span>
                        </span>
                    </label>
                    <span
                        class="file-name"
                        id="file-name"
                        v-for="image in imagesCloud"
                        :key="image.id"
                    >
                        <img v-bind:src="image.images" />
                        <span class="image-name">
                            {{ image.images }}
                        </span>
                        <a
                            class="image-delete"
                            v-on:click="deleteImageCloud(image)"
                            ><i class="far fa-times-circle"></i
                        ></a>
                    </span>
                    <span
                        class="file-name"
                        id="file-name"
                        v-for="image in images"
                        :key="image.id"
                    >
                        <span class="image-name">
                            {{ image.name }}
                        </span>
                        <a
                            class="image-delete"
                            v-on:click="deleteImageLocal(image)"
                            ><i class="far fa-times-circle"></i
                        ></a>
                    </span>
                </div>
                <p class="help is-danger" v-if="errorImagesBoolean">
                    <i class="fas fa-exclamation-circle"></i>
                    {{ errorMessageImages }}
                </p>
            </div>
            <div class="field">
                <div class="control">
                    <button
                        class="button is-link"
                        v-on:click="submitUpdatedProduct"
                        v-bind:disabled="submittedBoolean"
                    >
                        Update
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
    name: "ProductsUpdate",
    data() {
        return {
            product: this.$store.state.productData,
            title: this.$store.state.productData.title,
            price: this.$store.state.productData.price,
            country: this.$store.state.productData.country,
            category: this.$store.state.productData.category,
            description: this.$store.state.productData.description,

            thumbnail: "",
            thumbnailCloud: this.$store.state.productData.thumbnail,
            images: [],
            imagesCloud: this.$store.state.imagesCloud,

            errors: [],
            errorTitleBoolean: false,
            errorCountryBoolean: false,
            errorPriceBoolean: false,
            errorCategoryBoolean: false,
            errorDescriptionBoolean: false,
            errorImagesBoolean: false,
            submittedBoolean: false,

            errorMessageTitle: null,
            errorMessagePrice: null,
            errorMessageCountry: null,
            errorMessageCategory: null,
            errorMessageDescription: null,
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
            } else if (this.price > 9999) {
                this.errorPriceBoolean = true;
                this.errorMessagePrice =
                    "Price cannot be bigger than 4 figures";
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
        uploadImages(event) {
            this.images = event.target.files;
        },
        deleteImageLocal(image) {
            this.images = Object.values(this.images).filter((i) => {
                return i.name !== image.name;
            });
        },
        deleteImageCloud(image) {
            this.imagesCloud = Object.values(this.imagesCloud).filter((i) => {
                return i.id !== image.id;
            });
            this.$store.commit("saveImagesCloudState", this.imagesCloud);
            this.deleteImage(image.id);
        },
        submitUpdatedProduct() {
            if (this.images.length + this.imagesCloud.length > 10) {
                this.errorImagesBoolean = true;
                this.errorMessageImages = "Max 10 images are allowed";
                return;
            } else {
                this.submittedBoolean = true;
                this.errorImagesBoolean = false;
            }
            this.checkErrors();
            let product = new FormData();
            product.append("title", this.title);
            product.append("price", this.price);
            product.append("country", this.country);
            product.append("category", this.category);
            product.append("owner", this.product.owner);
            product.append("description", this.description);
            product.append("thumbnail", this.thumbnail);
            product.append("post_id", this.product.post_id);
            djangoAPI
                .put(
                    `/api/v1/products/${this.product.post_id}/update/`,
                    product,
                    {
                        headers: {
                            Authorization: `JWT ${this.$store.state.tokenAccess}`,
                        },
                    }
                )
                .then((updatedProductResponse) => {
                    console.log(updatedProductResponse);
                    if (this.images.length !== 0) {
                        this.submitNewImages();
                    } else {
                        this.$router.push(
                            "/accounts/profile/" + this.$store.state.currentUser
                        );
                        toast({
                            message: "Post has been successfully updated!",
                            type: "is-success",
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 3000,
                            position: "bottom-right",
                        });
                    }
                })
                .catch((error) => {
                    console.log(error);
                    this.submittedBoolean = false;
                    if (
                        error.response.status === 403 ||
                        error.response.status === 401
                    ) {
                        this.$store.commit("removeCredentialsState");
                        this.$router.push("/error");
                    }
                });
        },
        submitNewImages() {
            if (this.images.length + this.imagesCloud.length > 10) {
                this.errorImagesBoolean = true;
                this.errorMessageImages = "Max 10 images are allowed";
                return;
            } else {
                this.submittedBoolean = true;
                this.errorImagesBoolean = false;
            }
            let images = new FormData();
            for (let i = 0; i < this.images.length; i++) {
                images.append("owner", this.$store.state.currentUserId);
                images.append("post_id", this.product.post_id);
                images.append("images", this.images[i]);
            }
            djangoAPI
                .post("/api/v1/images/create/", images, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.tokenAccess}`,
                    },
                })
                .then((createdImagesResponse) => {
                    console.log(createdImagesResponse);
                    this.$router.push(
                        "/accounts/profile/" + this.$store.state.currentUser
                    );
                    toast({
                        message: "Post has been successfully updated!",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: "bottom-right",
                    });
                })
                .catch((error) => {
                    console.log(error);
                    this.submittedBoolean = false;
                    if (
                        error.response.status === 403 ||
                        error.response.status === 401
                    ) {
                        this.$store.commit("removeCredentialsState");
                        this.$router.push("/error");
                    }
                });
        },
        deleteImage(image_id) {
            djangoAPI
                .delete(`/api/v1/images/${image_id}/delete/`, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.tokenAccess}`,
                    },
                })
                .then((deletedImagesResponse) => {
                    console.log(deletedImagesResponse);
                    toast({
                        message: "Image has been successfully deleted!",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: "bottom-right",
                    });
                })
                .catch((error) => {
                    console.log(error);
                    if (
                        error.response.status === 403 ||
                        error.response.status === 401
                    ) {
                        this.$store.commit("removeCredentialsState");
                        this.$router.push("/error");
                    }
                });
        },
        setTitle() {
            document.title = `Update "${this.product.title}" | MechMarketEU`;
        },
    },
    beforeCreate() {
        this.$store.commit("localStorageProductData");
        this.$store.commit("localStorageProductImages");
    },
    created() {
        this.countCharacters();
        this.setTitle();
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
img {
    height: inherit;
}
.file-label,
.file-name {
    text-align: center;
}
#file-name {
    display: flex;
    justify-content: flex-start;
    padding-left: 0px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
}
#thumbnail {
    display: flex;
    padding-left: 0px;
}
#images {
    display: flex;
    flex-direction: column;
}
.thumbnail-name,
.image-name {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-left: 30px;
    margin-right: 30px;
}
.thumbnail-name {
    margin-left: 15px;
    margin-right: 15px;
}
.image-delete {
    position: absolute;
    right: 15px;
}
a {
    color: #424242;
}
a:hover {
    color: black;
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
