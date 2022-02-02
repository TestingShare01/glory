import Vue from "vue";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import TDesign from 'tdesign-vue';
import 'tdesign-vue/es/style/index.css';



import App from "./App.vue";

import VueCodemirror from 'vue-codemirror'
import 'codemirror/lib/codemirror.css'
import router from "./router";
import store from "./store";
import jsonView from 'vue-json-views'


Vue.use(ElementUI)
Vue.use(jsonView)
Vue.use(TDesign)
Vue.use(VueCodemirror)

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");


