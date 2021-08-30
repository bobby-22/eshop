<template>
    <div class="container" v-on:submit.stop.prevent="submitLogin">
        <form class="form">
            <h1 class="title">
                Login
                <i class="far fa-user-circle"></i>
            </h1>
            <div class="notification is-danger" v-if="error">
                <p id="error">Incorrect username or password</p>
            </div>
            <div class="field">
                <p class="control has-icons-left">
                    <input
                        class="input"
                        type="text"
                        placeholder="Username"
                        v-model="username"
                    />
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
                        v-model="password"
                    />
                    <span class="icon is-small is-left">
                        <i class="fas fa-lock"></i>
                    </span>
                </p>
            </div>
            <div class="field">
                <p class="control">
                    <button class="button is-success">Login</button>
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
            error: false,
        };
    },
    methods: {
        submitLogin() {
            djangoAPI
                .post("/accounts/login/", {
                    username: this.username,
                    password: this.password,
                })
                .then((loginResponse) => {
                    console.log(loginResponse);
                    this.$store.commit(
                        "saveTokenAccessState",
                        loginResponse.data.access
                    );
                    this.$store.commit(
                        "saveTokenRefreshState",
                        loginResponse.data.refresh
                    );
                    this.$store.commit("authenticated");
                    this.$router.push("/");
                    toast({
                        message: "You were successfully logged in!",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                })
                .catch((error) => {
                    console.log(error)
                    if (error) {
                        this.error = true;
                    }
                });
        },
    },
    created() {
        document.title = "Login | MechMarketEU";
    },
};
</script>

<style lang="scss" scoped>
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
</style>
