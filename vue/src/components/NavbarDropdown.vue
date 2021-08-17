<template>
    <div class="dropdown is-hoverable">
        <div class="dropdown-trigger">
            <span>Category</span>
            <i class="fas fa-angle-down"></i>
        </div>

        <div class="dropdown-menu">
            <router-link to="/cables" class="dropdown-item">Cables</router-link>
            <hr class="dropdown-divider">
            <router-link to="/deskmats" class="dropdown-item">Deskmats</router-link>
            <hr class="dropdown-divider">
            <router-link to="/keyboards" class="dropdown-item">Keyboards</router-link>
            <hr class="dropdown-divider">
            <router-link to="/keycaps" class="dropdown-item">Keycaps</router-link>
            <hr class="dropdown-divider">
            <router-link to="/switches" class="dropdown-item">Switches</router-link>
            <hr class="dropdown-divider">
            <router-link style="border-bottom-right-radius:10px; border-bottom-left-radius:10px;" to="/other" class="dropdown-item">Others</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: "NavbarDropdown"
}
</script>

<style scoped>
.dropdown-menu {
    border-radius: 10px;
    box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.20);
    background-color: white;
    padding: 0px;
}
.dropdown-divider {
    margin: 0px;
}
.fas {
    margin-left: 3px;
}
</style>
