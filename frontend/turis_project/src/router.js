import { createRouter, createWebHashHistory } from "vue-router";
import App from "./App.vue";
import Inicio from "./components/Inicio.vue";
import Servicios from "./components/Servicios.vue";
import Galeria from "./components/Galeria.vue";
import Reservacion from "./components/Reserva.vue";
import DetalleReserva from "./components/DetalleReserva.vue";

const routes = [
	{
		path: "/",
		name: "root",
		component: App,
	},
	{
		path: "/reserva/inicio",
		name: "inicio",
		component: Inicio,
	},
	{
		path: "/reserva/servicios",
		name: "servicios",
		component: Servicios,
	},
	{
		path: "/reserva/galeria",
		name: "galeria",
		component: Galeria,
	},
	{
		path: "/reserva/reservacion",
		name: "reservacion",
		component: Reservacion,
	},
	{
		path: "/reserva/detalleReserva",
		name: "detalleReserva",
		component: DetalleReserva,
	},
];

const router = createRouter({
	history: createWebHashHistory(),
	routes,
});

export default router;
