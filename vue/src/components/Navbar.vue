<template>
    <nav class="navbar is-light">
        <div class="navbar-brand" style="margin:0px;">
            <router-link to="/" class="navbar-item" style="border-top-left-radius:10px; border-bottom-left-radius:10px;"><strong>MechMarketEU</strong></router-link>
            <router-link to="/latest/" class="navbar-item">Latest</router-link>
            <NavbarDropdown  class="navbar-item"/>
            <div class="navbar-burger" data-target="collapse_burger" v-on:click="collapseHamburger" v-bind:class="{'is-active': collapseBoolean}">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>

        <div class="navbar-menu" id="collapse_burger" v-bind:class="{'is-active': collapseBoolean}">
            <div class="navbar-start">
                <div class="navbar-item">
                    <form method="post" action="/search">
                        <div class="field has-addons">
                            <div class="control">
                                <input type="text" class="input" placeholder="Search..." name="query">
                            </div>
                            <div class="control">
                                <a href="" class="button is-danger">
                                    <i class="fas fa-search"></i>
                                </a>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <div class="navbar-end">
                <router-link to="/" class="navbar-item">Log in</router-link>
                <router-link to="/" class="navbar-item">
                    <span class="fas fa-bookmark" >
                        <span class="counter">{{ wishLength }}</span>
                    </span>
                </router-link>
                <div class="navbar-item" style="margin-right:7px;">
                    <router-link to="/" class="button is-info">Sign up</router-link>
                    <router-link to="/" class="button is-warning">Donate</router-link>
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
            collapseBoolean: false,
            wish: {
                items: []
            }
        }
    },
    methods: {
        collapseHamburger() {
            this.collapseBoolean = !this.collapseBoolean
        }
    },
    computed: {
        wishLength() {
            let length = 0
            for (let i = 0; i < this.wish.items.length; i++) {
                length += this.wish.items[i].quantity
            }
            return length
        }
    },
    beforeCreate() {
        this.$store.commit("initializeStore")
    },
    mounted() {
        this.wish = this.$store.state.wish
    }
}
</script>

<style lang="scss" scoped>
$counter-color: #c9a0ff;
.navbar.is-light {
    box-shadow: rgba(0, 0, 0, 0.1) 0px 2px 4px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;
    border-radius: 10px;
    margin-top: 15px;
}
.navbar-start {
    flex-grow: 1;
    justify-content: center;
    align-items: center;

}
.input, .button.is-danger {
    border-radius: 10px;
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
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
}
</style>
