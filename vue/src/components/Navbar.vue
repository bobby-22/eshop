<template>
    <div id="container">
        <nav class="navbar is-light">
            <div class="navbar-brand">
                <router-link to="/" class="navbar-item"><strong>MechMarketEU</strong></router-link>
                <router-link to="/latest-products" class="navbar-item">Latest</router-link>
                <NavbarDropdown  class="navbar-item"/>
                <div class="navbar-burger" data-target="collapse_burger" v-on:click="collapse = !collapse">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>

            <div class="navbar-menu" id="collapse_burger" v-bind:class="{'is-active': collapse}">
                <div class="navbar-end">
                    <div class="navbar-item">
                        <router-link to="/log-in" class="button is-light">Log in</router-link>
                        <router-link to="/sign-up" class="button is-info">Sign up</router-link>
                        <router-link to="/donate" class="button is-warning">Donate</router-link>
                    </div>
                </div>
            </div>
        </nav>
        <section class="section">
            <router-view/>
        </section>
        <footer class="footer">
            <p class="has-text-centered">Copyright (C) 2021</p>
        </footer>
    </div>
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
            collapse: false
        }
    },
}
</script>

<style lang="scss">
@import "../../node_modules/bulma";
</style>
