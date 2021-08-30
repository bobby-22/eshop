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
                v-bind:to="{ name: 'Category', params: { category_id: 1 } }"
                >Cables</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{ name: 'Category', params: { category_id: 2 } }"
                >Cases</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{ name: 'Category', params: { category_id: 3 } }"
                >Deskmats</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{ name: 'Category', params: { category_id: 4 } }"
                >Keyboards</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{ name: 'Category', params: { category_id: 5 } }"
                >Keycaps</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{ name: 'Category', params: { category_id: 6 } }"
                >Others</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{ name: 'Category', params: { category_id: 7 } }"
                >PCBs</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{ name: 'Category', params: { category_id: 8 } }"
                >Plates</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{ name: 'Category', params: { category_id: 9 } }"
                >Switches</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                v-bind:to="{ name: 'Category', params: { category_id: 10 } }"
                >Travelling cases</router-link
            >
            <hr class="dropdown-divider" />
            <router-link
                class="dropdown-item"
                id="last"
                v-bind:to="{ name: 'Category', params: { category_id: 11 } }"
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

<style lang="scss" scoped>
$dropdown-menu-background-color: white;
.dropdown-menu {
    border-radius: 10px;
    box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.2);
    background: $dropdown-menu-background-color;
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
</style>
