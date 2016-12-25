<template>
  <div>
    <md-toolbar>
      <md-button class="md-icon-button">
        <md-icon>menu</md-icon>
      </md-button>

      <h2 class="md-title" style="flex: 1">Hello Deviantart!</h2>

      <md-button v-for="item in items" class="md-icon-button" v-bind:href="item.href" alt="About">
        <md-icon>{{ item.icon }}</md-icon>
        <md-tooltip md-direction="bottom">{{item.tips}}</md-tooltip>
      </md-button>

    </md-toolbar>

    
    <slot></slot>

  </div>  
</template>

<script>
  
  export default {
    data : function(){
      return {
        items: [
          { href: '/', icon: 'home', tips: 'Home'},
          { href: '/users', icon: 'favorite', tips: 'Follows'},
          { href: '/about', icon: 'description', tips: 'About'}
        ]
      }
    }
  }

</script>