import { createWebHistory, createRouter } from "vue-router";

import login from '@/page/cr-login.vue';
import main from '@/page/cr-main.vue';
import chat from '@/page/cr-room.vue';

const routes = [
  {
      path: "/",
      component:login
  },
  {
      path: "/main",
      component:main
  },
  {
      path: "/chat",
      component:chat
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to,from,next)=>{
  next();
})

export default router;