<template>
    <div class="container">
        <div class="details" v-for="detail in details" :key="detail.id">
            <div class="details-left">
                <div class="detail-thumbnail">
                    <img v-bind:src="photo" />
                    <div class="gallery-control">
                        <i
                            class="fas fa-chevron-left"
                            id="controls"
                            v-on:click="previousPhoto"
                        ></i>
                        <i
                            class="fas fa-chevron-right"
                            id="controls"
                            v-on:click="nextPhoto"
                        ></i>
                    </div>
                </div>
                <div class="detail-images">
                    <img
                        id="image"
                        v-for="photo in gallery"
                        :key="photo.id"
                        v-bind:src="photo"
                    />
                </div>
            </div>

            <div class="details-right">
                <div class="detail-header">
                    <div class="detail-title">
                        <h1 class="title" id="title-header">
                            {{ detail.title }}
                        </h1>
                        <div class="modalActivate">
                            <button
                                class="button is-dark"
                                v-if="authenticated"
                                v-on:click="modalBoolean = true"
                            >
                                Contact
                            </button>
                            <div
                                class="modal"
                                v-bind:class="{ 'is-active': modalBoolean }"
                            >
                                <div
                                    class="modal-background"
                                    v-on:click="modalBoolean = false"
                                ></div>
                                <div class="modal-content">
                                    <form class="form" @submit.prevent>
                                        <h1 class="title" id="title-modal">
                                            Contact {{ detail.user }}
                                            <i class="far fa-address-book"></i>
                                        </h1>
                                        <div class="field">
                                            <span class="label">Email</span>
                                            <div class="control has-icons-left">
                                                <input
                                                    class="input"
                                                    type="email"
                                                    placeholder="example@example.com"
                                                    v-model="email"
                                                />
                                                <span
                                                    class="
                                                        icon
                                                        is-small is-left
                                                    "
                                                >
                                                    <i
                                                        class="fas fa-envelope"
                                                    ></i>
                                                </span>
                                            </div>
                                            <p
                                                class="help is-danger"
                                                v-if="errorEmailBoolean"
                                            >
                                                <i
                                                    class="
                                                        fas
                                                        fa-exclamation-circle
                                                    "
                                                ></i>
                                                {{ errorMessageEmail }}
                                            </p>
                                        </div>
                                        <div class="field">
                                            <span class="label">Message</span>
                                            <div class="control">
                                                <textarea
                                                    class="textarea"
                                                    rows="10"
                                                    type="text"
                                                    v-model="description"
                                                ></textarea>
                                            </div>
                                            <p
                                                class="help is-danger"
                                                v-if="errorDescriptionBoolean"
                                            >
                                                <i
                                                    class="
                                                        fas
                                                        fa-exclamation-circle
                                                    "
                                                ></i>
                                                {{ errorMessageDescription }}
                                            </p>
                                        </div>
                                        <div class="field">
                                            <div class="control">
                                                <button
                                                    class="button is-link"
                                                    v-on:click="contactUser"
                                                    v-bind:disabled="
                                                        submittedBoolean
                                                    "
                                                >
                                                    Contact
                                                </button>
                                            </div>
                                        </div>
                                    </form>
                                </div>
                                <button
                                    class="modal-close is-large"
                                    aria-label="close"
                                    v-on:click="modalBoolean = false"
                                ></button>
                            </div>
                        </div>
                    </div>
                    <div class="detail-header-top">
                        <h2 class="title is-5">
                            <i class="fas fa-euro-sign"></i>
                            {{ detail.price }}
                        </h2>
                        <h2 class="title is-5">
                            <i class="fas fa-map-marker-alt"></i>
                            {{ detail.country }}
                        </h2>
                    </div>
                    <div class="detail-header-bottom">
                        <h2 class="title is-6">
                            <i class="fas fa-calendar-alt"></i>
                            {{ detail.date }}
                        </h2>
                        <h2 class="title is-6">
                            <i class="fas fa-user"></i>
                            <router-link
                                v-bind:to="{
                                    name: 'User',
                                    params: {
                                        user: detail.user,
                                    },
                                }"
                                >&nbsp;{{ detail.user }}
                            </router-link>
                        </h2>
                    </div>
                </div>
                <div class="detail-body">
                    <p>{{ detail.description }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import { toast } from "bulma-toast";
export default {
    name: "Details",
    data() {
        return {
            details: [],
            images: [],
            gallery: [],
            photo: null,
            product: null,
            authenticated: this.$store.state.authenticated,
            email: null,
            description: null,
            errorMessageEmail: null,
            errorMessageDescription: null,

            errorEmailBoolean: false,
            errorDescriptionBoolean: false,
            submittedBoolean: false,
            modalBoolean: false,
        };
    },
    methods: {
        getDetails() {
            let post_id = this.$route.params.post_id;
            djangoAPI({
                method: "GET",
                url: `/api/v1/products/${post_id}/`,
            })
                .then((detailsResponse) => {
                    console.log(detailsResponse);
                    this.details = detailsResponse.data;
                    this.product = this.details[0];
                    this.gallery.push(this.product.thumbnail);
                    this.photo = this.gallery[0];
                    document.title = `${this.product.title} | MechMarketEU`;
                    this.getImages();
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        getImages() {
            let post_id = this.$route.params.post_id;
            djangoAPI({
                method: "GET",
                url: `/api/v1/images/${post_id}/`,
            })
                .then((imagesResponse) => {
                    console.log(imagesResponse);
                    this.images = imagesResponse.data;
                    for (let i = 0; i < this.images.length; i++) {
                        this.gallery.push(this.images[i].images);
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        contactUser() {
            if (!this.email) {
                this.errorEmailBoolean = true;
                this.errorMessageEmail = "Email cannot be empty";
                return;
            } else {
                this.errorEmailBoolean = false;
            }
            if (!this.description) {
                this.errorDescriptionBoolean = true;
                this.errorMessageDescription = "Message cannot be empty";
                return;
            } else {
                this.errorDescriptionBoolean = false;
            }
            this.submittedBoolean = true;
            let message = {
                email: this.email,
                description: this.description,
            };
            djangoAPI
                .post(
                    `/api/v1/accounts/user/${this.product.user}/contact/`,
                    message,
                    {
                        headers: {
                            Authorization: `JWT ${this.$store.state.tokenAccess}`,
                        },
                    }
                )
                .then((contactedUserResponse) => {
                    console.log(contactedUserResponse);
                    this.modalBoolean = false;
                    toast({
                        message: "Message has been successfully sent!",
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
                    if (error.response.status === 401) {
                        this.$router.push("/error");
                    }
                });
        },
        previousPhoto() {
            let currentPosition = this.gallery.indexOf(this.photo);
            this.photo = this.gallery[currentPosition - 1];
            if (this.photo === undefined) {
                this.photo = this.gallery[this.gallery.length - 1];
            }
        },
        nextPhoto() {
            let currentPosition = this.gallery.indexOf(this.photo);
            this.photo = this.gallery[currentPosition + 1];
            if (this.photo === undefined) {
                this.photo = this.gallery[0];
            }
        },
    },
    created() {
        this.getDetails();
    },
};
</script>

<style scoped>
.container {
    min-height: 100%;
    width: 100%;
    padding: 30px;
}
.details {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.details-left {
    display: flex;
    flex-direction: column;
    flex-basis: 50%;
    margin-right: 30px;
}
.detail-thumbnail {
    position: relative;
    max-width: fit-content;
}
.detail-thumbnail > img {
    max-height: 500px;
}
.gallery-control {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    min-width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 15px;
}
#controls {
    opacity: 0.3;
    background: #fafafa;
    color: #616161;
    transition: opacity 0.5s;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    line-height: 40px;
    text-align: center;
}
#controls:hover {
    color: black;
    opacity: 0.7;
}
.detail-images {
    display: flex;
    flex-direction: row;
    overflow: scroll;
    overflow-y: hidden;
    column-gap: 5px;
}
#image {
    height: 100px;
}
.details-right {
    flex-basis: 50%;
}
.detail-title {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 15px;
    margin-bottom: 15px;
}
#title-header {
    margin-bottom: 0px;
}
.detail-header-top {
    display: flex;
    justify-content: space-between;
}
.detail-header-bottom {
    display: flex;
    justify-content: space-between;
    margin-top: -15px;
    margin-bottom: 24px;
}
.title.is-6 {
    margin-bottom: 0px;
}
.detail-body {
    white-space: pre-line;
}
::-webkit-scrollbar {
    height: 10px;
}
::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background: #c2c9d2;
}
@media (max-width: 1024px) {
    .details {
        flex-direction: column;
    }
    .details-left {
        margin-right: 0px;
        margin-bottom: 15px;
    }
}
.modal-content {
    background: white;
    border-radius: 10px;
    padding: 30px;
}
.notification.is-danger {
    padding: 20px 27px 20px 24px;
}
#title-modal {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.input {
    height: 100%;
}
#error {
    text-align: center;
}
@media (max-width: 1024px) {
    .modal-content {
        border-radius: 0px;
    }
}
</style>
