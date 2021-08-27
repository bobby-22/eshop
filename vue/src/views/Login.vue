<template>
    <div class="container" v-on:submit.stop.prevent="submitLogin">
        <form class="form">
            <h1 class="title">
                Login
                <i class="far fa-user-circle"></i>
            </h1>
            <div class="notification is-danger" v-if="errors.length">
                <p id="error" v-for="error in errors" v-bind:key="error">
                    {{ error }}
                </p>
            </div>
            <div class="field">
                <p class="control has-icons-left">
                    <input class="input" type="text" placeholder="Username" />
                    <span class="icon is-small is-left">
                        <i class="fas fa-user"></i>
                    </span>
                </p>
            </div>
            <div class="field">
                <p class="control has-icons-left">
                    <input
                        class="input"
                        type="password"
                        placeholder="Password"
                    />
                    <span class="icon is-small is-left">
                        <i class="fas fa-lock"></i>
                    </span>
                </p>
            </div>
            <div class="field">
                <p class="control">
                    <button class="button is-success">
                        Login
                    </button>
                </p>
            </div>
        </form>
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import { toast } from "bulma-toast";
export default {
    name: "Login",
    data() {
        return {
            username: "",
            password: "",
            errors: [],
        };
    },
    methods: {
        submitLogin() {
            let user = {
                username: this.username,
                password: this.password,
            };
            djangoAPI
                .post("/accounts/login/", user)
                .then((loginResponse) => {
                    console.log(loginResponse);
                    toast({
                        message: "You have been successfully logged in!",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                    this.$router.push("/");
                })
                .catch((error) => {
                    this.errors.splice(0, this.errors.length);
                    for (let property in error.response.data) {
                        this.errors.push(`${error.response.data[property]}`);
                    }
                });
        },
    },
};
</script>

<style lang="scss" scoped>
.container {
    min-height: 100%;
    display: flex;
    justify-content: space-around;
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
</style>
