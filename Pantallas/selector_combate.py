import tkinter as tk

class SelectorCombate:

    def __init__(self, entrenador):
        self.entrenador = entrenador
        self.seleccionado = None

        self.ventana = tk.Tk()
        self.ventana.title("Elige tu Pokémon")

        tk.Label(self.ventana, text="Elige un Pokémon para combatir").pack()

        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        self.mostrar()

        tk.Button(self.ventana, text="Confirmar", command=self.confirmar).pack(pady=10)

    def mostrar(self):
        for i, p in enumerate(self.entrenador.pokemons):

            if p.esta_derrotado():
                continue

            img = tk.PhotoImage(file=p.imagen).subsample(3, 3)

            btn = tk.Button(
                self.frame,
                image=img,
                text=p.nombre,
                compound="top",
                command=lambda p=p: self.seleccionar(p)
            )

            btn.image = img
            btn.grid(row=0, column=i, padx=10, pady=10)

    def seleccionar(self, pokemon):
        self.seleccionado = pokemon
        print(f"Seleccionado: {pokemon.nombre}")

    def confirmar(self):
        if self.seleccionado:
            self.ventana.destroy()

    def obtener(self):
        self.ventana.mainloop()
        return self.seleccionado