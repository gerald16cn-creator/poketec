import random
class Entrenador:               #la clase "Entrenador" aplica tanto para el jugador como para la cpu

    def __init__(self, nombre, avatar):     #Constructor de la clase

        self.nombre = nombre
        self.avatar = avatar
        self.pokemons = []
        self.puntaje = 0

    def agregar_pokemon(self, pokemon):         #función que añade los 3 pokemon iniciales         
        self.pokemons.append(pokemon)
    
    def quitar_pokemon(self, pokemon):          #función que elimina pokemon cuando se pierde batalla
        if pokemon in self.pokemons:
            self.pokemons.remove(pokemon)
    
    def tiene_pokemon_vivos(self):          #función que verifica si aún el entrenador puede pelear
        for p in self.pokemons:
            if not p.esta_derrotado():
                return True
        return False

    def obtener_pokemon_vivos(self):                                #Devuelve una lista con los pokemon vivos del jugador
        return [p for p in self.pokemons if not p.esta_derrotado()]
    
    def obtener_pokemon_vivo_random(self):                           #Crea una lista con los pokemon del rival, si esta vacía retorna nada y y si tiene al menos un elemento retorna un elemento al azar
        vivos = [p for p in self.pokemons if not p.esta_derrotado()]
        if vivos:
            return random.choice(vivos)
        return None