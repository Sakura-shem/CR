import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import state from './state';
import axios from 'axios';
import { ElInput,ElButton,ElIcon,ElScrollbar,ElCard,ElNotification,ElMessage } from 'element-plus';
import 'element-plus/dist/index.css';

const app = createApp(App);

app.config.globalProperties.$axios=axios;
app.config.globalProperties.$log=ElNotification;
app.config.globalProperties.$message=ElMessage;
axios.defaults.headers.common['Content-Type'] = 'application/json;charset=UTF-8';

app
    .use(router)
    .use(state)
    .use(ElInput)
    .use(ElButton)
    .use(ElIcon)
    .use(ElScrollbar)
    .use(ElCard)
    .mount('#app')
