import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    children:[
      {path:"/project",name:'project',component:()=>import("@/views/apiView/project.vue")},
      {path:"/model",name:'model',component:()=>import("@/views/apiView/model.vue")},
      {path:"/caselist",name:'caselist',component:()=>import("@/views/apiView/api_list.vue")},
      {path:"/case",name:'case',component:()=>import("@/views/apiView/case.vue")},
    ]
  },

];

const router = new VueRouter({
  // mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
