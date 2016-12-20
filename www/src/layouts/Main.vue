<template>  
  <v-container>
    <ul>
        <li>
          <v-link href="/">Home</v-link>
          <v-link href="/about">About</v-link>
        </li>

       <!-- Dropdown Trigger -->
        <a class='dropdown-button btn' href='#' data-activates='dropdown1'>Drop Me!</a>

        <!-- Dropdown Structure -->
        <ul id='dropdown1' class='dropdown-content'>
          <li v-for="item in items"><a href="#!">{{ item }}</a></li>
          <li class="divider"></li>
          <li><a href="/about">three</a></li>
        </ul>
        

    <slot></slot>
  </v-container>    
</template>

<script>
  import VLink from '../components/VLink.vue' 
  
  export default {
    components: {
      VLink 
    },
    data : function(){
      return {
        items : [
          'aaa',
          'bbb'
        ]
      }
    }
  }

</script>

