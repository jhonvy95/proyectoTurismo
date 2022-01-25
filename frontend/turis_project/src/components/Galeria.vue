<template>
    <body>
        <div class="titulo-galeria">
            <h1>Galeria</h1>
        </div>        
            <div class="galery-container">
                <div class="photho"><img src="../assets/galeria/1.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/2.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/3.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/4.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/5.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/6.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/7.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/8.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/9.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/10.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/11.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/12.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/13.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/14.png" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/15.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/16.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/17.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/18.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/19.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/20.jpg" class="item-img"></div>
                <div class="photho"><img src="../assets/galeria/21.jpg" class="item-img"></div>
            </div>
        
    </body>
</template>

<style>
    body{
        margin: 0 0 0 0;
        font-family: 'Mulish',sans-serif;
        box-sizing: border-box;
       
    }

    .titulo-galeria{
        margin-top: 250px;
        text-align: center;
    }
    .titulo-galeria h1{
        font-size: 36px;
        font-family: 'Roboto';
        font-weight: bold;
    }

    

    /* phothos */

    .item-img{
        width: 100%;
        height: 340px;
    }
    .galery-container{
        width: 60%;
        margin: 0 auto 100px auto;
        display: grid;   
        grid-template-columns: repeat(3,1fr);
    }

    .photho{
        margin: 10px;
        transition: transform 0.3s ease-in-out;
    }
    .photho:hover{
        filter: opacity(0.9);
        transform: scale(1.04);
    }
</style>