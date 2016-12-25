<template>
  <main-layout>
    	<md-tabs>
    	  	<md-dialog-alert
    	  	  md-title="Preview"
  			  :md-content-html="thumbnail"
			  md-ok-text="ok"
			  @open="onOpen"
			  @close="onClose"
			  ref="dialog">
		    </md-dialog-alert>

    	  <md-tab v-for="item in items" v-bind:id="item.author" v-bind:md-label="item.author">
    	  
		    <p>
				<md-table>
				    <md-table-header>
				      <md-table-row>
				        <md-table-head>Title</md-table-head>
				        <md-table-head md-numeric>Preview Thumbnail</md-table-head>
				        <md-table-head md-numeric>DownLoad (experimental)</md-table-head>
				      </md-table-row>
				    </md-table-header>

				    <md-table-body>
				      <md-table-row v-for="data in item.containers" :key="index">
				     
				        <md-table-cell>
				        	<a v-bind:href="data.href" target="_blank">{{data.title}}</a>
				        </md-table-cell>

				        <md-table-cell md-numeric>
				        	&nbsp;<!-- Will not left-aligned if delete space ? -->
				        	<md-button class="md-primary" @click="thumbnail = '<img src=' + data.thumb + ' />'; openDialog('dialog')">
				        		<md-icon class="md-primary">search</md-icon>
				        	</md-button>
				        </md-table-cell>

							
						<md-table-cell md-numeric>
				        	<span v-if="data.DL">Yes</span>
				        	<span v-if="!data.DL">No</span>
				        </md-table-cell>

				      </md-table-row>
				    </md-table-body>
				</md-table>

		    </p>
		  </md-tab>
		</md-tabs>

  </main-layout>
</template>


<script>
  import MainLayout from '../layouts/Main.vue'
  import VueMaterial from 'vue-material'

  export default {
    components: {
      MainLayout,
      VueMaterial
    },
    data : function(){
    	return {
    		items : [{ author : 'Pending...', containers : [] }],
    		start : this.start,
    		thumbnail : 'thumbnail'
    	}
    },
    mounted : function(){
    	
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
	    	console.log('Cool-Start!')
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
	  	},
	  	openDialog(ref) {
	  	  this.$refs[ref].open();
	    },
	  	closeDialog(ref) {
	      this.$refs[ref].close();
	    },
	    onOpen() {
	      console.log('Opened');
	    },
	    onClose(type) {
	      console.log('Closed', type);
	    }
    }
  }
</script>

<style scoped>
	
</style>