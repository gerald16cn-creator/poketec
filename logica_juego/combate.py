def pelear(p1, p2):
    print(f"\n {p1.nombre} vs {p2.nombre}")

    while not p1.esta_derrotado() and not p2.esta_derrotado():
        # p1 ataca
        daño = p1.ataque - p2.defensa
        if daño <= 0:
            daño = 1
        p2.recibir_daño(daño)
        print(f"{p1.nombre} hace {daño} de daño a {p2.nombre}")

        if p2.esta_derrotado():
            break

        # p2 ataca
        daño = p2.ataque - p1.defensa
        if daño <= 0:
            daño = 1
        p1.recibir_daño(daño)
        print(f"{p2.nombre} hace {daño} de daño a {p1.nombre}")

    # resultado
    if p1.esta_derrotado():
        print(f"{p1.nombre} fue derrotado")
        return p2, p1  # ganador, perdedor
    else:
        print(f"{p2.nombre} fue derrotado")
        return p1, p2


def transferir_pokemon(ganador_entrenador, perdedor_entrenador, pokemon):
    print(f"{ganador_entrenador.nombre} ganó a {pokemon.nombre}")

    perdedor_entrenador.quitar_pokemon(pokemon)
    pokemon.revivir()
    ganador_entrenador.agregar_pokemon(pokemon)
    