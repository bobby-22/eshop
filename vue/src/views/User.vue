<template>
    <div class="container">
        <div class="title-container">
            <h1 class="title" id="title-header">{{ username }}'s posts</h1>
            <div class="reviews">
                <div class="modalActivate">
                    <button
                        class="button is-text"
                        id="view-reviews"
                        v-on:click="modalShowBoolean = true"
                    >
                        Show reviews
                    </button>
                    <div
                        class="modal"
                        v-bind:class="{ 'is-active': modalShowBoolean }"
                    >
                        <div
                            class="modal-background"
                            v-on:click="modalShowBoolean = false"
                        ></div>
                        <div class="modal-content">
                            <h1 class="title" id="title-modal">
                                User reviews
                                <i class="far fa-star"></i>
                            </h1>
                            <p v-if="!reviews.length">No reviews yet...</p>
                            <div class="reviews-content">
                                <div
                                    class="review-list"
                                    v-for="review in reviews"
                                    :key="review.id"
                                >
                                    <div class="header">
                                        <div class="left">
                                            <i
                                                class="far fa-smile-beam"
                                                v-if="
                                                    review.rating === 'Positive'
                                                "
                                            ></i>
                                            <i
                                                class="far fa-angry"
                                                v-if="
                                                    review.rating === 'Negative'
                                                "
                                            ></i>
                                            <span class="reviewer">
                                                <router-link
                                                    v-on:click="
                                                        modalShowBoolean = false
                                                    "
                                                    v-bind:to="{
                                                        name: 'User',
                                                        params: {
                                                            user: review.reviewer,
                                                        },
                                                    }"
                                                >
                                                    {{ review.reviewer }}
                                                </router-link>
                                            </span>
                                        </div>
                                        <div class="right">
                                            <i class="far fa-calendar-alt"></i>
                                            {{ review.date }}
                                        </div>
                                    </div>
                                    <div class="description">
                                        <i>{{ review.description }}</i>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <button
                            class="modal-close is-large"
                            aria-label="close"
                            v-on:click="modalShowBoolean = false"
                        ></button>
                    </div>
                </div>
                <div class="modalActivate">
                    <button
                        class="button is-dark"
                        v-if="authenticated"
                        v-on:click="modalBoolean = true"
                    >
                        Review
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
                                    Review {{ username }}
                                    <i class="far fa-star"></i>
                                </h1>
                                <div class="field">
                                    <span class="label">Rating</span>
                                    <div class="control has-icons-left">
                                        <div class="select">
                                            <select v-model="rating">
                                                <option disabled value="">
                                                    Select rating
                                                </option>
                                                <option>Positive</option>
                                                <option>Negative</option>
                                            </select>
                                        </div>
                                        <span class="icon is-small is-left">
                                            <i
                                                class="far fa-smile-beam"
                                                v-if="rating === 'Positive'"
                                            ></i>
                                            <i
                                                class="far fa-angry"
                                                v-if="rating === 'Negative'"
                                            ></i>
                                            <i
                                                class="fas fa-star-half-alt"
                                                v-if="rating === null"
                                            ></i>
                                        </span>
                                    </div>
                                    <p
                                        class="help is-danger"
                                        v-if="errorRatingBoolean"
                                    >
                                        <i
                                            class="fas fa-exclamation-circle"
                                        ></i>
                                        {{ errorMessageRating }}
                                    </p>
                                </div>
                                <div class="field">
                                    <span class="label">Description</span>
                                    <div class="control">
                                        <textarea
                                            class="textarea"
                                            rows="5"
                                            type="text"
                                            v-model="description"
                                        ></textarea>
                                    </div>
                                    <p
                                        class="help is-danger"
                                        v-if="errorDescriptionBoolean"
                                    >
                                        <i
                                            class="fas fa-exclamation-circle"
                                        ></i>
                                        {{ errorMessageDescription }}
                                    </p>
                                </div>
                                <div class="field">
                                    <div class="control">
                                        <button
                                            class="button is-success"
                                            v-on:click="reviewUser"
                                            v-bind:disabled="submittedBoolean"
                                        >
                                            Send
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
        </div>
        <p v-if="!products.length">No posts added...</p>
        <AccountsUser
            v-for="product in products"
            v-bind:key="product.id"
            v-bind:product="product"
        />
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import { toast } from "bulma-toast";
import AccountsUser from "../components/AccountsUser.vue";
export default {
    name: "User",
    components: {
        AccountsUser,
    },
    data() {
        return {
            products: [],
            product: null,
            reviews: [],
            username: this.$route.params.user,
            authenticated: this.$store.state.authenticated,
            rating: null,
            description: null,
            errorMessageRating: null,
            errorMessageDescription: null,

            errorRatingBoolean: false,
            errorDescriptionBoolean: false,
            modalBoolean: false,
            modalShowBoolean: false,
            submittedBoolean: false,
        };
    },
    methods: {
        getUserProducts() {
            djangoAPI
                .get("/api/v1/accounts/user/" + this.$route.params.user)
                .then((profileResponse) => {
                    console.log(profileResponse);
                    this.products = profileResponse.data;
                    for (let i = 0; i < this.products.slice(0, 1).length; i++) {
                        this.product = this.products[i];
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        getUserReviews() {
            djangoAPI
                .get(`/api/v1/accounts/user/${this.username}/reviews`)
                .then((userReviewsResponse) => {
                    console.log(userReviewsResponse);
                    this.reviews = userReviewsResponse.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        reviewUser() {
            if (!this.rating) {
                this.errorRatingBoolean = true;
                this.errorMessageRating = "Rating cannot be empty";
                return;
            } else {
                this.errorRatingBoolean = false;
            }
            if (!this.description) {
                this.errorDescriptionBoolean = true;
                this.errorMessageDescription = "Description cannot be empty";
                return;
            } else {
                this.errorDescriptionBoolean = false;
            }
            this.submittedBoolean = true;
            let review = {
                owner: this.product.owner,
                rating: this.rating,
                description: this.description,
            };
            djangoAPI
                .post(
                    `/api/v1/accounts/user/${this.product.user}/review/`,
                    review,
                    {
                        headers: {
                            Authorization: `JWT ${this.$store.state.tokenAccess}`,
                        },
                    }
                )
                .then((reviewedUserResponse) => {
                    console.log(reviewedUserResponse);
                    this.modalBoolean = false;
                    toast({
                        message: "Review has been successfully posted!",
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
                        this.$router.push("/error");
                    }
                });
        },
        setTitle() {
            document.title = `${this.$route.params.user}'s Posts | MechMarketEU`;
        },
    },
    created() {
        this.getUserProducts();
        this.getUserReviews();
        this.setTitle();
    },
    watch: {
        $route(to, from) {
            if (to.name === "User") {
                (this.username = this.$route.params.user),
                    (this.authenticated = this.$store.state.authenticated),
                    this.getUserProducts();
                this.getUserReviews();
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
.title-container {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #ededed;
    padding-bottom: 15px;
    margin-bottom: 20px;
}
#title-header {
    margin-bottom: 0px;
}
.reviews {
    display: flex;
}
.review-list {
    border-bottom: 1px solid #ededed;
    padding: 15px;
}
.review-list:last-child {
    border-bottom: none;
}
.left {
    font-size: 20px;
    font-weight: 500;
    margin-bottom: 5px;
}
.reviewer {
    margin-left: 5px;
}
.right {
    color: #949494;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
#view-reviews {
    margin-left: 15px;
}
.description {
    white-space: pre-line;
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
