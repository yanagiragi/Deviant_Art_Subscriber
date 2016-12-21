<template>
  <main-layout>
    	<ul class="collapsible popout" data-collapsible="expandable">
		    <li v-for="item in items">
		      <div class="collapsible-header"><i class="material-icons">filter_drama</i>{{item.author}}</div>
		      <div class="collapsible-body"><p>{{item.containers}</p></div>
		    </li>
	  </ul>

  </main-layout>
</template>


<script>
  import MainLayout from '../layouts/Main.vue'
  
  export default {
    components: {
      MainLayout
    },
    data : function(){
    	return {
    		items : [{ author : 'No_One_Here' }],
    		start : this.start
    	}
    },
    mounted : function(){
    	$('.collapsible').collapsible({
	      accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
	    });

		var self = this
		this.start()
        setInterval(function cycle() {
           self.start()
        }, 1000 * 60 * 5) // check per 5 minute
    }, 
    watch : {
    	items : function(){
    		console.log('change! ')
    	}
    },
    methods : {
	    start : function(){
	    	console.log('start')
	    	this.fetch().then(data => this.update(data))
	  	},
	  	fetch : function(){
	  		return new Promise((resolve, reject) => {
	    		$.ajax('assets/jsons/dump.json').done(function(data){
	  				resolve(data)	
	  			})
	    	})
	  	}, 
	  	update : function(data){
	  		this.items = data;
	  	}
    }
  }
</script>

<style scoped>
	.main-container{
		padding : 5%;
	}
<sytle>