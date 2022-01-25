<template>
	<div>
		<div class="reserva_form">
			<form v-on:submit.prevent="processReserva">
				<h2 class="title1">Informacion del invitado</h2>
				<div class="dc_ajus">
					<p class="text">Documento</p>
					<input
						type="number"
						v-model="persona.documento"
						id="dc"
						class="field"
						required
					/>
				</div>

				<div class="block1">
					<div class="centrar">
						<p>Nombres</p>
						<input
							type="text"
							v-model="persona.nombres"
							id="nombres"
							class="field"
							required
							maxlength="10"
						/>
					</div>
					<div class="centrar">
						<p>Apellidos</p>
						<input
							type="text"
							v-model="persona.apellidos"
							id="apellidos"
							class="field"
							required
						/>
					</div>
				</div>

				<div class="block1">
					<div class="centrar">
						<p>Telefono</p>
						<input
							type="tel"
							v-model="persona.telefono"
							id="telefonos"
							class="field"
							required
						/>
					</div>
					<div class="centrar">
						<p>Correo</p>
						<input
							type="email"
							v-model="persona.correo"
							id="correo"
							class="field"
							required
						/>
					</div>
				</div>

				<div class="block1">
					<div class="centrar">
						<p>Fecha Ingreso</p>
						<input
							type="date"
							v-model="persona.reserva.fechaIngreso"
							id="fechaIngreso"
							class="field"
							required
						/>
					</div>
					<div class="centrar">
						<p>Fecha Salida</p>
						<input
							type="date"
							v-model="persona.reserva.fechaSalida"
							id="fechaSalida"
							class="field"
							required
						/>
					</div>
				</div>
				<hr class="hr" />
				<!-- ------------------------------------------box Planes ---------------------------------------------->
				<h2 class="title1">Planes</h2>
				<div class="list_plan">
					<div class="plan_container">
						<div class="plan_section">
							<img src="../assets/plan/amigos.jpg" alt="" class="img_plan" />
							<p>Aire Acondicionado</p>
							<p>wifi</p>
							<p>Caja fuerte en la habitación</p>
							<p>TV</p>
						</div>
						<div class="plan_section2">
							<h2>Plan amigos</h2>
							<p>3 habitaciones</p>
							<p>Desayuno incluido</p>
							<p>Garantizado con tarjeta de crédito</p>
							<p>Precio:$500.000 por noche</p>
							<hr />
							<button type="button" class="btn" id="btn1" v-on:click="p_btn1">
								<i class="fas fa-check"></i>
							</button>
							<button
								type="button"
								class="btnx"
								id="btn1x"
								v-on:click="p_btn1x"
							>
								<i class="fas fa-times"></i>
							</button>
						</div>
					</div>
					<div class="plan_container">
						<div class="plan_section">
							<img src="../assets/plan/relax.jpg" alt="" class="img_plan" />
							<p>Aire Acondicionado</p>
							<p>wifi</p>
							<p>Caja fuerte en la habitación</p>
							<p>TV</p>
						</div>
						<div class="plan_section2">
							<h2>Plan Pasadia Relax</h2>
							<p>1 habitacion</p>
							<p>Desayuno incluido</p>
							<p>Garantizado con tarjeta de crédito</p>
							<p>Precio:$150.000 por noche</p>
							<hr />
							<button type="button" class="btn" id="btn2" v-on:click="p_btn2">
								<i class="fas fa-check"></i>
							</button>
							<button
								type="button"
								class="btnx"
								id="btn2x"
								v-on:click="p_btn2x"
							>
								<i class="fas fa-times"></i>
							</button>
						</div>
					</div>
					<div class="plan_container">
						<div class="plan_section">
							<img src="../assets/plan/casate.jpg" alt="" class="img_plan" />
							<p>Aire Acondicionado</p>
							<p>wifi</p>
							<p>Caja fuerte en la habitación</p>
							<p>TV</p>
						</div>
						<div class="plan_section2">
							<h2>Plan Casate Conmigo</h2>
							<p>1 habitacion</p>
							<p>Desayuno incluido</p>
							<p>Garantizado con tarjeta de crédito</p>
							<p>Precio:$250.000 por noche</p>
							<hr />
							<button type="button" class="btn" id="btn3" v-on:click="p_btn3">
								<i class="fas fa-check"></i>
							</button>
							<button
								type="button"
								class="btnx"
								id="btn3x"
								v-on:click="p_btn3x"
							>
								<i class="fas fa-times"></i>
							</button>
						</div>
					</div>
					<div class="plan_container">
						<div class="plan_section">
							<img
								src="../assets/plan/amor_y_amistad.jpg"
								alt=""
								class="img_plan"
							/>
							<p>Aire Acondicionado</p>
							<p>wifi</p>
							<p>Caja fuerte en la habitación</p>
							<p>TV</p>
						</div>
						<div class="plan_section2">
							<h2>Plan Amor y amistad</h2>
							<p>1 habitacion</p>
							<p>Desayuno incluido</p>
							<p>Garantizado con tarjeta de crédito</p>
							<p>Precio:$200.000 por noche</p>
							<hr />
							<button type="button" class="btn" id="btn4" v-on:click="p_btn4">
								<i class="fas fa-check"></i>
							</button>
							<button
								type="button"
								class="btnx"
								id="btn4x"
								v-on:click="p_btn4x"
							>
								<i class="fas fa-times"></i>
							</button>
						</div>
					</div>
				</div>

				<hr class="hr" />
				<!-- ------------------------------------------box servicio ---------------------------------------------->
				<div>
					<h2 class="title1">Servicios</h2>
					<div class="list_plan">
						<div class="plan_container">
							<div class="plan_section">
								<img src="../assets/spa.jpg" alt="" class="img_plan" />
							</div>
							<div class="plan_section2">
								<h2>Spa & Relajacion</h2>
								<p>
									Disfrute de tratamientos rodeados de naturaleza en nuestras
									cabañas al aire libre y un área especial de relajación y una
									playa contemplativa.
								</p>
								<p>Precio:$50.000 por noche</p>
								<hr />
								<button
									type="button"
									class="btn"
									id="s_btn1"
									v-on:click="s_btn1"
								>
									<i class="fas fa-check"></i>
								</button>
								<button
									type="button"
									class="btnx"
									id="s_btn1x"
									v-on:click="s_btn1x"
								>
									<i class="fas fa-times"></i>
								</button>
							</div>
						</div>
						<div class="plan_container">
							<div class="plan_section">
								<img src="../assets/buseo.jpg" alt="" class="img_plan" />
							</div>
							<div class="plan_section2">
								<h2>Excursión de buceo</h2>
								<p>
									El recorrido sale de nuestro muelle de recepción, después
									donde los huéspedes son transportados al lugar designado para
									bucear ubicado al Parque Nacional Natural Corales.
								</p>
								<p>Precio:$100.000 por noche</p>
								<hr />
								<button
									type="button"
									class="btn"
									id="s_btn2"
									v-on:click="s_btn2"
								>
									<i class="fas fa-check"></i>
								</button>
								<button
									type="button"
									class="btnx"
									id="s_btn2x"
									v-on:click="s_btn2x"
								>
									<i class="fas fa-times"></i>
								</button>
							</div>
						</div>
						<div class="plan_container">
							<div class="plan_section">
								<img src="../assets/clase_Cocina.jpg" alt="" class="img_plan" />
							</div>
							<div class="plan_section2">
								<h2>Clase de cocina</h2>
								<p>
									Aprende a elaborar platos tradicionales de la region como
									ceviche, coctel de camarones y frituras con un cocinero local.
								</p>
								<p>Precio:$60.000 por noche</p>
								<hr />
								<button
									type="button"
									class="btn"
									id="s_btn3"
									v-on:click="s_btn3"
								>
									<i class="fas fa-check"></i>
								</button>
								<button
									type="button"
									class="btnx"
									id="s_btn3x"
									v-on:click="s_btn3x"
								>
									<i class="fas fa-times"></i>
								</button>
							</div>
						</div>
						<div class="plan_container">
							<div class="plan_section">
								<img src="../assets/restaurant.jpg" alt="" class="img_plan" />
							</div>
							<div class="plan_section2">
								<h2>Restaurantes & Bares</h2>
								<p>
									El Hotel marca la pauta para reuniones y eventos memorables.
									Nuestra sala de reuniones cuenta con una decoración africana
									distintiva.
								</p>
								<p>Precio:$70.000 por noche</p>
								<hr />
								<button
									type="button"
									class="btn"
									id="s_btn4"
									v-on:click="s_btn4"
								>
									<i class="fas fa-check"></i>
								</button>
								<button
									type="button"
									class="btnx"
									id="s_btn4x"
									v-on:click="s_btn4x"
								>
									<i class="fas fa-times"></i>
								</button>
							</div>
						</div>
					</div>
				</div>
				<hr class="hr" />

				<!-- ------------------------------------------box pago ---------------------------------------------->
				<h2 class="title1">Información del pago</h2>
				<div class="medio_pago">
					<div>
						<img
							src="../assets/medio_pago/medios_pago.png"
							alt=""
							class="img_pago"
						/>

						<div class="tipo_pago">
							<input
								type="radio"
								value="Targeta Debito"
								v-model="persona.pago.tipo_pago"
								required
							/>
							<label>Tarjeta dèbito</label>

							<input
								type="radio"
								value="Tarjeta Credito"
								v-model="persona.pago.tipo_pago"
								required
							/>
							<label>Tarjeta credito</label>
						</div>
					</div>
					<div class="total">
						<h2 class="title_total">Total:</h2>
						<h2>{{ persona.reserva.costo }}</h2>
					</div>
				</div>
				<hr class="hr" />
				<!-- ------------------------------------------- Boton reserva -------------------------------------- -->

				<div class="box_reserva">
					<button class="reserva" type="submit" id="btn">Reservar</button>
				</div>
			</form>
		</div>
	</div>
