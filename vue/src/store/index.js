import { createStore } from 'vuex'

export default createStore({
  state: {
    bookmark: {
      items: [],
    },
    tokenAccess: "",
    tokenRefresh: ""
  },
  mutations: {
    localStorageBookmark(state) {
      if (localStorage.getItem("bookmark")) {
        state.bookmark = JSON.parse(localStorage.getItem("bookmark"))
      } else {
        localStorage.setItem("bookmark", JSON.stringify(state.bookmark))
      }
    },
    localStorageToken(state) {
      if (localStorage.getItem("tokenAccess")) {
        state.tokenAccess = JSON.parse(localStorage.getItem("tokenAccess"))
      } else {
        localStorage.setItem("tokenAccess", JSON.stringify(state.tokenAccess))
      }
    },
    addToBookmark(state, item) {
      state.bookmark.items.push(item)
      localStorage.setItem("bookmark", JSON.stringify(state.bookmark))
    }
  },
  actions: {
  },
  modules: {
  }
})
