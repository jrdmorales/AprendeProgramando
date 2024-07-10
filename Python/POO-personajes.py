class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def Atributos(self):
        print(self.nombre, ":" , sep="")
        print("-Vida: ", self.vida)
        print("-Ataque: ", self.ataque)
        print("-Defensa: ", self.defensa)

    def SubirNivel(self):
        self.vida += 10
        self.ataque += 2
        self.defensa += 1

    
    def esta_vivo(self):
        return self.vida > 0
    

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.ataque - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ataca a", enemigo.nombre, "y le hace", daño, "puntos de daño")
        if enemigo.esta_vivo():
            print(enemigo.nombre, "tiene", enemigo.vida, "puntos de vida")
        else:
            enemigo.morir()
    

#Mi Personaje Se llama Aragorn y tiene 100 de vida, 20 de ataque y 10 de defensa   
mi_personaje = Personaje('Aragorn', 100, 20, 10)
print(mi_personaje.Atributos())

#Mi enemigo se llama Sauron y tiene 200 de vida, 30 de ataque y 15 de defensa
mi_enemigo = Personaje('Sauron', 100, 30, 15)
print(mi_enemigo.Atributos())

#Aragorn ataca a Sauron
mi_personaje.atacar(mi_enemigo)


class Guerrero(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, espada):
        #Llama al constructor de la clase padre
        super().__init__(nombre, vida, ataque, defensa)
        self.espada = espada

    def cambiar_botas(self, espada, ataque, defensa):
        opcion = int(input("Elige una opción: \n1. Botas de cuero (+10 de espada)\n2. Botas de hierro (+13 de espada)\n"))
        if opcion == 1:
            self.espada = espada + 10
        elif opcion == 2: 
            self.espada = espada + 13
        else:
            print("Opción no válida")

    def Atributos(self):
        #Llama al metodo Atributos de la clase padre
        super().Atributos()
        print("-Espada: ", self.espada)


    def daño(self, enemigo):
        #Calcula el daño que hace el guerrero
        return self.ataque + self.espada - enemigo.defensa
    
class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, hechizo):
        super().__init__(nombre, vida, ataque, defensa)
        self.hechizo = hechizo

    def cambiar_hechizo(self, hechizo):
        opcion = int(input("Elige una opción: \n1. Rayo (+10 de hechizo)\n2. Bola de fuego (+13 de hechizo)\n"))
        if opcion == 1:
            self.hechizo = hechizo + 10
        elif opcion == 2: 
            self.hechizo = hechizo + 13
        else:
            print("Opción no válida")

    def Atributos(self):
        super().Atributos()
        print("-Hechizo: ", self.hechizo)

    def daño(self, enemigo):
        return self.ataque + self.hechizo - enemigo.defensa
    

#nombre Guerrero 
personaje1 = Guerrero('Goku', 100, 20, 10, 10)
print(personaje1.Atributos())

#nombre Mago
personaje2 = Mago('Gandalf', 100, 20, 10, 10)
print(personaje2.Atributos())

def Combate(personaje1, personaje2):
    turno = 0
    while personaje1.esta_vivo() and personaje2.esta_vivo():
        print("Turno", turno)
        print("--- Accion de", personaje1.nombre, ":" , sep="")
        personaje1.atacar(personaje2)
        print("--- Accion de", personaje2.nombre, ":" , sep="")
        personaje2.atacar(personaje1)
        turno += 1
    if personaje1.esta_vivo():
        print(personaje1.nombre, "ha ganado")
    elif personaje2.esta_vivo():
        print(personaje2.nombre, "ha ganado")
    else:
        print("Empate")



Combate(personaje1, personaje2)



    
