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
        localStorageSavedTokens(state) {
            if (localStorage.getItem("tokenAccess")) {
                state.tokenAccess = JSON.parse(
                    localStorage.getItem("tokenAccess")
                );
            } else {
                localStorage.setItem(
                    "tokenAccess",
                    JSON.stringify(state.tokenAccess)
                );
            }
        },
        authenticated(state) {
            state.authenticated = !state.authenticated
        },
        saveTokenState(state, { access, refresh }) {
            state.tokenAccess = access;
            state.tokenRefresh = refresh;
            localStorage.setItem(
                "tokenAccess",
                JSON.stringify(state.tokenAccess)
            );
            localStorage.setItem(
                "tokenRefresh",
                JSON.stringify(state.tokenRefresh)
            );
        },
        removeTokenState(state) {
            state.tokenAccess = null;
            state.tokenRefresh = null;
            localStorage.setItem(
                "tokenAccess",
                JSON.stringify(state.tokenAccess)
            );
            localStorage.setItem(
                "tokenRefresh",
                JSON.stringify(state.tokenRefresh)
            );
        },
    },
    modules: {},
});
