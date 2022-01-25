<template>
    <body>
        <div class="image_prin">
            <!-- <img src="../assets/principal.jpg" alt="playa"> -->
            <video class="" src="../assets/video.mp4" muted loop autoplay></video>
        </div>
        <div class="titulo">
            <h1>Bienvenidos a LA ISLA DEL SOL</h1>
        </div>
        <div class="contenedor">
        <div class="contenido">
                <p>Bienvenidos a LA ISLA DEL SOL
                Reconecta y refresca tu espíritu en medio de las playas de arena blanca y las aguas turquesas   de la Isla Barú de Colombia. Ubicado a solo 45 minutos de Cartagena, el Hotel Las Islas es un     refugio sofisticado, consciente del medio ambiente, con lujosas habitaciones y comodidades  excepcionales.</p>
                <p>
                Acomódese en su bungalow impecablemente decorado, con sus vistas al mar o al vecino Parque Nacional         Natural        Corales del Rosario y de San Bernardo. Visite uno de nuestros restaurantes y bares       para disfrutar de la        cocina local preparada por expertos. Relájese junto a la piscina de     agua dulce, disfrute de las vistas        desde el solárium o explore una de las muchas actividades       disponibles en el hotel. Durante su visita,        disfrutará de la atención personalizada de los       miembros de nuestro personal, quienes están comprometidos a        hacer que su estadía sea       verdaderamente extraordinaria.</p>
            </div>
        </div>
        
    </body>
</template>

<style>

    body{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    .contenedor{
        margin-bottom: 100px;
    }
    .titulo h1{
        text-align: center;
        font-size: 25px;
        margin: 60px;
    }
    .contenido p{
        font-size: 16px;
        color: #939393;
        text-align: center;
    }
    .contenido{
        width: 700px;
        margin: auto;
        padding: 30px 0 0 0;
    }

    .image_prin{
        width: 100%;
        height: 850px;
        overflow: hidden;
    }

     .image_prin video{
        width: 100%;
        height: auto;
    }
    
</style>