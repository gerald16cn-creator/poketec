class Pokemon:

    def __init__(self, nombre, vida, ataque, defensa, imagen):      #constructor de la clase
        self.nombre = nombre
        self.vida_maxima = vida
        self.vida_actual = vida
        self.ataque = ataque
        self.defensa = defensa
        self.imagen = imagen

    def recibir_daño(self, daño):           #Función que calcula el daño recibido, no devuelve valores negativos
        self.vida_actual -= daño
        if self.vida_actual < 0:
            self.vida_actual = 0

    def esta_derrotado(self):           #Pregunta si el pokemon tiene vida
        return self.vida_actual <= 0

    def revivir(self):                  #Revive al pokemon coo su vida máxima
        self.vida_actual = self.vida_maxima

    def __str__(self):
        return (f"{self.nombre} | HP: {self.vida_actual}/{self.vida_maxima} | "
                f"Ataque: {self.ataque} | Defensa: {self.defensa}")