import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from './components/Dashboard.vue';
import error404 from './components/error404.vue'

import store from "./store"; 


const routes = [
    {
        path: '/',
        name: 'dashboard',
        component: Dashboard,
    },{
        path: '/error404',
        name: 'error404',
        component: error404,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })

router.beforeEach(async (to, from, next) => {
    store.dispatch("saveLastPage",from)
    let routesList = ['/','/error404']
    if (!routesList.includes(to.path)){
        next('/error404')
    }
/*     const publicPages = ['/login',"/register"];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = store.state.loggedIn; */
    next()
/*     if (!authRequired) {
        next()
    } else if (authRequired && !loggedIn) {
        next('/login');
    }else{
        next()
    } */

});


export default router;
