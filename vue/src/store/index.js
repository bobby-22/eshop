import { createStore } from "vuex";
import { djangoAPI } from "../axios";

export default createStore({
    state: {
        savedProducts: {
            items: [],
        },
        authenticated: false,
        tokenAccess: null,
        tokenRefresh: null,
        currentUser: "",
    },
    mutations: {
        localStorageSavedProducts(state) {
            if (localStorage.getItem("savedProducts")) {
                state.savedProducts = JSON.parse(
                    localStorage.getItem("savedProducts")
                );
            } else {
                localStorage.setItem(
                    "savedProducts",
                    JSON.stringify(state.savedProducts)
                );
            }
        },
        saveProductState(state, item) {
            state.savedProducts.items.push(item);
            localStorage.setItem(
                "savedProducts",
                JSON.stringify(state.savedProducts)
            );
        },
        localStorageAuthenticated(state) {
            if (localStorage.getItem("authenticated")) {
                state.authenticated = JSON.parse(
                    localStorage.getItem("authenticated")
                );
            } else {
                localStorage.setItem(
                    "authenticated",
                    JSON.stringify(state.authenticated)
                );
            }
        },
        authenticate(state) {
            state.authenticated = !state.authenticated;
            localStorage.setItem(
                "authenticated",
                JSON.stringify(state.authenticated)
            );
        },
        localStorageSavedTokens(state) {
            if (localStorage.getItem("tokenAccess")) {
                state.tokenAccess = JSON.parse(
                    localStorage.getItem("tokenAccess")
                );
                state.tokenRefresh = JSON.parse(
                    localStorage.getItem("tokenRefresh")
                );
            } else {
                localStorage.setItem(
                    "tokenAccess",
                    JSON.stringify(state.tokenAccess)
                );
                localStorage.setItem(
                    "tokenRefresh",
                    JSON.stringify(state.tokenRefresh)
                );
            }
        },
        saveTokenAccessState(state, access) {
            state.tokenAccess = access;
            localStorage.setItem(
                "tokenAccess",
                JSON.stringify(state.tokenAccess)
            );
        },
        saveTokenRefreshState(state, refresh) {
            state.tokenRefresh = refresh;
            localStorage.setItem(
                "tokenRefresh",
                JSON.stringify(state.tokenRefresh)
            );
        },
        localStorageSavedCurrentUser(state) {
            if (localStorage.getItem("currentUser")) {
                state.currentUser = JSON.parse(
                    localStorage.getItem("currentUser")
                );
            } else {
                localStorage.setItem(
                    "currentUser",
                    JSON.stringify(state.currentUser)
                );
            }
        },
        saveCurrentUserState(state, currentUser) {
            state.currentUser = currentUser;
            localStorage.setItem(
                "currentUser",
                JSON.stringify(state.currentUser)
            );
        },
        removeCredentialsState(state) {
            state.authenticated = false;
            state.tokenAccess = null;
            state.tokenRefresh = null;
            state.currentUser = "";
            localStorage.setItem(
                "authenticated",
                JSON.stringify(state.authenticated)
            );
            localStorage.setItem(
                "tokenAccess",
                JSON.stringify(state.tokenAccess)
            );
            localStorage.setItem(
                "tokenRefresh",
                JSON.stringify(state.tokenRefresh)
            );
            localStorage.setItem(
                "currentUser",
                JSON.stringify(state.currentUser)
            );
        },
    },
    modules: {},
});
