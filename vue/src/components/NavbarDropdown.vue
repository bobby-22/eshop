<template>
    <div class="dropdown is-hoverable">
        <div class="dropdown-trigger">
            <span>Category</span>
            <i class="fas fa-angle-down"></i>
        </div>

        <div class="dropdown-menu">
            <router-link
                class="dropdown-item"
                id="first"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'Cables', page: 1 },
                }"
                >Cables</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'Cases', page: 1 },
                }"
                >Cases</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'Deskmats', page: 1 },
                }"
                >Deskmats</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'Keyboards', page: 1 },
                }"
                >Keyboards</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'Keycaps', page: 1 },
                }"
                >Keycaps</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'Others', page: 1 },
                }"
                >Others</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'PCBs', page: 1 },
                }"
                >PCBs</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'Plates', page: 1 },
                }"
                >Plates</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'Switches', page: 1 },
                }"
                >Switches</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'Travelling-Cases', page: 1 },
                }"
                >Travelling cases</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                id="last"
                v-bind:to="{
                    name: 'Category',
                    params: { category: 'Wrist-rests', page: 1 },
                }"
                >Wrist-rests</router-link
            >
        </div>
    </div>
</template>

<script>
export default {
    name: "NavbarDropdown",
};
</script>

<style scoped>
.dropdown-menu {
    border-radius: 10px;
    box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.2);
    background: white;
    padding: 0px;
}
.dropdown-divider {
    margin: 0px;
}
#first {
    border-top-right-radius: 10px;
    border-top-left-radius: 10px;
}
#last {
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
}
.fas {
    margin-left: 3px;
}
a:link,
a:visited,
a:active,
a:hover {
    color: inherit;
}
</style>
