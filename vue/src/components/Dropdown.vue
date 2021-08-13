<template>
    <div class="dropdown is-hoverable">
        <div class="dropdown-trigger" data-target="collapse_dropdown">
                <span>Category</span>
                <span class="icon is-small">
                    <i class="fas fa-angle-down"></i>
                </span>
        </div>
        <div class="dropdown-menu" id="collapse_dropdown">
            <div class="dropdown-content">
                <router-link to="/cables" class="dropdown-item">Cables</router-link>
                <router-link to="/deskmats" class="dropdown-item">Deskmats</router-link>
                <router-link to="/keyboards" class="dropdown-item">Keyboards</router-link>
                <router-link to="/keycaps" class="dropdown-item">Keycaps</router-link>
                <router-link to="/switches" class="dropdown-item">Switches</router-link>
                <router-link to="/other" class="dropdown-item">Other</router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Dropdown",
    data() {
        return {
            collapse: false
        }
    }
}
</script>

<style>
</style>
