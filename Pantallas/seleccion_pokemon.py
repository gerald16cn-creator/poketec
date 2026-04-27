from data.pokemones import POKEMONS_DISPONIBLES
import tkinter as tk

class VentanaSeleccion:

    def __init__(self, entrenador):
        self.entrenador = entrenador

        # ✅ lista de seleccionados
        self.pokemones_seleccionados = []

        self.ventana = tk.Tk()
        self.ventana.title("Selecciona 3 Pokémon")

        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        self.mostrar_pokemones()

        # botón confirmar
        self.boton_confirmar = tk.Button(
            self.ventana,
            text="Confirmar",
            command=self.confirmar
        )
        self.boton_confirmar.pack(pady=10)

    def seleccionar_pokemon(self, pokemon):
        if pokemon in self.pokemones_seleccionados:
            print("Ya lo elegiste")
            return

        if len(self.pokemones_seleccionados) < 3:
            self.pokemones_seleccionados.append(pokemon)
            print(f"Elegiste: {pokemon.nombre}")
        else:
            print("Ya seleccionaste 3")

    def mostrar_pokemones(self):
        vivos = POKEMONS_DISPONIBLES

        for i, p in enumerate(vivos):
            try:
                imagen = tk.PhotoImage(file=p.imagen).subsample(3, 3)
            except:
                print(f"Error cargando imagen: {p.imagen}")
                continue

            boton = tk.Button(
                self.frame,
                image=imagen,
                text=p.nombre,
                compound="top",
                command=lambda p=p: self.seleccionar_pokemon(p)
            )

            boton.image = imagen
            boton.grid(row=i // 5, column=i % 5, padx=10, pady=10)

    def confirmar(self):
        if len(self.pokemones_seleccionados) == 3:
            self.ventana.destroy()
        else:
            print("Debes elegir 3 Pokémon")

    def obtener_seleccion(self):
        self.ventana.mainloop()
        return self.pokemones_seleccionados