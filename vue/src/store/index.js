import { createStore } from 'vuex'

export default createStore({
  state: {
    bookmark: {
      items: [],
    },
  },
  mutations: {
    localStorageManipulation(state) {
      if (localStorage.getItem("bookmark")) {
        state.bookmark = JSON.parse(localStorage.getItem("bookmark"))
      } else {
        localStorage.setItem("bookmark", JSON.stringify(state.bookmark))
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
