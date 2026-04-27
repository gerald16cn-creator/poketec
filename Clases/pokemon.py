class Pokemon:

    def __init__(self, nombre, vida, ataque, defensa, imagen):
        self.nombre = nombre
        self.vida_maxima = vida
        self.vida_actual = vida
        self.ataque = ataque
        self.defensa = defensa
        self.imagen = imagen

    def recibir_daño(self, daño):
        self.vida_actual -= daño
        if self.vida_actual < 0:
            self.vida_actual = 0

    def esta_derrotado(self):
        return self.vida_actual <= 0

    def revivir(self):
        self.vida_actual = self.vida_maxima

    def __str__(self):
        return (f"{self.nombre} | HP: {self.vida_actual}/{self.vida_maxima} | "
                f"Ataque: {self.ataque} | Defensa: {self.defensa}")