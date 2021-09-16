<template>
    <nav class="navbar is-light">
        <div class="navbar-brand" style="margin: 0px">
            <router-link to="/" class="navbar-item" id="brand">
                <strong>MechMarketEU</strong>
            </router-link>
            <router-link to="/posts/latest" class="navbar-item"
                >Latest</router-link
            >
            <NavbarDropdown class="navbar-item" />
            <div
                class="navbar-burger"
                v-on:click="openHamburger"
                v-bind:class="{ 'is-active': hamburgerBoolean }"
            >
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>

        <div
            class="navbar-menu"
            v-bind:class="{ 'is-active': hamburgerBoolean }"
        >
            <div class="navbar-start">
                <div class="navbar-item">
                    <form @submit.prevent="submitSearch">
                        <div class="field has-addons">
                            <div class="control">
                                <input
                                    class="input"
                                    type="text"
                                    placeholder="Search..."
                                    v-model="keyword"
                                />
                            </div>
                            <div class="control">
                                <button class="button is-danger" type="submit">
                                    <i class="fas fa-search"></i>
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <div class="navbar-end" v-if="authenticated">
                <span class="navbar-item"
                    >Hello,
                    <router-link
                        id="profile"
                        v-bind:to="{
                            name: 'Profile',
                            params: {
                                profile: currentUser,
                            },
                        }"
                        >&nbsp;{{ currentUser }}
                    </router-link>
                </span>
                <router-link to="/posts/saved" class="navbar-item">
                    <span class="fas fa-bookmark">
                        <span class="counter">{{ bookmarkLength }}</span>
                    </span>
                </router-link>
                <div class="navbar-item" id="button-area">
                    <span class="button is-info" v-on:click="logoutUser"
                        >Logout</span
                    >
                    <router-link to="/" class="button is-warning"
                        >Donate</router-link
                    >
                </div>
            </div>
            <div class="navbar-end" v-else>
                <router-link to="/accounts/login" class="navbar-item"
                    >Login</router-link
                >
                <router-link to="/posts/saved" class="navbar-item">
                    <span class="fas fa-bookmark">
                        <span class="counter">{{ bookmarkLength }}</span>
                    </span>
                </router-link>
                <div class="navbar-item" id="button-area">
                    <router-link to="/accounts/register" class="button is-info"
                        >Register</router-link
                    >
                    <span class="button is-warning" v-on:click="donate"
                        >Donate</span
                    >
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import NavbarDropdown from "./NavbarDropdown";
import { toast } from "bulma-toast";
import { djangoAPI } from "../axios";
export default {
    name: "Navbar",
    components: {
        NavbarDropdown,
    },
    data() {
        return {
            savedProducts: this.$store.state.savedProducts,
            authenticated: this.$store.state.authenticated,
            currentUser: this.$store.state.currentUser,
            keyword: null,
            hamburgerBoolean: false,
        };
    },
    methods: {
        openHamburger() {
            this.hamburgerBoolean = !this.hamburgerBoolean;
        },
        submitSearch() {
            this.$router.push({
                name: "Search",
                params: { keyword: this.keyword },
            });
        },
        logoutUser() {
            this.$store.commit("removeCredentialsState");
            this.$router.push("/accounts/login");
            toast({
                message: "You have been successfully logged out!",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: "bottom-right",
            });
        },
        donate() {
            djangoAPI
                .get("/api/v1/donate")
                .then((donateResponse) => {
                    console.log(donateResponse);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    computed: {
        bookmarkLength() {
            let length = this.$store.state.savedProducts.length;
            return length;
        },
    },
    beforeCreate() {
        this.$store.commit("localStorageSavedProducts");
        this.$store.commit("localStorageSavedCurrentUser");
        this.$store.commit("localStorageAuthenticated");
    },
    watch: {
        "$store.state.authenticated": function () {
            this.authenticated = !this.authenticated;
        },
        "$store.state.currentUser": function () {
            this.currentUser = this.$store.state.currentUser;
        },
    },
};
</script>

<style lang="scss" scoped>
.navbar.is-light {
    box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px,
        rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;
    border-radius: 15px;
    background: #f8f8f8;
    margin-top: 15px;
}
#brand {
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
}
.navbar-start {
    flex-grow: 1;
    justify-content: center;
    align-items: center;
}
.input,
.button.is-danger {
    border-radius: 15px;
}
#profile,
#profile:hover {
    color: black;
}
#button-area {
    margin-right: 7px;
}
.button {
    &.is-warning {
        border-top-right-radius: 10px;
        border-bottom-right-radius: 10px;
        border-bottom-left-radius: 0px;
        border-top-left-radius: 0px;
    }
    &.is-info {
        border-radius: 0px;
    }
}
.fas.fa-bookmark {
    font-size: 20px;
    position: relative;
}
.fas.fa-bookmark::before {
    color: #4a4a4a;
}
.counter {
    position: absolute;
    bottom: 50%;
    left: 50%;
    border-radius: 50%;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 600;
    font-size: 12px;
    background: #c9a0ff;
    color: #616161;
    width: 20px;
    height: 20px;
    line-height: 20px;
    text-align: center;
}
@media (max-width: 1024px) {
    .navbar.is-light {
        border-radius: 0px;
        margin-top: 0px;
        padding-left: 0px;
        padding-right: 0px;
    }
    #brand {
        border-top-left-radius: 0px;
        border-bottom-left-radius: 0px;
    }
    .button.is-warning {
        border-top-right-radius: 0px;
        border-bottom-right-radius: 0px;
    }
}
</style>
