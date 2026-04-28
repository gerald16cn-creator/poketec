from Pantallas.pantalla_inicio import PantallaInicio
from Pantallas.seleccion_pokemon import VentanaSeleccion
from Clases.entrenadores import Entrenador
from data.pokemones import POKEMONS_DISPONIBLES
from logica_juego.juego import juego
import random


#Pantalla de inicio (nombre + avatar)
inicio = PantallaInicio()
nombre, avatar = inicio.iniciar()

# validacion 
if not nombre or not avatar:
    print("Inicio cancelado")
    exit()

# crear entrenadores
jugador = Entrenador(nombre, avatar)
cpu = Entrenador("CPU", "Imagenes/avatares/avatar1.png")


# selecciona 3 pokemones
seleccion = VentanaSeleccion(jugador)
pokemones_elegidos = seleccion.obtener_seleccion()

#validacion importante
if not pokemones_elegidos or len(pokemones_elegidos) != 3:
    print("Selección inválida")
    exit()

# agregar pokemons a la lista del jugador
for p in pokemones_elegidos:
    jugador.agregar_pokemon(p)


# obtener pokémon del jugador
pokemones_jugador = jugador.pokemons

# filtrar disponibles para CPU
disponibles_cpu = [p for p in POKEMONS_DISPONIBLES if p not in pokemones_jugador]

# cpu elije tres pokemons
cpu_pokemones = random.sample(disponibles_cpu, 3)

for p in cpu_pokemones:
    cpu.agregar_pokemon(p)


# iniciar juego
juego(jugador, cpu)