<template>  
  <div class="main-container">
    <slot></slot>
  </div>    
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