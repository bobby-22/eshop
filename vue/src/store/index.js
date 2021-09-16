import { createStore } from "vuex";
import { djangoAPI } from "../axios";

export default createStore({
    state: {
        productData: Object,
        imagesCloud: [],
        savedProducts: [],
        authenticated: false,
        tokenAccess: null,
        tokenRefresh: null,
        currentUser: null,
    },
    mutations: {
        localStorageProductData(state) {
            if (localStorage.getItem("productData")) {
                state.productData = JSON.parse(
                    localStorage.getItem("productData")
                );
            } else {
                localStorage.setItem(
                    "productData",
                    JSON.stringify(state.productData)
                );
            }
        },
        saveProductDataState(state, product) {
            state.productData = product;
            localStorage.setItem(
                "productData",
                JSON.stringify(state.productData)
            );
        },
        localStorageProductImages(state) {
            if (localStorage.getItem("imagesCloud")) {
                state.imagesCloud = JSON.parse(
                    localStorage.getItem("imagesCloud")
                );
            } else {
                localStorage.setItem(
                    "imagesCloud",
                    JSON.stringify(state.imagesCloud)
                );
            }
        },
        saveImagesCloudState(state, images) {
            state.imagesCloud = images;
            localStorage.setItem(
                "imagesCloud",
                JSON.stringify(state.imagesCloud)
            );
        },
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
        saveProductState(state, product) {
            state.savedProducts.push(product);
            localStorage.setItem(
                "savedProducts",
                JSON.stringify(state.savedProducts)
            );
        },
        updateSavedProductsState(state, product) {
            state.savedProducts = state.savedProducts.filter((i) => {
                return i.post_id !== product.post_id;
            });
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
            state.productData = null;
            state.imagesCloud = [];
            state.authenticated = false;
            state.tokenAccess = null;
            state.tokenRefresh = null;
            state.currentUser = null;
            localStorage.setItem(
                "productData",
                JSON.stringify(state.productData)
            );
            localStorage.setItem(
                "imagesCloud",
                JSON.stringify(state.imagesCloud)
            );
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
