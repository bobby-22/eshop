<template>
    <div class="container">
        <form class="form" v-on:submit.stop.prevent="submitRegister">
            <h1 class="title">
                Register
                <i class="fas fa-user-circle"></i>
            </h1>
            <div class="notification is-danger" v-if="errors.length">
                <p id="error" v-for="error in errors" v-bind:key="error">
                    {{ error }}
                </p>
            </div>
            <div class="field">
                <label class="label">Username</label>
                <div class="control has-icons-left">
                    <input
                        class="input"
                        type="text"
                        placeholder="example"
                        v-model="username"
                    />
                    <span class="icon is-small is-left">
                        <i class="fas fa-user"></i>
                    </span>
                </div>
            </div>

            <div class="field">
                <label class="label">Email</label>
                <div class="control has-icons-left">
                    <input
                        class="input"
                        type="email"
                        placeholder="example@example.com"
                        v-model="email"
                    />
                    <span class="icon is-small is-left">
                        <i class="fas fa-envelope"></i>
                    </span>
                </div>
            </div>

            <div class="field">
                <label class="label">Password</label>
                <div class="control has-icons-left">
                    <input
                        class="input"
                        type="password"
                        placeholder="supersecretpassword123"
                        v-model="password1"
                    />
                    <span class="icon is-small is-left">
                        <i class="fas fa-key"></i>
                    </span>
                </div>
            </div>

            <div class="field">
                <span class="label">Confirm password</span>
                <div class="control has-icons-left">
                    <input
                        class="input"
                        type="password"
                        placeholder="supersecretpassword123"
                        v-model="password2"
                    />
                    <span class="icon is-small is-left">
                        <i class="fas fa-key"></i>
                    </span>
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <span class="checkbox">
                        <input type="checkbox" />
                        <span id="terms"
                            >I agree to the
                            <a href="/">terms and conditions</a></span
                        >
                    </span>
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <button class="button is-link">Submit</button>
                </div>
            </div>
            <p>
                Already registered?
                <router-link to="/accounts/login">Login</router-link>
            </p>
        </form>
    </div>
</template>

<script>
import { djangoAPI } from "../axios";
import { toast } from "bulma-toast";
export default {
    name: "Register",
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
                .post("/api/v1/accounts/register/", user)
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

<style scoped>
.container {
    min-height: 100%;
    display: flex;
    justify-content: space-around;
    margin-top: 30px;
    margin-bottom: 30px;
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
.checkbox {
    display: flex;
    justify-content: center;
    align-items: center;
}
#terms {
    margin-left: 15px;
}
p {
    text-align: center;
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
