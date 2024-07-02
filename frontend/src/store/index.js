import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate";


export default createStore({
  plugins: [createPersistedState()],
  state: {
    style: {},
    token: '',
    email: '',
    password: '',
    userId: '',
    loggedIn: false,
    lastPage: '',
    index: [],
    pies: ''

  },
  mutations: {
    saveStyle(state, style){
      state.style = style;
    },
    saveToken(state, token){
      state.token = token;
    },
    saveEmail(state, email){
      state.email = email;
    },
    savePassword(state, password){
      state.password = password;
    },
    removeCredentialsUser(state){
      state.email = '';
      state.password = '';
    },
    saveUserId(state, userId){
      state.userId = userId;
    },
    logIn(state){
      state.loggedIn = true;
    },
    logOut(state){
      state.loggedIn = false;
    },
    saveLastPage(state,lastPage){
      state.lastPage=lastPage
    },
    saveIndex(state, index){
      state.index=index;
    },
    savePies(state, pies){
      state.pies= pies;
    }
  },
  actions: {
    saveStyle({commit},style){
      commit("saveStyle", style)
    },
    saveToken({commit}, token){
      commit("saveToken", token);
    },
    saveEmail({commit}, email){
      commit("saveEmail", email);
    },
    savePassword({commit}, password){
      commit("savePassword", password);
    },
    removeCredentialsUser({commit}){
      commit("removeCredentialsUser");
    },
    saveUserId({commit}, userId) {
      commit("saveUserId", userId);
    },
    logIn({commit}){
      commit("logIn");
    },
    logOut({commit}){
      commit("logOut");
    },
    saveLastPage({commit},lastPage){
      commit("saveLastPage",lastPage)
    },
    saveIndex({commit}, index){
      commit("saveIndex", index)
    },
    savePies({commit}, pies){
      commit("savePies", pies)
    }
  },
  modules: {
  }
})