</template>

<script>
	import axios from "axios";
	export default {
		name: "Reserva",
		data: function() {
			return {
				persona: {
					documento: "",
					nombres: "",
					apellidos: "",
					telefono: "",
					correo: "",
					cliente: {
						active: true,
					},
					reserva: {
						fechaReserva: "2021-10-30",
						fechaIngreso: "",
						fechaSalida: "",
						costo: 0,
					},
					plan: {
						tipoPlan: "",
						precio: 0,
					},
					pago: {
						tipo_pago: "",
					},
					servicio: {
						nombreServicio: "",
						descripcion: "",
						precioDia: 0,
					},
				},
			};
		},
		methods: {
			processReserva: function() {
				axios
					.post("http://localhost:8000/reserva/", this.persona, { headers: {} })
					.then((result) => {
						if (result.status == 201) {
							this.reservaExitosa();
							localStorage.setItem("documento", this.persona.documento);
							console.log(typeof localStorage.getItem("documento"));
						}
					})
					.catch((error) => {
						console.log(error);
					});
			},
            calcularFecha:function(){
                var fechaini = new Date(document.getElementById('fechaIngreso').value);
	            var fechafin = new Date(document.getElementById('fechaSalida').value);
	            var diasdif= fechafin.getTime()-fechaini.getTime();
	            var contdias = Math.round(diasdif/(1000*60*60*24));
                return contdias
            },
			p_btn1: function() {
				document.getElementById("btn1").setAttribute("class", "btn_pres");
				document.getElementById("btn2").setAttribute("disabled", "false");
				document.getElementById("btn2").setAttribute("class", "btn_desabled");
				document.getElementById("btn3").setAttribute("disabled", "false");
				document.getElementById("btn3").setAttribute("class", "btn_desabled");
				document.getElementById("btn4").setAttribute("disabled", "false");
				document.getElementById("btn4").setAttribute("class", "btn_desabled");

				document.getElementById("btn2x").setAttribute("disabled", "false");
				document.getElementById("btn2x").setAttribute("class", "btn_desabled");
				document.getElementById("btn3x").setAttribute("disabled", "false");
				document.getElementById("btn3x").setAttribute("class", "btn_desabled");
				document.getElementById("btn4x").setAttribute("disabled", "false");
				document.getElementById("btn4x").setAttribute("class", "btn_desabled");

				console.log((this.persona.plan.tipoPlan = "Plan amigos"));
				console.log((this.persona.plan.precio = 500000));
				this.persona.reserva.costo += (500000*(this.calcularFecha()))
			},
			p_btn2: function() {
				document.getElementById("btn2").setAttribute("class", "btn_pres");
				document.getElementById("btn1").setAttribute("disabled", "false");
				document.getElementById("btn1").setAttribute("class", "btn_desabled");
				document.getElementById("btn3").setAttribute("disabled", "false");
				document.getElementById("btn3").setAttribute("class", "btn_desabled");
				document.getElementById("btn4").setAttribute("disabled", "false");
				document.getElementById("btn4").setAttribute("class", "btn_desabled");

				console.log((this.persona.plan.tipoPlan = "Plan Pasadia Relax Plus"));
				console.log((this.persona.plan.precio = 150000));
				this.persona.reserva.costo += (150000*(this.calcularFecha()))

				document.getElementById("btn1x").setAttribute("disabled", "false");
				document.getElementById("btn1x").setAttribute("class", "btn_desabled");
				document.getElementById("btn3x").setAttribute("disabled", "false");
				document.getElementById("btn3x").setAttribute("class", "btn_desabled");
				document.getElementById("btn4x").setAttribute("disabled", "false");
				document.getElementById("btn4x").setAttribute("class", "btn_desabled");
			},
			p_btn3: function() {
				document.getElementById("btn3").setAttribute("class", "btn_pres");
				document.getElementById("btn2").setAttribute("disabled", "false");
				document.getElementById("btn2").setAttribute("class", "btn_desabled");
				document.getElementById("btn1").setAttribute("disabled", "false");
				document.getElementById("btn1").setAttribute("class", "btn_desabled");
				document.getElementById("btn4").setAttribute("disabled", "false");
				document.getElementById("btn4").setAttribute("class", "btn_desabled");

				console.log((this.persona.plan.tipoPlan = "Plan Casate Conmigo"));
				console.log((this.persona.plan.precio = 250000));
				this.persona.reserva.costo += (250000*(this.calcularFecha()));
				

				document.getElementById("btn2x").setAttribute("disabled", "false");
				document.getElementById("btn2x").setAttribute("class", "btn_desabled");
				document.getElementById("btn1x").setAttribute("disabled", "false");
				document.getElementById("btn1x").setAttribute("class", "btn_desabled");
				document.getElementById("btn4x").setAttribute("disabled", "false");
				document.getElementById("btn4x").setAttribute("class", "btn_desabled");
			},
			p_btn4: function() {
				document.getElementById("btn4").setAttribute("class", "btn_pres");
				document.getElementById("btn2").setAttribute("disabled", "false");
				document.getElementById("btn2").setAttribute("class", "btn_desabled");
				document.getElementById("btn3").setAttribute("disabled", "false");
				document.getElementById("btn3").setAttribute("class", "btn_desabled");
				document.getElementById("btn1").setAttribute("disabled", "false");
				document.getElementById("btn1").setAttribute("class", "btn_desabled");

				console.log((this.persona.plan.tipoPlan = "Plan Amor y amistad"));
				console.log((this.persona.plan.precio = 200000));
			    this.persona.reserva.costo += (200000*(this.calcularFecha()));


				document.getElementById("btn2x").setAttribute("disabled", "false");
				document.getElementById("btn2x").setAttribute("class", "btn_desabled");
				document.getElementById("btn3x").setAttribute("disabled", "false");
				document.getElementById("btn3x").setAttribute("class", "btn_desabled");
				document.getElementById("btn1x").setAttribute("disabled", "false");
				document.getElementById("btn1x").setAttribute("class", "btn_desabled");
			},
			p_btn1x: function() {
				document.getElementById("btn1").removeAttribute("btn_pres");
				document.getElementById("btn1").setAttribute("class", "btn");
				document.getElementById("btn2").removeAttribute("disabled");
				document.getElementById("btn2").setAttribute("class", "btn");
				document.getElementById("btn3").removeAttribute("disabled");
				document.getElementById("btn3").setAttribute("class", "btn");
				document.getElementById("btn4").removeAttribute("disabled");
				document.getElementById("btn4").setAttribute("class", "btn");
				this.persona.reserva.costo -=(500000*(this.calcularFecha()));

				document.getElementById("btn2x").removeAttribute("disabled");
				document.getElementById("btn2x").setAttribute("class", "btnx");
				document.getElementById("btn3x").removeAttribute("disabled");
				document.getElementById("btn3x").setAttribute("class", "btnx");
				document.getElementById("btn4x").removeAttribute("disabled");
				document.getElementById("btn4x").setAttribute("class", "btnx");
			},
			p_btn2x: function() {
				document.getElementById("btn2").removeAttribute("btn_pres");
				document.getElementById("btn2").setAttribute("class", "btn");
				document.getElementById("btn1").removeAttribute("disabled");
				document.getElementById("btn1").setAttribute("class", "btn");
				document.getElementById("btn3").removeAttribute("disabled");
				document.getElementById("btn3").setAttribute("class", "btn");
				document.getElementById("btn4").removeAttribute("disabled");
				document.getElementById("btn4").setAttribute("class", "btn");
				this.persona.reserva.costo -= (150000*(this.calcularFecha()));

				document.getElementById("btn1x").removeAttribute("disabled");
				document.getElementById("btn1x").setAttribute("class", "btnx");
				document.getElementById("btn3x").removeAttribute("disabled");
				document.getElementById("btn3x").setAttribute("class", "btnx");
				document.getElementById("btn4x").removeAttribute("disabled");
				document.getElementById("btn4x").setAttribute("class", "btnx");
			},
			p_btn3x: function() {
				document.getElementById("btn3").removeAttribute("btn_pres");
				document.getElementById("btn3").setAttribute("class", "btn");
				document.getElementById("btn2").removeAttribute("disabled");
				document.getElementById("btn2").setAttribute("class", "btn");
				document.getElementById("btn1").removeAttribute("disabled");
				document.getElementById("btn1").setAttribute("class", "btn");
				document.getElementById("btn4").removeAttribute("disabled");
				document.getElementById("btn4").setAttribute("class", "btn");
				this.persona.reserva.costo -= (250000*(this.calcularFecha()));

				document.getElementById("btn2x").removeAttribute("disabled");
				document.getElementById("btn2x").setAttribute("class", "btnx");
				document.getElementById("btn1x").removeAttribute("disabled");
				document.getElementById("btn1x").setAttribute("class", "btnx");
				document.getElementById("btn4x").removeAttribute("disabled");
				document.getElementById("btn4x").setAttribute("class", "btnx");
			},
			p_btn4x: function() {
				document.getElementById("btn4").removeAttribute("btn_pres");
				document.getElementById("btn4").setAttribute("class", "btn");
				document.getElementById("btn2").removeAttribute("disabled");
				document.getElementById("btn2").setAttribute("class", "btn");
				document.getElementById("btn3").removeAttribute("disabled");
				document.getElementById("btn3").setAttribute("class", "btn");
				document.getElementById("btn1").removeAttribute("disabled");
				document.getElementById("btn1").setAttribute("class", "btn");
				this.persona.reserva.costo -= (200000*(this.calcularFecha()));

				document.getElementById("btn2x").removeAttribute("disabled");
				document.getElementById("btn2x").setAttribute("class", "btnx");
				document.getElementById("btn3x").removeAttribute("disabled");
				document.getElementById("btn3x").setAttribute("class", "btnx");
				document.getElementById("btn1x").removeAttribute("disabled");
				document.getElementById("btn1x").setAttribute("class", "btnx");
			},
			s_btn1: function() {
				document.getElementById("s_btn1").setAttribute("class", "btn_pres");
				document.getElementById("s_btn2").setAttribute("disabled", "false");
				document.getElementById("s_btn2").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn3").setAttribute("disabled", "false");
				document.getElementById("s_btn3").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn4").setAttribute("disabled", "false");
				document.getElementById("s_btn4").setAttribute("class", "btn_desabled");

				document.getElementById("s_btn2x").setAttribute("disabled", "false");
				document.getElementById("s_btn2x").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn3x").setAttribute("disabled", "false");
				document.getElementById("s_btn3x").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn4x").setAttribute("disabled", "false");
				document.getElementById("s_btn4x").setAttribute("class", "btn_desabled");

				console.log(
					(this.persona.servicio.nombreServicio = "Spa & Relajacion")
				);
				console.log(
					(this.persona.servicio.descripcion =
						"Disfrute de tratamientos rodeados de naturaleza en nuestras cabañas al aire libre y un área especial de relajación y una playa contemplativa.")
				);
				console.log((this.persona.servicio.precioDia = 50000));
				this.persona.reserva.costo += (50000*(this.calcularFecha()));
			},
			s_btn2: function() {
				document.getElementById("s_btn2").setAttribute("class", "btn_pres");
				document.getElementById("s_btn1").setAttribute("disabled", "false");
				document.getElementById("s_btn1").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn3").setAttribute("disabled", "false");
				document.getElementById("s_btn3").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn4").setAttribute("disabled", "false");
				document.getElementById("s_btn4").setAttribute("class", "btn_desabled");

				document.getElementById("s_btn1x").setAttribute("disabled", "false");
				document.getElementById("s_btn1x").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn3x").setAttribute("disabled", "false");
				document.getElementById("s_btn3x").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn4x").setAttribute("disabled", "false");
				document.getElementById("s_btn4x").setAttribute("class", "btn_desabled");

                console.log(
					(this.persona.servicio.nombreServicio = "Excursión de buceo")
				);
				console.log(
					(this.persona.servicio.descripcion =
						"El recorrido sale de nuestro muelle de recepción, después donde los huéspedes son transportados al lugar designado para bucear")
				);
				console.log((this.persona.servicio.precioDia = 100000));
				this.persona.reserva.costo += (100000*(this.calcularFecha()));
			},
			s_btn3: function() {
				document.getElementById("s_btn3").setAttribute("class", "btn_pres");
				document.getElementById("s_btn2").setAttribute("disabled", "false");
				document.getElementById("s_btn2").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn1").setAttribute("disabled", "false");
				document.getElementById("s_btn1").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn4").setAttribute("disabled", "false");
				document.getElementById("s_btn4").setAttribute("class", "btn_desabled");

				console.log((this.persona.servicio.nombreServicio = "Clase de cocina"));
				console.log(
					(this.persona.servicio.descripcion =
						"Aprende a elaborar platos tradicionales de la region como ceviche, coctel de camarones y frituras con un cocinero local.")
				);
				console.log((this.persona.servicio.precioDia = 60000));
				this.persona.reserva.costo += (60000*(this.calcularFecha()));

				document.getElementById("s_btn2x").setAttribute("disabled", "false");
				document.getElementById("s_btn2x").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn1x").setAttribute("disabled", "false");
				document.getElementById("s_btn1x").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn4x").setAttribute("disabled", "false");
				document.getElementById("s_btn4x").setAttribute("class", "btn_desabled");
			},
			s_btn4: function() {
				document.getElementById("s_btn4").setAttribute("class", "btn_pres");
				document.getElementById("s_btn2").setAttribute("disabled", "false");
				document.getElementById("s_btn2").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn3").setAttribute("disabled", "false");
				document.getElementById("s_btn3").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn1").setAttribute("disabled", "false");
				document.getElementById("s_btn1").setAttribute("class", "btn_desabled");

				console.log(
					(this.persona.servicio.nombreServicio = "Restaurantes & Bares")
				);
				console.log(
					(this.persona.servicio.descripcion =
						"El Hotel marca la pauta para reuniones y eventos memorables. Nuestra sala de reuniones cuenta con una decoración africana distintiva.")
				);
				console.log((this.persona.servicio.precioDia = 70000));
				this.persona.reserva.costo += (70000*(this.calcularFecha()));

				document.getElementById("s_btn2x").setAttribute("disabled", "false");
				document.getElementById("s_btn2x").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn3x").setAttribute("disabled", "false");
				document.getElementById("s_btn3x").setAttribute("class", "btn_desabled");
				document.getElementById("s_btn1x").setAttribute("disabled", "false");
				document.getElementById("s_btn1x").setAttribute("class", "btn_desabled");
			},
			s_btn1x: function() {
				document.getElementById("s_btn1").removeAttribute("btn_pres");
				document.getElementById("s_btn1").setAttribute("class", "btn");
				document.getElementById("s_btn2").removeAttribute("disabled");
				document.getElementById("s_btn2").setAttribute("class", "btn");
				document.getElementById("s_btn3").removeAttribute("disabled");
				document.getElementById("s_btn3").setAttribute("class", "btn");
				document.getElementById("s_btn4").removeAttribute("disabled");
				document.getElementById("s_btn4").setAttribute("class", "btn");
				this.persona.reserva.costo -= (50000*(this.calcularFecha()));

				document.getElementById("s_btn2x").removeAttribute("disabled");
				document.getElementById("s_btn2x").setAttribute("class", "btnx");
				document.getElementById("s_btn3x").removeAttribute("disabled");
				document.getElementById("s_btn3x").setAttribute("class", "btnx");
				document.getElementById("s_btn4x").removeAttribute("disabled");
				document.getElementById("s_btn4x").setAttribute("class", "btnx");
			},
			s_btn2x: function() {
				document.getElementById("s_btn2").removeAttribute("btn_pres");
				document.getElementById("s_btn2").setAttribute("class", "btn");
				document.getElementById("s_btn1").removeAttribute("disabled");
				document.getElementById("s_btn1").setAttribute("class", "btn");
				document.getElementById("s_btn3").removeAttribute("disabled");
				document.getElementById("s_btn3").setAttribute("class", "btn");
				document.getElementById("s_btn4").removeAttribute("disabled");
				document.getElementById("s_btn4").setAttribute("class", "btn");
				this.persona.reserva.costo -= (100000*(this.calcularFecha()));

				document.getElementById("s_btn1x").removeAttribute("disabled");
				document.getElementById("s_btn1x").setAttribute("class", "btnx");
				document.getElementById("s_btn3x").removeAttribute("disabled");
				document.getElementById("s_btn3x").setAttribute("class", "btnx");
				document.getElementById("s_btn4x").removeAttribute("disabled");
				document.getElementById("s_btn4x").setAttribute("class", "btnx");
			},
			s_btn3x: function() {
				document.getElementById("s_btn3").removeAttribute("btn_pres");
				document.getElementById("s_btn3").setAttribute("class", "btn");
				document.getElementById("s_btn2").removeAttribute("disabled");
				document.getElementById("s_btn2").setAttribute("class", "btn");
				document.getElementById("s_btn1").removeAttribute("disabled");
				document.getElementById("s_btn1").setAttribute("class", "btn");
				document.getElementById("s_btn4").removeAttribute("disabled");
				document.getElementById("s_btn4").setAttribute("class", "btn");
				this.persona.reserva.costo -= (60000*(this.calcularFecha()));

				document.getElementById("s_btn2x").removeAttribute("disabled");
				document.getElementById("s_btn2x").setAttribute("class", "btnx");
				document.getElementById("s_btn1x").removeAttribute("disabled");
				document.getElementById("s_btn1x").setAttribute("class", "btnx");
				document.getElementById("s_btn4x").removeAttribute("disabled");
				document.getElementById("s_btn4x").setAttribute("class", "btnx");
			},
			s_btn4x: function() {
				document.getElementById("s_btn4").removeAttribute("btn_pres");
				document.getElementById("s_btn4").setAttribute("class", "btn");
				document.getElementById("s_btn2").removeAttribute("disabled");
				document.getElementById("s_btn2").setAttribute("class", "btn");
				document.getElementById("s_btn3").removeAttribute("disabled");
				document.getElementById("s_btn3").setAttribute("class", "btn");
				document.getElementById("s_btn1").removeAttribute("disabled");
				document.getElementById("s_btn1").setAttribute("class", "btn");
				this.persona.reserva.costo -= (70000*(this.calcularFecha()));

				document.getElementById("s_btn2x").removeAttribute("disabled");
				document.getElementById("s_btn2x").setAttribute("class", "btnx");
				document.getElementById("s_btn3x").removeAttribute("disabled");
				document.getElementById("s_btn3x").setAttribute("class", "btnx");
				document.getElementById("s_btn1x").removeAttribute("disabled");
				document.getElementById("s_btn1x").setAttribute("class", "btnx");
			},
			reservaExitosa: function() {
				this.$router.push({ name: "detalleReserva" });
			},
		},
	};
