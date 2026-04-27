import json

RUTA = "data/puntajes.json"

def cargar_puntajes():
    try:
        with open(RUTA, "r") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_puntajes(puntajes):
    with open(RUTA, "w") as archivo:
        json.dump(puntajes, archivo, indent=4)

def agregar_puntaje(nombre, puntaje, avatar):
    puntajes = cargar_puntajes()

    nuevo = {
        "nombre": nombre,
        "puntaje": puntaje,
        "avatar": avatar
    }

    puntajes.append(nuevo)

    # ordenar de mayor a menor
    puntajes.sort(key=lambda x: x["puntaje"], reverse=True)

    # top 10
    puntajes = puntajes[:10]

    guardar_puntajes(puntajes)