<template>
     <div>
         <div class="detalleRe" id="detalleReserva">
             <button id="cerrar" class="cerrar" v-on:click="cerrarWindow"><i class="far fa-times-circle"></i></button>
                    <h1 class="titleDetalle">Detalle de la reserva</h1>
             <div class="datePerson">
                <div class="datePlane">
                    <h2>Datos</h2>
                    <p>Nombres: {{nombres}}</p>
                    <p>Apellidos: {{apellidos}}</p>
                    <p>Telefono: {{telefono}}</p>
                    <p>Correo: {{correo}}</p>
                    <p>FechaReserva: {{fechaReserva}}</p>    
                    <p>FechaIngreso: {{fechaIngreso}}</p>    
                    <p>FechaSalida: {{fechaSalida}}</p>
                    <p>Tipo de pago: {{tipo_pago}}</p>    
                </div>
                <div class="dateServ">
                    <h2>{{tipoPlan}}</h2>
                    <p>3 habitaciones</p>
                    <p>Desayuno incluido</p>
                    <p>Garantizado con tarjeta de crédito</p>
                    <p>Precio:${{precio}} por noche</p>
                    
                    <h2>{{nombreServicio}}</h2>
                    <p>{{descripcion}}</p>
                    <p>Precio dia ${{precioDia}}</p>
                    <h2>Total: ${{costo}}</h2>
                </div>
            </div>
        </div> 
          
         <div class="nota"> 
             <h2>!Reserva Exitosa¡</h2>
             <p>Felicidades LA ISLA DEL SOL te desea unas hermosas vacaciones,junto con tu familia o 
                amigos,sientanse como en su casa,disfruten de nuestras atenciones,y de todas nuestras
                actividades.
             </p>
         </div>
         <div class="btnsDetalle">
             <button type="button" class="btnDetalle" id="btnDetalle" v-on:click="mostrarDatos">Ver Reserva</button>
             <button type="button" class="btnsalir" id="btnsalir" v-on:click="backInit">Salir</button>
         </div>
     </div>
</template>

<script>
 import axios from 'axios';
export default ({
    name: 'DetalleReserva',
    data:function(){
        return{
            documento:"",
            nombres:"",
            apellidos:"",
            telefono:0,
            correo:"",
            fechaReserva:"",
            fechaIngreso:"",
            fechaSalida:"",
            costo:0,
            tipoPlan:"",
            precio:0,
            tipo_pago:"",
            nombreServicio:"",
            descripcion:"",
            precioDia:0
        }
         
    },
    methods:{
        mostrarDatos:function(){
            axios
            .get(
                `http://localhost:8000/reserva/${parseInt(localStorage.getItem("documento"))}/`,
                {headers:{}}
                
            )
            .then((result) =>{
                if (result.status == 200){
                this.documento = result.data.documento;
                this.nombres = result.data.nombres;
                this.apellidos = result.data.apellidos;
                this.telefono = result.data.telefono;
                this.correo = result.data.email;
                this.fechaReserva = result.data.reserva.fechaReserva;
                this.fechaIngreso = result.data.reserva.fechaIngreso;
                this.fechaSalida = result.data.reserva.fechaSalida;
                this.costo = (result.data.reserva.costo);
                this.tipoPlan = result.data.plan.tipoPlan;
                this.precio = result.data.plan.precio;
                this.tipo_pago = result.data.pago.tipo_pago;
                this.nombreServicio = result.data.servicio.nombreServicio;
                this.descripcion = result.data.servicio.descripcion;
                this.precioDia = result.data.servicio.precioDia

                }
                this.showVent();
                document.getElementById("btnDetalle").setAttribute("disabled","false");
                document.getElementById("btnDetalle").setAttribute("class","btnDetalle__desabled");
                document.getElementById("btnsalir").setAttribute("disabled","false");
                document.getElementById("btnsalir").setAttribute("class","btnDetalle__desabled");
            }
            )
            .catch((error)=>{
               console.log(error) 
            })
        },
        showVent:function(){
             document.getElementById("detalleReserva").style.display = "block";
        },
        cerrarWindow:function(){
            document.getElementById("detalleReserva").style.display = "none";
            document.getElementById("btnDetalle").removeAttribute("disabled");
            document.getElementById("btnDetalle").setAttribute("class","btnDetalle");
            document.getElementById("btnsalir").removeAttribute("disabled");
            document.getElementById("btnsalir").setAttribute("class","btnDetalle");
        },
        backInit:function(){
            this.$router.push({name:"inicio"});
            this.usuOut
        },
        usuOut:function(){
            localStorage.clear()
        }
    }
})
</script>

