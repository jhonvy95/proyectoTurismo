# La isla del sol

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)

Esta es una aplicacion web,basada en una Arquitectura de tres capas,con el objetivo de tener buen rendimiento ,escalabilidad,simplicidad,modificabilidad y confiabilidad,la comuniccion atraves del fronent y el backend es atraves del protocolo REST,y la comunicacion entre el backend y la base de datos es atraves del protocolo TSP

-  Capa de Presentacion.
   vue.js framework
   HTML
   CSS
   JavaScript
   Visual Studio Code(Editor)

-  Capa de Logica
   Django framework
   Python
   Visual Studio Code(Editor)

-  Capa de Datos
   PostgreSQL

![](https://scontent.fbog3-1.fna.fbcdn.net/v/t39.30808-6/272585975_4639775026139287_1690243112315898370_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=730e14&_nc_ohc=_fGI1-kMVR4AX-wM0A-&_nc_ht=scontent.fbog3-1.fna&oh=00_AT-ujNmlqE2aXKknsMv7i46Ra7joDCWIkr7U-E7z0E1X1A&oe=61F62354)

#### Despliegue

-  En este caso se hizo uso del PaaS HEROKU para desplegar las 3 capas.

### Como funciona

La aplicacion web tiene la funcion de realizar una reservacion,dar la opcion de escoger,que servicios quiere incluir,que tipo de plan desea,y poderse dar informacion detallada sobre el lugar,y los servicios que ofrece,en este caso el hotel.

-  Link de la aplicacion web desplegada en heroku [Link]
   (https://laisladelsolfrontend.herokuapp.com/#/reserva/inicio "Link")

### 1. Pagina de inicio

![](https://scontent.fbog3-2.fna.fbcdn.net/v/t39.30808-6/272555310_4640243606092429_4938993759853492722_n.jpg?_nc_cat=106&ccb=1-5&_nc_sid=730e14&_nc_ohc=nHbZhq_eTRwAX-WuZ49&_nc_ht=scontent.fbog3-2.fna&oh=00_AT8cur557Bnnu3JeagHrp0liqirLIRMoTozmz7NNWAU50w&oe=61F69030)

### 2. Seccion de servicios

![](https://scontent.fbog3-2.fna.fbcdn.net/v/t39.30808-6/272798264_4640243632759093_1334120786234431306_n.jpg?_nc_cat=106&ccb=1-5&_nc_sid=730e14&_nc_ohc=rysJemGhgsQAX96mAgI&_nc_ht=scontent.fbog3-2.fna&oh=00_AT8N4G9EkD3dXlQtlNxHurKbHg1H-OxAdxBet4lvJVvwIA&oe=61F5CBE9)

### 3. Seccion de galeria

![](https://scontent.fbog3-2.fna.fbcdn.net/v/t39.30808-6/272437658_4640243602759096_2857857957951021487_n.jpg?_nc_cat=106&ccb=1-5&_nc_sid=730e14&_nc_ohc=3kx6WD6kjhsAX9x9kU5&_nc_ht=scontent.fbog3-2.fna&oh=00_AT8Dwm6wh-xR_PUnyLcEt0FYE3GbQ0MG5Vo0ClhbQ3bHwQ&oe=61F4E1A4)

### 4. Seccion de reserva

-  Toda la informacion de la reserva se guarda en la base de datos. y una vez confirmada la reserva,se le envia al cliente la informacion de la reserva.
   ![](https://scontent.fbog3-1.fna.fbcdn.net/v/t39.30808-6/272821342_4640243762759080_8354392186438260994_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=730e14&_nc_ohc=Qkqa0bPbCNUAX86V2oS&_nc_ht=scontent.fbog3-1.fna&oh=00_AT83-lWD8cPtOYD5c9WeU0u1Axdqzt5MoX1oHkDlH7lhcg&oe=61F57A83)
