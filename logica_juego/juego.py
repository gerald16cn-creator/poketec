from Pantallas.pantalla_puntajes import PantallaPuntajes
from Utilidades.puntajes import agregar_puntaje
from Pantallas.pantalla_batalla import PantallaBatalla
from Pantallas.selector_combate import SelectorCombate
from logica_juego.combate import transferir_pokemon



def elegir_pokemon_cpu(entrenador):                     #llama a otra función para elegir entre los pokemon de la CPU
    return entrenador.obtener_pokemon_vivo_random()


def elegir_pokemon_jugador(entrenador):        #Crea una ventana (SelectorCombate) para que el jugador seleccione y devuelve el Pokémon elegido. 
    selector = SelectorCombate(entrenador)
    return selector.obtener()


def juego(jugador, cpu):

    while jugador.tiene_pokemon_vivos() and cpu.tiene_pokemon_vivos():  #Mientras ambos entrenadores tengan al menos un pokemon disponible el bucle continua


        p_jugador = elegir_pokemon_jugador(jugador)         #El jugador selecciona un pokemon
        if p_jugador is None:               #si no selecciona ninguna entonces reinicia el ciclo
            continue  

        p_cpu = elegir_pokemon_cpu(cpu)     #la CPU elige un pokemon al azar


        #Batalla
        pantalla = PantallaBatalla(jugador, cpu, p_jugador, p_cpu) #se crea y se inicia la pantalla de batalla (la ventana de Tkinter donde ocurre el combate).
        pantalla.iniciar()

        ganador = pantalla.ganador      #cuando la batalla termina se obtiene el perdedor y el ganador
        perdedor = pantalla.perdedor


        if ganador is None or perdedor is None:     #si por un motivo cualquiera no hay ganador, se reinicia el ciclo
            continue

        #transferir pokemon
        if ganador == p_jugador:
            transferir_pokemon(jugador, cpu, perdedor)
        else:
            transferir_pokemon(cpu, jugador, perdedor)


    agregar_puntaje(jugador.nombre, jugador.puntaje, jugador.avatar)    #se guarda el puntaje

    
    pantalla = PantallaPuntajes()  #se inicia la pantalla de puntajes
    pantalla.iniciar()