def pelear(p1, p2):
    #print(f"\n {p1.nombre} vs {p2.nombre}")

    while not p1.esta_derrotado() and not p2.esta_derrotado():          #si ninguno de los pokemon está derrotado, entonces se repite el bucle
        #pokemon jugador ataca
        daño = p1.ataque - p2.defensa                   #se calcula el daño
        if daño <= 0:                                   #si el daño es 0 o negativo entonces lo fuerza a ser 1
            daño = 1
        p2.recibir_daño(daño)                           #llama a la función recibir daño para el pokemon 2

        if p2.esta_derrotado():                         #si el pokemon enemigo muere, se rompe el ciclo
            break

        # pokemon CPU ataca
        daño = p2.ataque - p1.defensa       #se calcula el daño
        if daño <= 0:                       #establece 1 como daño mínimo
            daño = 1
        p1.recibir_daño(daño)               #provoca daño al pokemon del jugador
        

    #cuando termina el ciclo de combate se establece el resultado

    if p1.esta_derrotado():                     #pregunta si el pokemon del jugador esta muerto
        
        return p2, p1               # si la respuesta es sí, estable al pokemon de la CPU como ganador, y al del jugador como perdedor
    
    else:                   
        return p1, p2   # si la respuesta es no, estable al pokemon del jugador como ganador, y al de la CPU como perdedor
    


def transferir_pokemon(ganador_entrenador, perdedor_entrenador, pokemon):   

    perdedor_entrenador.quitar_pokemon(pokemon)     #quita el pokemon perdedor de la lista de su entrenador
    pokemon.revivir()                               #le restaura la vida a este pokemon
    ganador_entrenador.agregar_pokemon(pokemon)     #lo incluye en la lista del otro entrenador
    