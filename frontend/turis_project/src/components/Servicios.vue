<template>
    <body>
        <div class="titulo-servicios">
            <h1>Servicios</h1>
        </div>
    <div class="container-galery">
        <div class="item">
            <img src="../assets/restaurant.jpg" class="item-image">
            <div class="item-text">
                <h3>Restaurantes & Bares</h3>
                <p>Los restaurantes y Bares del Hotel ofrecen exquisitas opciones gastronómicas para satisfacer todos los apetitos.</p>
            </div>
        </div>
        <div class="item">
            <img src="../assets/events.jpg" class="item-image">
            <div class="item-text">
                <h3>Reuniones & Eventos</h3>
                <p>El Hotel marca la pauta para reuniones y eventos memorables. Nuestra sala de reuniones cuenta con una decoración africana distintiva, inspirada en los pueblos originarios de la isla.</p>
            </div>
        </div>
        <div class="item">
            <img src="../assets/spa.jpg" class="item-image">
            <div class="item-text">
                <h3>Spa & Relajacion</h3>
                <p>El Spa ofrece 6 salas de tratamiento privadas, tres de ellas especiales para parejas y con aire acondicionado. Disfrute de tratamientos rodeados de naturaleza en nuestras cabañas al aire libre y un área especial de relajación y una playa contemplativa.</p>
            </div>
        </div>
        <div class="item">
            <img src="../assets/buseo.jpg" class="item-image">
            <div class="item-text">
                <h3>Excursión de buceo</h3>
                <p>El recorrido sale de nuestro muelle de recepción, después donde los huéspedes son transportados al lugar designado para bucear ubicado al Parque Nacional Natural Corales.</p>
            </div>
        </div>
        <div class="item">
            <img src="../assets/isleta.jpg" class="item-image">
            <div class="item-text">
                <h3>Isleta</h3>
                <p>Isla privada especialmente diseñada para eventos o estancias privadas con 7 habitaciones para hasta 14 personas, una piscina  privada y mas  de 300 metros de playa</p>
            </div>
        </div>
        <div class="item">
            <img src="../assets/clase_Cocina.jpg" class="item-image">
            <div class="item-text">
                <h3>Clase de cocina</h3>
                <p>Aprende a elaborar platos tradicionales de la region como ceviche, coctel de camarones y frituras con un cocinero local. Las clase de cocina son gratuitas para los huéspedes.</p>
            </div>
        </div>
    </div>
    </body>
</template>

<style>
    body{
        margin: 0 0 0 0;
        font-family: 'Mulish',sans-serif;
        box-sizing: border-box;
    }

    .titulo-servicios{
        margin-top: 250px;
        text-align: center;
    }
    .titulo-servicios h1{
        font-size: 36px;
        font-family: 'Roboto';
        font-weight: bold;
    }

    .item-image{
        width: 100%;
        height: 600px;
        margin: 25px 0 0 0;
          
    }

    .container-galery{
        padding: 90px 0 0 0;
        width: 95%;
        margin: 0 auto 100px auto;
        display: grid;   
        grid-template-columns: repeat(2,1fr);  
    }

    .item-text{
        text-align: left;
    }

    .item-text p{
        color: #777777;
        font-family: 'Muli';
        margin: 0;
        font-size: 19px;
    }

    .item-text h3{
        font-family: 'Roboto';
        font-size: 24px;
        margin: 7px 0 7px 0;
    }
    .item{
        margin: 10px;
    }


   
</style>