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
      {path:"/",name:"gloab",component:()=>import("@/views/apiView/baseData.vue")},

      {path:"/project",name:'project',component:()=>import("@/views/apiView/project.vue")},
      {path:"/model",name:'model',component:()=>import("@/views/apiView/model.vue")},
      {path:"/caselist",name:'caselist',component:()=>import("@/views/apiView/api_list.vue")},
      {path:"/case",name:'case',component:()=>import("@/views/apiView/case.vue")},
      {path:"/tasklist",name:"tasklist",component:()=>import("@/views/apiView/task_list.vue")},
      {path:"/report",name:"report",component:()=>import("@/views/apiView/report_list.vue")},
      {path:"/detail",name:"detail",component:()=>import("@/views/apiView/detailReport_list.vue")},
      {path:"/gloab",name:"gloab",component:()=>import("@/views/apiView/gloab_list.vue")},
      {path:"/env",name:"env",component:()=>import("@/views/apiView/env.vue")},
      {path:"/envList",name:"envList",component:()=>import("@/views/apiView/env_list.vue")},
      {path:"/reportList",name:"reportList",component:()=>import("@/views/apiView/report.vue")},

    ]
    
  },
  {path:"/login",name:"login",component:()=>import("@/views/apiView/login.vue")}


];

const router = new VueRouter({
  // mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
