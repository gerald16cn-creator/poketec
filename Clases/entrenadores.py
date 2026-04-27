import random
class Entrenador:

    def __init__(self, nombre, avatar):

        self.nombre = nombre
        self.avatar = avatar
        self.pokemons = []
        self.puntaje = 0

    def agregar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
    
    def quitar_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            self.pokemons.remove(pokemon)
    
    def tiene_pokemon_vivos(self):
        for p in self.pokemons:
            if not p.esta_derrotado():
                return True
        return False

    def obtener_pokemon_vivos(self):
        return [p for p in self.pokemons if not p.esta_derrotado()]
    
    def obtener_pokemon_vivo_random(self):
        vivos = [p for p in self.pokemons if not p.esta_derrotado()]
        if vivos:
            return random.choice(vivos)
        return None