<style>


.detalleRe{
    width: 45%;
    height: 50%;
    margin: 60px 0 0 0 ;
    background-color: #ffffff;
    border-radius: 25px;
    position: absolute;
    left: 28%;
    top: 17%;
    z-index: 998;
    display: none;
    border: 1px solid #d7d7d7;
}
.detalleRe .titleDetalle{
    text-align: center;
    font-family: 'Muli';
}

.btnsDetalle{
    margin: 0 auto 50px auto;
    width: 500px;
    text-align: center;
    display: flex;
    justify-content: space-between;
}

/* ------------------------ Boton ver reserva ----------------------- */

.btnsDetalle .btnDetalle{
       border: none; 
       width: 200px;
       height: auto; 
       background-color: #333333;     
       font-family: 'Roboto';
       color: #fff9f9;
       border-radius: 5px;
       cursor: pointer;
       font-size: 20px;
       text-align: center;
       padding: 10px 0px 10px 0px;

        
    }
.btnsDetalle .btnDetalle__desabled{
       border: 1px solid #d3d3d3; 
       width: 200px;
       height: auto;      
       font-family: 'Roboto';
       color: #d3d3d3;
       border-radius: 5px;
       font-size: 20px;
       text-align: center;
       padding: 10px 0px 10px 0px;

        
    }


.btnsDetalle .btnDetalle:hover{
       border: none;
       width: 200px;
       height: auto; 
       background-color: #626161;     
       font-family: 'Roboto';
       color: #fff9f9;
       border-radius: 5px;
       cursor: pointer;
       font-size: 20px;
       text-align: center;
       padding: 10px 0px 10px 0px;
       transform: scale(1.04);
       
    }


/* ------------------------ Boton ver reserva ----------------------- */

.btnsDetalle .btnsalir{
       border: none; 
       width: 200px;
       height: auto; 
       background-color: #333333;     
       font-family: 'Roboto';
       color: #fff9f9;
       border-radius: 5px;
       cursor: pointer;
       font-size: 20px;
       text-align: center;
       padding: 10px 0px 10px 0px;

        
    }

.btnsDetalle .btnsalir:hover{
       border: none;
       width: 200px;
       height: auto; 
       background-color: #626161;     
       font-family: 'Roboto';
       color: #fff9f9;
       border-radius: 5px;
       cursor: pointer;
       font-size: 20px;
       text-align: center;
       padding: 10px 0px 10px 0px;
       transform: scale(1.04);
       
    }
/* ------------------------ Boton Cerrar ----------------------- */

.cerrar{
        background: transparent;
       width: 50px;
       height: 50px;      
       font-family: 'Roboto';
       cursor: pointer;
       font-size: 20px;
       text-align: center;
       padding: 0;
       border: none;
       position: absolute;
       right: 3px;
       top:1px
    
       
       
}
.cerrar i{
    font-size: 40px;
    padding: 0%;
    background-color: transparent;
   
}

/* ------------------------ Ventana Detalle Reserva ----------------------- */

.datePerson{
    display: flex;
    justify-content: space-between;
    margin: 0 0 0 50px;
}
.datePerson p{
    margin: 0px 0 6px 0;
    font-family: 'Muli';
}


.dateServ{
    width: 350px;
    margin: 0 30px 0 0;
}

.dateServ h2{
    font-family: 'Roboto';
    font-weight: 500;
    font-size: 20px;
}
.dateServ p{
    margin: 0 0 0 0 ;
    font-family: 'Muli';
    font-size: 17px;
}

.datePlane p{
    font-family: 'Muli';
    font-size: 18px;
}
.datePlane h2{
    font-family: 'Roboto';
    font-weight: 500;
    font-size: 20px;
}

/* ------------------------ nota Reserva ----------------------- */

.nota{
    width: 700px;
    margin: 400px auto 300px auto;
    text-align: center;
}
.nota h2{
    font-family: 'roboto';
    font-size: 30px;
}
.nota p{
    font-family: 'Muli';
    font-size: 20px;
}
</style>