<template>
  <main-layout>
    <div class="title">
    	About Hello DevaiantArt!
    </div>
	
	<div class="row">
		<div class="col s6">
			 <div class="card">
			    <div class="card-image">
			      <img src="assets/images/about.png">
			      <span class="card-title" style="padding : 12px">DevaiantArt</span>
			    </div>
			    <div class="card-content">
			      <p>
			      	DeviantArt is the world's largest online social community for artists and art enthusiasts, allowing people to connect through the creation and sharing of art.
			      </p>
			    </div>
			    <div class="card-action">
			      <a href="http://www.deviantart.com" target="_blank">Visit DevianArt</a>
			    </div>
			</div>
		</div>

		<div class="col s6">		
			<div class="card">
			    <div class="card-image">
			      <img src="assets/images/about.png">
			      <span class="card-title" style="padding : 12px">Hello DevaiantArt!</span>
			    </div>
			    <div class="card-content">
			      <p>
			      	Hello DeviantArt! is a site that collects some watching contents. I mainly focus on Miku Miku Dance contents, such as models, effects, stages, etc.
			      </p>
			    </div>
			    <div class="card-action">
			      <a href="https://github.com/yanagiragi/Deviant_Art_Subscriber" target=_blank>Visit Github</a>
			    </div>
			</div>
		</div>

	</div>



  </main-layout>
</template>

<script>
  import MainLayout from '../layouts/Main.vue'

  export default {
    components: {
      MainLayout
    }
  }
</script>

<style scoped>
	.title {
		width : 100%;
		text-align : center;
		font-size : 3em;
		padding: 5%;
	}
	.card {
		margin-left: 25%;
		width : 50%;
		text-align: center;
	}
	.card-title{
		width : 100%;
		font-style : italic;
	}
	
</style>