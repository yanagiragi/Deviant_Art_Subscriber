import Vue from 'vue'
import routes from './routes'
import Materials from "vue-materials"

Vue.use(Materials)

const app = new Vue({
  el: '#app',
  data: {
    currentRoute: window.location.pathname
  },
  computed: {
    ViewComponent () {
      const matchingView = routes[this.currentRoute]
      return matchingView
        ? require('./pages/' + matchingView + '.vue')
        : require('./pages/404.vue')
    }
  },
  render (h) {
    return h(this.ViewComponent)
  }, 
  ready : function(){
    
  }
})

window.addEventListener('popstate', () => {
  app.currentRoute = window.location.pathname
})
