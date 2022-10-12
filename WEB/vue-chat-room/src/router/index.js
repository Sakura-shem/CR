import { createWebHistory, createRouter } from "vue-router";

import login from '@/page/cr-login.vue';
import main from '@/page/cr-main.vue';
// import aouth from '@/page/app-oauth.vue';
// import admin from '@/page/admin/admin-index.vue';
// import asset_in from '@/page/admin/info/asset-in.vue';
// import asset_state from '@/page/admin/info/asset-state.vue';
// import asset_out from '@/page/admin/info/record/asset-out.vue';
// import class_in from '@/page/admin/info/class-in.vue';
// import asset_log from '@/page/admin/info/log/asset-log.vue';
// import user_in from '@/page/admin/info/user-in.vue';
// import Err_404 from '@/page/v-404.vue';
// import VFAIL from '@/page/v-fail.vue';

const routes = [
  {
      path: "/",
      component:login
  },
  {
      path: "/chat",
      component:main
  }
//   {
//     path: "/oauth",
//     component:aouth
//   },
//   {
//     path: "/admin",
//     name: "admin",
//     component: admin,
//     children:[
//       {
//         path: "/asset",
//         name: "asset_in",
//         component: asset_in,
//       },{
//         path: "/asset-state",
//         name: "asset_state",
//         component: asset_state,
//       },{
//         path: "/asset-out",
//         name: "asset_out",
//         component: asset_out,
//       },{
//           path: "/class",
//           name: "class_in",
//           component: class_in,
//       },{
//         path: "/asset-log",
//         name: "asset_log",
//         component: asset_log,
//       },{
//         path: "/user",
//         name: "user_in",
//         component: user_in,
//       }
//     ]
//   },
//   {
//     path: "/404",
//     name:"404",
//     component:Err_404
//   },
//   {
//     path: "/fail",
//     name:"fail",
//     component:VFAIL
//   }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to,from,next)=>{
  next();
})

export default router;