<template>
    <div class="container">
        <form class="form" v-on:submit.stop.prevent="submitRegister">
            <h1 class="title">
                Post new product
                <i class="fas fa-plus"></i>
            </h1>
            <div class="notification is-danger" v-if="errors.length">
                <p id="error" v-for="error in errors" v-bind:key="error">
                    {{ error }}
                </p>
            </div>
            <div class="field">
                <label class="label">Name</label>
                <div class="control has-icons-left">
                    <input class="input" type="text" v-model="username" />
                    <span class="icon is-small is-left">
                        <i class="fas fa-heading"></i>
                    </span>
                </div>
            </div>

            <div class="field">
                <label class="label">Price</label>
                <div class="control has-icons-left">
                    <input
                        style="width: 50%"
                        class="input"
                        type="text"
                        v-model="email"
                    />
                    <span class="icon is-small is-left">
                        <i class="fas fa-euro-sign"></i>
                    </span>
                </div>
            </div>

            <div class="field">
                <label class="label">Location</label>
                <div class="control has-icons-left">
                    <div class="select">
                        <select>
                            <option>Select country</option>
                            <option>With options</option>
                        </select>
                    </div>
                    <span class="icon is-small is-left">
                        <i class="fas fa-map-marker-alt"></i>
                    </span>
                </div>
            </div>

            <div class="field">
                <span class="label">Description</span>
                <div class="control">
                    <textarea
                        class="textarea"
                        type="text"
                        v-model="password2"
                    ></textarea>
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <button class="button is-link">Create</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import { toast } from "bulma-toast";
export default {
    name: "Create",
    data() {
        return {
            username: "",
            email: "",
            password1: "",
            password2: "",
            errors: [],
        };
    },
    methods: {
        submitRegister() {
            let user = {
                username: this.username,
                email: this.email,
                password1: this.password1,
                password2: this.password2,
            };
            djangoAPI
                .post("/accounts/register/", user)
                .then((registerResponse) => {
                    console.log(registerResponse);
                    toast({
                        message: "Account was successfully created!",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                    this.$router.push("/");
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
        document.title = "Register | MechMarketEU";
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
