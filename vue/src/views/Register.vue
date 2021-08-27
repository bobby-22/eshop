<template>
<form class="container" @submit.stop.prevent="submitRegister">
    <h1 class="title">
        Register
        <i class="fas fa-user-circle"></i>
    </h1>
    <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
    </div>
    <div class="field">
        <label class="label">Username</label>
        <div class="control has-icons-left has-icons-right">
            <input class="input" type="text" placeholder="example" v-model="username">
            <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
            </span>
        </div>
    </div>

    <div class="field">
        <span class="label">Email</span>
        <div class="control has-icons-left">
            <input class="input" type="email" placeholder="example@example.com" v-model="email">
            <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
            </span>
        </div>
    </div>

    <div class="field">
        <span class="label">Password</span>
        <div class="control has-icons-left">
            <input class="input" type="password" placeholder="supersecretpassword123" v-model="password1">
            <span class="icon is-small is-left">
                <i class="fas fa-key"></i>
            </span>
        </div>
    </div>

    <div class="field">
        <span class="label">Confirm password</span>
        <div class="control has-icons-left">
            <input class="input" type="password" placeholder="supersecretpassword123" v-model="password2">
            <span class="icon is-small is-left">
                <i class="fas fa-key"></i>
            </span>
        </div>
    </div>

    <div class="field">
        <div class="control">
            <span class="checkbox">
                <input type="checkbox">
                I agree to the <a href="/">terms and conditions</a>
            </span>
        </div>
    </div>

    <div class="field">
        <div class="control">
            <button class="button is-link">Submit</button>
        </div>
    </div>
    <div class="section">
        <p>
            Already registered?
            <router-link to="/accounts/login">Login</router-link>
        </p>
    </div>
</form>
</template>

<script>
import { djangoAPI } from "../axios"
import { toast } from "bulma-toast"
export default {
    name: "Register",
    data() {
        return {
            username: "",
            email: "",
            password1: "",
            password2: "",
            errors: []
        }
    },
    methods: {
        submitRegister() {
            let user = {
                username: this.username,
                email: this.email,
                password1: this.password1,
                password2: this.password2
            }
            djangoAPI
                .post("/accounts/register/", user)
                .then(registerResponse => {
                    console.log(registerResponse)
                    toast({
                        message: "Account was successfully created!",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right"
                    })
                    this.$router.push("/")
                })
                .catch(error => {
                    this.errors.splice(0, this.errors.length)
                    for (let property in error.response.data) {
                        this.errors.push(`${error.response.data[property]}`)
                    }
                })
        }
    }
}
</script>

<style lang="scss" scoped>
.container {
    min-height: 100%;
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
    border-radius: 5px;
    margin-top: 30px;
    margin-bottom: 30px;
    padding: 30px;
}
.title {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.checkbox {
  color: black;
}
</style>
