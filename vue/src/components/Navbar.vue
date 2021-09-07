<template>
    <nav class="navbar is-light">
        <div class="navbar-brand" style="margin: 0px">
            <router-link to="/" class="navbar-item" id="brand">
                <strong>MechMarketEU</strong>
            </router-link>
            <router-link to="/products/latest" class="navbar-item"
                >Latest</router-link
            >
            <NavbarDropdown class="navbar-item" />
            <div
                class="navbar-burger"
                data-target="hamburger"
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
            id="collapse_burger"
            v-bind:class="{ 'is-active': hamburgerBoolean }"
        >
            <div class="navbar-start">
                <div class="navbar-item">
                    <form v-on:submit.stop.prevent="submitSearch">
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
                                user: currentUser,
                            },
                        }"
                        >&nbsp;{{ currentUser }}
                    </router-link>
                </span>
                <router-link to="/products/savedProducts" class="navbar-item">
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
                    >Log in</router-link
                >
                <router-link to="/products/savedProducts" class="navbar-item">
                    <span class="fas fa-bookmark">
                        <span class="counter">{{ bookmarkLength }}</span>
                    </span>
                </router-link>
                <div class="navbar-item" id="button-area">
                    <router-link to="/accounts/register" class="button is-info"
                        >Register</router-link
                    >
                    <router-link to="/" class="button is-warning"
                        >Donate</router-link
                    >
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import NavbarDropdown from "./NavbarDropdown";
export default {
    name: "Navbar",
    components: {
        NavbarDropdown,
    },
    data() {
        return {
            hamburgerBoolean: false,
            savedProducts: {
                items: [],
            },
            keyword: null,
            authenticated: this.$store.state.authenticated,
            currentUser: this.$store.state.currentUser,
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
        },
    },
    computed: {
        bookmarkLength() {
            let length = this.savedProducts.items.length;
            return length;
        },
    },
    beforeCreate() {
        this.$store.commit("localStorageSavedProducts");
        this.$store.commit("localStorageSavedCurrentUser");
        this.$store.commit("localStorageAuthenticated");
    },
    created() {
        this.savedProducts = this.$store.state.savedProducts;
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
$navbar-background-color: #f8f8f8;
$counter-color: #c9a0ff;
.navbar.is-light {
    box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px,
        rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;
    border-radius: 15px;
    background: $navbar-background-color;
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
#profile, #profile:hover {
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
.counter {
    position: absolute;
    bottom: 50%;
    left: 50%;
    border-radius: 50%;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 700;
    font-size: 11px;
    background: $counter-color;
    padding: 3px;
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
