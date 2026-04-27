import tkinter as tk

class PantallaBatalla:

    def __init__(self, jugador, cpu, p_jugador, p_cpu):
        self.jugador = jugador
        self.cpu = cpu
        self.p_jugador = p_jugador
        self.p_cpu = p_cpu

        self.ganador = None
        self.perdedor = None
        self.combate_terminado = False  # 🔥 control de estado

        self.ventana = tk.Tk()
        self.ventana.title("Batalla Pokémon")

        # 🧱 FRAME SUPERIOR (avatares + info)
        frame_superior = tk.Frame(self.ventana)
        frame_superior.pack(pady=10)

        # 🧑 JUGADOR
        frame_jugador = tk.Frame(frame_superior)
        frame_jugador.pack(side="left", padx=20)

        self.img_jugador = tk.PhotoImage(file=jugador.avatar).subsample(3, 3)
        label_img_j = tk.Label(frame_jugador, image=self.img_jugador)
        label_img_j.image = self.img_jugador
        label_img_j.pack()

        tk.Label(frame_jugador, text=jugador.nombre).pack()

        self.label_puntos_jugador = tk.Label(frame_jugador, text=f"Puntos: {jugador.puntaje}")
        self.label_puntos_jugador.pack()

        # 🤖 CPU
        frame_cpu = tk.Frame(frame_superior)
        frame_cpu.pack(side="right", padx=20)

        self.img_cpu = tk.PhotoImage(file=cpu.avatar).subsample(3, 3)
        label_img_c = tk.Label(frame_cpu, image=self.img_cpu)
        label_img_c.image = self.img_cpu
        label_img_c.pack()

        tk.Label(frame_cpu, text=cpu.nombre).pack()

        self.label_puntos_cpu = tk.Label(frame_cpu, text=f"Puntos: {cpu.puntaje}")
        self.label_puntos_cpu.pack()

        # 🐉 FRAME DE COMBATE
        frame_combate = tk.Frame(self.ventana)
        frame_combate.pack(pady=20)

        # 🧑 Pokémon jugador
        self.img_pj = tk.PhotoImage(file=p_jugador.imagen).subsample(2, 2)

        frame_pj = tk.Frame(frame_combate)
        frame_pj.pack(side="left", padx=30)

        label_img_pj = tk.Label(frame_pj, image=self.img_pj)
        label_img_pj.image = self.img_pj
        label_img_pj.pack()

        tk.Label(frame_pj, text=p_jugador.nombre).pack()

        # VS
        tk.Label(frame_combate, text="VS", font=("Arial", 16)).pack(side="left", padx=10)

        # 🤖 Pokémon CPU
        self.img_pc = tk.PhotoImage(file=p_cpu.imagen).subsample(2, 2)

        frame_pc = tk.Frame(frame_combate)
        frame_pc.pack(side="right", padx=30)

        label_img_pc = tk.Label(frame_pc, image=self.img_pc)
        label_img_pc.image = self.img_pc
        label_img_pc.pack()

        tk.Label(frame_pc, text=p_cpu.nombre).pack()

        # ❤️ VIDA
        self.vida_jugador = tk.Label(self.ventana)
        self.vida_jugador.pack()

        self.vida_cpu = tk.Label(self.ventana)
        self.vida_cpu.pack()

        # 📢 RESULTADO
        self.label_resultado = tk.Label(self.ventana, text="")
        self.label_resultado.pack()

        # ⚔️ BOTÓN
        self.boton_atacar = tk.Button(self.ventana, text="Atacar", command=self.atacar)
        self.boton_atacar.pack(pady=10)

        self.actualizar_vida()

    def actualizar_vida(self):
        self.vida_jugador.config(
            text=f"{self.p_jugador.nombre} HP: {self.p_jugador.vida_actual}/{self.p_jugador.vida_maxima}"
        )
        self.vida_cpu.config(
            text=f"{self.p_cpu.nombre} HP: {self.p_cpu.vida_actual}/{self.p_cpu.vida_maxima}"
        )

    def actualizar_puntos(self):
        self.label_puntos_jugador.config(text=f"Puntos: {self.jugador.puntaje}")
        self.label_puntos_cpu.config(text=f"Puntos: {self.cpu.puntaje}")

    def atacar(self):

        if self.combate_terminado:
            return

        # jugador ataca
        daño = self.p_jugador.ataque - self.p_cpu.defensa
        if daño <= 0:
            daño = 1
        self.p_cpu.recibir_daño(daño)

        # cpu ataca
        if not self.p_cpu.esta_derrotado():
            daño = self.p_cpu.ataque - self.p_jugador.defensa
            if daño <= 0:
                daño = 1
            self.p_jugador.recibir_daño(daño)

        self.actualizar_vida()

        # 🔥 BLOQUE FINAL SEGURO
        if self.p_jugador.esta_derrotado() or self.p_cpu.esta_derrotado():

            if self.combate_terminado:
                return  # 🔒 doble protección

            self.combate_terminado = True

            self.boton_atacar.config(state="disabled")

            if self.p_jugador.esta_derrotado():
                self.label_resultado.config(text="Perdiste")
                self.ganador = self.p_cpu
                self.perdedor = self.p_jugador
                self.cpu.puntaje += 1
            else:
                self.label_resultado.config(text="Ganaste")
                self.ganador = self.p_jugador
                self.perdedor = self.p_cpu
                self.jugador.puntaje += 1

            self.actualizar_puntos()

            self.ventana.after(1500, self.ventana.destroy)

    def iniciar(self):
        self.ventana.mainloop()