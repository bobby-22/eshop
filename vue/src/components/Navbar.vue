<template>
    <nav class="navbar is-light" style="background-color:#f2f2f2; box-shadow: rgba(0, 0, 0, 0.1) 0px 3px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;">
        <div class="navbar-brand" style="margin:0px;">
            <router-link style="border-top-left-radius:10px; border-bottom-left-radius:10px;" to="/" class="navbar-item"><strong>MechMarketEU</strong></router-link>
            <router-link to="/latest-products" class="navbar-item">Latest</router-link>
            <NavbarDropdown  class="navbar-item"/>
            <div class="navbar-burger" data-target="collapse_burger" v-on:click="collapseHamburger" v-bind:class="{'is-active': collapseBoolean}">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>

        <div class="navbar-menu" id="collapse_burger" v-bind:class="{'is-active': collapseBoolean}">
            <div class="navbar-end">
                <router-link to="/log-in" class="navbar-item">Log in</router-link>
                <div class="navbar-item" style="margin-right:7px">
                    <router-link to="/sign-up" class="button is-info">Sign up</router-link>
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

<style scoped>
.navbar.is-light {
    border-radius: 10px;
    margin-top: 15px;
}
.button.is-warning {
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 0px;
    border-top-left-radius: 0px;
}
.button.is-info {
    border-radius: 0px;
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
