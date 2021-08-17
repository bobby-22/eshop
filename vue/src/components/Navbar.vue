<template>
    <nav class="navbar is-light">
        <div class="navbar-brand">
            <router-link style="border-top-left-radius:10px; border-bottom-left-radius:10px" to="/" class="navbar-item"><strong>MechMarketEU</strong></router-link>
            <router-link to="/latest-products" class="navbar-item">Latest</router-link>
            <NavbarDropdown  class="navbar-item"/>
            <div class="navbar-burger" data-target="collapse_burger" v-on:click="collapseHamburger()" v-bind:class="{'is-active': collapseBoolean}">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>

        <div class="navbar-menu" id="collapse_burger" v-bind:class="{'is-active': collapseBoolean}">
            <div class="navbar-end">
                <router-link to="/log-in" class="navbar-item">Log in</router-link>
                <router-link to="/sign-up" class="navbar-item">Sign up</router-link>
                <div class="navbar-item">
                    <router-link to="/donate" class="button is-warning">Donate</router-link>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import NavbarDropdown from "./NavbarDropdown"
export default {
    name: "Navbar",
    components: {
        NavbarDropdown
    },
    data() {
        return {
            collapseBoolean: false
        }
    },
    methods: {
        collapseHamburger() {
            this.collapseBoolean = !this.collapseBoolean
        }
    }
}
</script>

<style>
.navbar.is-light {
    border-radius: 10px;
    margin-top: 15px;
    padding-left: 10px;
    padding-right: 10px;
}
.button.is-warning {
    border-radius: 10px;
}
@media (max-width: 1024px) {
    .navbar.is-light {
        border-radius: 0px;
        margin-top: 0px;
        padding-left: 0px;
        padding-right: 0px;
    }
}
</style>
