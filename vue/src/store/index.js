import { createStore } from "vuex";
import { djangoAPI } from "../axios";

export default createStore({
    state: {
        savedProducts: [],
        productData: Object,
        imagesCloud: [],
        authenticated: false,
        tokenAccess: null,
        tokenRefresh: null,
        currentUser: "",
        currentUserId: null,
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
        saveProductState(state, product) {
            state.savedProducts.push(product);
            localStorage.setItem(
                "savedProducts",
                JSON.stringify(state.savedProducts)
            );
        },
        updateSavedProductsState(state, product) {
            state.savedProducts = state.savedProducts.filter((i) => {
                return i.stripe_product_id !== product.stripe_product_id;
            });
            localStorage.setItem(
                "savedProducts",
                JSON.stringify(state.savedProducts)
            );
        },
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
        localStorageSavedCurrentUserId(state) {
            if (localStorage.getItem("currentUserId")) {
                state.currentUserId = JSON.parse(
                    localStorage.getItem("currentUserId")
                );
            } else {
                localStorage.setItem(
                    "currentUserId",
                    JSON.stringify(state.currentUserId)
                );
            }
        },
        saveCurrentUserIdState(state, currentUserId) {
            state.currentUserId = currentUserId;
            localStorage.setItem(
                "currentUserId",
                JSON.stringify(state.currentUserId)
            );
        },
        removeCredentialsState(state) {
            state.authenticated = false;
            state.tokenAccess = null;
            state.tokenRefresh = null;
            state.currentUser = "";
            state.currentUserId = null;
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
            localStorage.setItem(
                "currentUserId",
                JSON.stringify(state.currentUserId)
            );
        },
    },
    modules: {},
});
