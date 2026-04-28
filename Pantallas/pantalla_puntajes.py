import tkinter as tk
from Utilidades.puntajes import cargar_puntajes

class PantallaPuntajes:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Mejores Puntajes")
        self.ventana.geometry("1000x300")  # opcional, para que quepa todo

        tk.Label(self.ventana, text=" TOP 10 ", font=("Arial", 16)).pack(pady=10)

        # contenedor principal para la fila horizontal
        contenedor = tk.Frame(self.ventana)
        contenedor.pack()

        puntajes = cargar_puntajes()

        for i, p in enumerate(puntajes):

            # cada jugador es una "columna"
            frame = tk.Frame(contenedor)
            frame.grid(row=0, column=i, padx=10, pady=10)

            # avatar
            try:
                img = tk.PhotoImage(file=p["avatar"]).subsample(4, 4)
                label_img = tk.Label(frame, image=img)
                label_img.image = img  # 🔥 MUY IMPORTANTE
                label_img.pack()
            except:
                print(f"Error cargando avatar: {p['avatar']}")

            # nombre y puntaje
            texto = f"{i+1}. {p['nombre']}\n{p['puntaje']} pts"
            tk.Label(frame, text=texto, font=("Arial", 10)).pack()

    def iniciar(self):
        self.ventana.mainloop()