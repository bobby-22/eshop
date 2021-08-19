import { createStore } from 'vuex'

export default createStore({
  state: {
    wish: {
      items: [],
    },
    isAuthenticated: false,
    token: "",
    isLoading: false
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("wish")) {
        state.wish = JSON.parse(localStorage.getItem("wish"))
      } else {
        localStorage.setItem("wish", JSON.stringify(state.wish))
      }
    },
    addToWish(state, item) {
      const exists = state.wish.items.filter(i => i.product.id === item.product.id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.wish.items.push(item)
      }
      localStorage.setItem("wish", JSON.stringify(state.wish))
    }
  },
  actions: {
  },
  modules: {
  }
})
