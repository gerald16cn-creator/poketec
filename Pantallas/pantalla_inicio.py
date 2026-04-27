import tkinter as tk

class PantallaInicio:

    def __init__(self):
        self.nombre = None
        self.avatar = None

        self.ventana = tk.Tk()
        self.ventana.title("Inicio")

        tk.Label(self.ventana, text="Ingresa tu nombre").pack(pady=5)

        self.entry = tk.Entry(self.ventana)
        self.entry.pack(pady=5)

        tk.Label(self.ventana, text="Elige tu avatar").pack(pady=10)

        self.frame_avatares = tk.Frame(self.ventana)
        self.frame_avatares.pack()

        self.cargar_avatares()

        tk.Button(self.ventana, text="Continuar", command=self.continuar).pack(pady=10)

    def cargar_avatares(self):
        rutas = [
            "Imagenes/avatares/avatar1.png",
            "Imagenes/avatares/avatar2.png",
            "Imagenes/avatares/avatar3.png",
            "Imagenes/avatares/avatar4.png",
            "Imagenes/avatares/avatar5.png",
        ]

        for i, ruta in enumerate(rutas):
            try:
                img = tk.PhotoImage(file=ruta).subsample(3, 3)
            except:
                print(f"Error cargando {ruta}")
                continue

            btn = tk.Button(
                self.frame_avatares,
                image=img,
                command=lambda r=ruta: self.seleccionar_avatar(r)
            )

            btn.image = img
            btn.grid(row=0, column=i, padx=5)

    def seleccionar_avatar(self, ruta):
        self.avatar = ruta
        print(f"Avatar seleccionado: {ruta}")

    def continuar(self):
        nombre = self.entry.get().strip()

        if not nombre:
            print("Ingresa un nombre")
            return

        if not self.avatar:
            print("Selecciona un avatar")
            return

        self.nombre = nombre
        self.ventana.destroy()

    def iniciar(self):
        self.ventana.mainloop()
        return self.nombre, self.avatar