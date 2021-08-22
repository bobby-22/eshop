<template>
    <div class="dropdown is-hoverable">
        <div class="dropdown-trigger">
            <span>Category</span>
            <i class="fas fa-angle-down"></i>
        </div>

        <div class="dropdown-menu">
            <router-link v-bind:to="{name: 'Category', params: { category_id: 1 }}" class="dropdown-item" id="first">
                Cables
            </router-link>
            <hr class="dropdown-divider">
            <router-link v-bind:to="{name: 'Category', params: { category_id: 2 }}" class="dropdown-item">
                Deskmats
            </router-link>
            <hr class="dropdown-divider">
            <router-link v-bind:to="{name: 'Category', params: { category_id: 3 }}" class="dropdown-item">
                Keyboards
            </router-link>
            <hr class="dropdown-divider">
            <router-link v-bind:to="{name: 'Category', params: { category_id: 4 }}" class="dropdown-item">
                Keycaps
            </router-link>
            <hr class="dropdown-divider">
            <router-link v-bind:to="{name: 'Category', params: { category_id: 5 }}" class="dropdown-item">
                Switches
            </router-link>
            <hr class="dropdown-divider">
            <router-link v-bind:to="{name: 'Category', params: { category_id: 6 }}" class="dropdown-item" id="last">
                Others
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: "NavbarDropdown"
}
</script>

<style lang="scss" scoped>
$dropdown-menu-background-color: white;
.dropdown-menu {
    border-radius: 10px;
    box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.20);
    background-color: $dropdown-menu-background-color;
    padding: 0px;
}
.dropdown-divider {
    margin: 0px;
}
#first {
    border-top-right-radius:10px;
    border-top-left-radius:10px;
}
#last {
    border-bottom-right-radius:10px;
    border-bottom-left-radius:10px;
}
.fas {
    margin-left: 3px;
}
</style>