</script>

<style>
	body {
		box-sizing: border-box;
		margin: 0;
		padding: 0;
	}
	.reserva_form {
		width: 800px;
		text-align: center;
		margin: 300px auto 50px auto;
		border: 1px solid #d7d7d7;
		padding: 50px;
		border-radius: 3px;
		font-size: 20px;
		font-family: "Muli";
		color: #999999;
	}
	input,
	textarea {
		border: 0;
		outline: none;
	}

	.field {
		border: 1px solid black;
		padding: 10px;
		width: 280px;
	}
	.field:focus {
		border-color: bisque;
	}

	.title1 {
		color: #333333;
		font-family: "Roboto Slab";
		font-size: 25px;
		font-weight: 300;
	}
	.block1 {
		display: flex;
		justify-content: space-around;
		margin-top: 50px;
	}

	.block1 .centrar {
		text-align: left;
	}
	.dc_ajus {
		text-align: left;
		margin: 90px 0 0 50px;
	}

	.hr {
		margin-top: 70px;
	}

	/* ----------------------------- planes ---------------------------*/

	.plan_container {
		display: flex;
		margin: 40px 10px 0 0;
		border: 1px solid #d7d7d7;
		padding: 10px;
	}
	.plan_container p {
		font-family: "Muli";
		font-size: 14px;
		color: #777777;
		margin: 5px 0 0 0;
	}
	.plan_container .plan_section {
		text-align: left;
	}
	.plan_container .plan_section2 {
		text-align: left;
		margin: 0 0 0 10px;
	}
	.plan_container .plan_section2 h2 {
		margin: 0 0 15px 0;
		font-family: "Muli";
		color: #333333;
		font-size: 21px;
	}
	.plan_container .plan_section2 button {
		margin: 5px 0 0 38px;
		align-content: center;
	}
	.plan_container .plan_section2 button i {
		font-size: 15px;
	}
	/* --------- Boton chulito ---------*/

	.plan_section2 .btn {
		border: 1px solid #777777;
		width: 50px;
		height: 30px;
		font-family: "Roboto";
		color: #777777;
		border-radius: 5px;
		cursor: pointer;
		font-size: 20px;
		text-align: center;
	}
	.plan_section2 .btn:hover {
		border: 1px solid #5c9c56;
		width: 50px;
		height: 30px;
		font-family: "Roboto";
		color: #5c9c56;
		border-radius: 5px;
		cursor: pointer;
		font-size: 20px;
		text-align: center;
	}
	.plan_section2 .btn_pres {
		border: none;
		width: 50px;
		height: 30px;
		font-family: "Roboto";
		color: #fafff9;
		background-color: #4ec044;
		border-radius: 5px;
		cursor: pointer;
		font-size: 20px;
		text-align: center;
	}
	.plan_section2 .btn_desabled {
		border: 1px solid #d3d3d3;
		width: 50px;
		height: 30px;
		font-family: "Roboto";
		color: #d3d3d3;
		border-radius: 5px;
		font-size: 20px;
		text-align: center;
	}

	/* --------- Boton x ---------*/

	.plan_section2 .btnx {
		border: 1px solid #777777;
		width: 50px;
		height: 30px;
		font-family: "Roboto";
		color: #777777;
		border-radius: 5px;
		cursor: pointer;
		font-size: 20px;
		text-align: center;
	}
	.plan_section2 .btnx:hover {
		border: 1px solid #bd3131;
		width: 50px;
		height: 30px;
		font-family: "Roboto";
		color: #bd3131;
		border-radius: 5px;
		cursor: pointer;
		font-size: 20px;
		text-align: center;
	}

	/* ----------------------------------------- */

	.img_plan {
		width: 150px;
		height: auto;
		margin-bottom: 10px;
	}

	.list_plan {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
	}

	/* ------------------------ Medio Pago ----------------------- */

	.medio_pago {
		display: flex;
		justify-content: space-between;
		margin: 70px 0 0 0;
	}
	.medio_pago .tipo_pago input {
		margin: 0 0 0 30px;
	}
	.medio_pago .img_pago {
		width: 200px;
		height: auto;
		margin: 0 0 20px 0;
	}
	.total {
		text-align: left;
		margin: 80px 90px 0 0;
	}
	.total h2 {
		font-family: "Muli";
		color: #777777;
		font-size: 20px;
		margin: 0;
	}
	.total .title_total {
		color: #333333;
		font-size: 25px;
	}

	/* ------------------------ Boton Reserva ----------------------- */
	.box_reserva button {
		margin: 60px 0 0 0;
	}
	.reserva {
		border: none;
		width: 150px;
		height: auto;
		background-color: #333333;
		font-family: "Roboto";
		color: #fff9f9;
		border-radius: 5px;
		cursor: pointer;
		font-size: 20px;
		text-align: center;
		padding: 10px 0px 10px 0px;
	}

	.reserva:hover {
		border: none;
		width: 150px;
		height: auto;
		background-color: #626161;
		font-family: "Roboto";
		color: #fff9f9;
		border-radius: 5px;
		cursor: pointer;
		font-size: 20px;
		text-align: center;
		padding: 10px 0px 10px 0px;
		transform: scale(1.04);
	}
</style>
