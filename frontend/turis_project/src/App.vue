<template>
  <div>
  <div class="header">
    <div class="container">
      <div class="nom_logo">
        <h1>LA ISLA DEL SOL</h1>
      </div>
      <div class="nom_sub">
        <h1>Hoteleria y Turismo</h1>
      </div>
      
    </div>
    <nav class="navigation">
        <ul>
          <li><a v-on:click="loadInicio">Inicio</a></li>
          <li><a v-on:click="loadServicios">Servicios</a></li>
          <li><a v-on:click="loadGaleria">Galeria</a></li>         
          <li><a v-on:click="loadReservacion">Reservas</a></li>
        </ul>
      </nav>
  </div>

  <div class="main-component">
    <router-view>
      
    </router-view>
  </div>

  <div class="footer">
    <div class="logo">
       <h1>LA ISLA DEL SOL</h1>
      <h2>Hoteleria y Turismo</h2>
    </div>

    <div class="imfomation">
      <h2>Reservacion:+57 60 1 9998745</h2>
      <h2>Recepcion:+57 60 5 8888745</h2>
      <h2>Email:reservas.hotel@laisladelsol.com.co</h2>
    </div>

    <div class="redes">
      <h2>Siguenos</h2>
      <ul class="icons">
        <li><a href="#"><i class="fab fa-facebook-square"></i></a></li>
        <li><a href="#"><i class="fab fa-instagram"></i></a></li>
        <li><a href="#"><i class="fab fa-twitter"></i></a></li>
        <li><a href="#"><i class="fab fa-youtube"></i></a></li>
      </ul>
    </div>

    <div class="date_curse">
      <h2>Mision Tic 2021</h2>
    </div>

  </div>

  </div>
  
</template>

<script>

export default {
  name:"App",
  data:function() {},
  methods:{
    
    
    loadInicio: function(){
      this.$router.push({name:"inicio"})
    },
    loadServicios: function(){
      this.$router.push({name:"servicios"})
    },
    loadGaleria:function(){
      this.$router.push({name:"galeria"})
    },
    loadReservacion:function(){
      this.$router.push({name:"reservacion"})
    },

  },
  created:function(){
    this.loadInicio()
  },
  
};
</script>


<style>
  body{
    margin: 0 0 0 0;
    font-family: 'Mulish',sans-serif;
  }
  .header{
    background-color: #FAF9F4;
    margin: 0;
    padding: 25px 0 50px 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;
    text-align: center;
    position: fixed;
    left: 0;
    top: 0;
    z-index: 999;
    
    
  }

  .header a{
    color: #5D5D5D;
    text-decoration: none;
    font-size: 18px;
    
  }
 nav ul{
   list-style: none;
   margin: 40px 0 0 0;
   padding: 0;
   
 }

 nav ul li{
   display: inline-block;
   margin: 0 20px;
 }

  nav ul li a:hover{
   color: black;
   cursor: pointer;
 }

  .nom_logo h1{
    margin: 0;
    text-align: center;
    letter-spacing: 7px;
  }

  .nom_sub h1{
    margin:  0;
    text-align: center;
    font-size: 12px;
  }

  /* Footer */
  .footer{
    display: flex;
    background-color: #FAF9F4;
    padding: 70px 80px 70px 80px;
    justify-content: space-between;
    align-items: center;
    
  }

  .logo{
    text-align: center;
    
  }
  .logo h1{
    font-family:'Muli';
    color: #000000;
    margin-bottom: 0;
  }

  .logo h2{
    font-family:'Muli';
    color: #000000;
    font-size: 20px;
    margin-top: 0;
  }

  .imfomation h2{
    font-family: 'Muli';
    font-size: 16px;
    color:  #939393;
  }

  .redes{
    text-align: left;

  }
  .redes h2{
    font-family: 'Roboto';
    font-size: 18px;
    color: #000000;
    font-weight: 400;
  }

  .redes ul{
    list-style: none;
    padding: 0;
  }

  .redes ul li{
    margin: 10px 10px;
    
  }
  .redes i{
    color: #939393;
    font-size: 25px;
  }

  .icons{
    display: flex;
  }

  .date_curse h2{
    font-family: 'Muli';
  }
 
</style>
