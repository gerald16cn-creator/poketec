from Pantallas.pantalla_puntajes import PantallaPuntajes
from Utilidades.puntajes import agregar_puntaje
from Pantallas.pantalla_batalla import PantallaBatalla
from Pantallas.selector_combate import SelectorCombate
from logica_juego.combate import transferir_pokemon


# 🤖 CPU elige Pokémon random
def elegir_pokemon_cpu(entrenador):
    return entrenador.obtener_pokemon_vivo_random()


# 🧑 JUGADOR elige Pokémon en pantalla
def elegir_pokemon_jugador(entrenador):
    selector = SelectorCombate(entrenador)
    return selector.obtener()


def juego(jugador, cpu):

    while jugador.tiene_pokemon_vivos() and cpu.tiene_pokemon_vivos():

        print("\n========================")
        print(f"{jugador.nombre}: {len(jugador.pokemons)} Pokémon")
        print(f"CPU: {len(cpu.pokemons)} Pokémon")
        print("========================")

        # 🧑 elegir Pokémon
        p_jugador = elegir_pokemon_jugador(jugador)
        if p_jugador is None:
            continue  # seguridad

        p_cpu = elegir_pokemon_cpu(cpu)

        print(f"\n{jugador.nombre} eligió: {p_jugador.nombre}")
        print(f"CPU eligió: {p_cpu.nombre}")

        # ⚔️ batalla
        pantalla = PantallaBatalla(jugador, cpu, p_jugador, p_cpu)
        pantalla.iniciar()

        ganador = pantalla.ganador
        perdedor = pantalla.perdedor

        # 🔥 VALIDACIÓN CLAVE (evita bug del contador)
        if ganador is None or perdedor is None:
            continue

        # 🔁 transferir Pokémon
        if ganador == p_jugador:
            transferir_pokemon(jugador, cpu, perdedor)
        else:
            transferir_pokemon(cpu, jugador, perdedor)

    # 🏁 fin del juego
    if jugador.tiene_pokemon_vivos():
        print("\n GANASTE")
    else:
        print("\n PERDISTE")

    # 💾 guardar puntaje
    agregar_puntaje(jugador.nombre, jugador.puntaje, jugador.avatar)

    # 🏆 mostrar ranking
    pantalla = PantallaPuntajes()
    pantalla.iniciar()