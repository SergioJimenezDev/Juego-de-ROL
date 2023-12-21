import random

#Creación de clases del juego
class Personaje:
    def __init__(self, nombre, nivel, vida_max, vida_actual, ataque, defensa, daño_critico, probabilidad_critico, velocidad, experiencia, experiencia_total, experiencia_subida_nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.vida_max = vida_max
        self.vida_actual = vida_actual
        self.ataque = ataque
        self.defensa = defensa
        self.daño_critico = daño_critico
        self.probabilidad_critico = probabilidad_critico
        self.velocidad = velocidad
        self.experiencia = experiencia
        self.experiencia_total = experiencia_total
        self.experiencia_subida_nivel = experiencia_subida_nivel

    def atacar(self,x):

        daño = random.randint(x-1, x+5)
        return daño
    
    def inventario(self):
        pass
        
    def mostrar_invetario(self):
        pass

    def subida_nivel(self, experiencia_sobrante):
        self.nivel = self.nivel + 1
        self.experiencia = experiencia_sobrante
        print(f"\n¡{self.nombre} ha subido al nivel {self.nivel}!")

    def xp_necesaria_nivel(self):
        experiencia_subida_nivel_2 = self.experiencia_subida_nivel * (1+(self.nivel/100)) * (self.nivel + 1)
        return experiencia_subida_nivel_2
            
    def experiencia_ganada(self):
        experiencia_subida_nivel = self.xp_necesaria_nivel()
        self.experiencia_total = self.experiencia_total + slime.experiencia_soltada
        self.experiencia = self.experiencia + slime.experiencia_soltada
        print(f"Experiencia obtenida: +{slime.experiencia_soltada}XP       |       Experiencia restante: {max((experiencia_subida_nivel - self.experiencia),0)}XP")
        if self.experiencia == experiencia_subida_nivel:
            experiencia_sobrante = self.experiencia - experiencia_subida_nivel
            self.subida_nivel(experiencia_sobrante)
        elif self.experiencia > experiencia_subida_nivel:
            while self.experiencia > experiencia_subida_nivel:
                experiencia_sobrante = self.experiencia - experiencia_subida_nivel
                self.subida_nivel(experiencia_sobrante)
                experiencia_subida_nivel = self.xp_necesaria_nivel()
                

class Enemigos:
    def __init__(self, vida_actual, ataque, experiencia_soltada):
        self.vida_actual = vida_actual
        self.ataque = ataque
        self.experiencia_soltada = experiencia_soltada

    def mostrar_vida(self, x):
        self.x = x
        if x <= 0:
            x = 0
            return x
        else:
            return x

class Zonas:
    def __init__(self, numero_zona, lista_zona):
        self.numero_zona = numero_zona
        self.lista_zona = lista_zona

    def mostrar_zona(self):
        return self.lista_zona[self.numero_zona-1]

    def mostrar_zona2(self, x):
        return self.lista_zona[x-1]
class Juego:
    def __init__(self, Zonas, Personaje, Enemigos):
        self.zonas = Zonas
        self.personaje = Personaje
        self.enemigos = Enemigos

class Combate:
    def __init__(self, combatiente1, combatiente2):
        self.combatiente1 = combatiente1
        self.combatiente2 = combatiente2

    def atacar_personaje(self):
        daño = random.randint(self.combatiente1.ataque-1, self.combatiente1.ataque+5)
        
        return daño

    def mostrar_vida(self, personaje, daño):
        vida_total = personaje.vida_actual - daño
        
        if vida_total <= 0:
            vida_total = 0
        else:
            vida_total
            
        return vida_total
    
    def atacar_monstruo(self):
        daño = random.randint(self.combatiente2.ataque-1, self.combatiente2.ataque+2)
        
        return daño
class Objeto:
    def __init__(self, nombre_objeto):
        self.nombre_objeto = nombre_objeto

#Objetos del juego
objeto_1 = Objeto("Poción de salud")

#CÓDIGO DEL JUEGO BASE

def codigo_juego(slime):
    while True:
        combate = Combate(personaje, slime)
        while combate.combatiente2.vida_actual > 0:
            print("\n\033[1m 1. Atacar\n", "2. Defender\n","3. Estadísticas de personaje\n","4. Volver al menú principal\033[0m\n")
            try:
                accion = input("acción: ")
            except ValueError:
                print("\n\033[7m\033[31mERROR: Introduce una acción válida.\033[0m\n")
                break
            if accion == "1":
                daño1 = combate.atacar_personaje()
                combate.combatiente2.vida_actual = combate.mostrar_vida(slime, daño1)
                print(f"\033[32m\033[1mTurno de {personaje.nombre}:\033[0m has hecho \033[32m\033[1m{daño1}\033[0m de daño. Vida restante del slime: \033[31m\033[1m{combate.combatiente2.vida_actual}\033[0m")
                daño2 = combate.atacar_monstruo()
                combate.combatiente1.vida_actual = combate.mostrar_vida(combate.combatiente1, daño2)
                print(f"\033[31m\033[1mTurno enemigo:\033[0m te han hecho \033[31m\033[1m{daño2}\033[0m de daño. Vida de {personaje.nombre} restante: \033[32m\033[1m{combate.combatiente1.vida_actual}\033[0m")
            elif accion == "2":
                print("JAJAJAJJAJAJAJAJJ que haces defendiendote maricon?")
                daño2 = combate.atacar_monstruo()
                combate.combatiente1.vida_actual = combate.mostrar_vida(combate.combatiente1, daño2)
                print("Te han hecho",daño2,"de daño por maricon. Tu vida restante es:",combate.combatiente1.vida_actual)
                pass
            elif accion == "3":
                print(f"\n\033[1m\033[4mEstadísticas de {personaje.nombre}:\033[0m\n")
                print(f"\033[37mNivel\033[0m: {personaje.nivel}")
                print(f"\033[32mVida:\033[0m {personaje.vida_max}")
                print(f"\033[31mDaño:\033[0m {personaje.ataque}")
                print(f"\033[34mDefensa:\033[0m {personaje.defensa}")
                print(f"\033[35mDaño Crítico:\033[0m {personaje.daño_critico}")
                print(f"\033[36mProbabilidad Crítico:\033[0m {personaje.probabilidad_critico}")
                print(f"\033[30mVelocidad:\033[0m {personaje.velocidad}")
                print(f"\033[33mExperiencia:\033[0m {personaje.experiencia}")
                print(f"Experiencia total: {personaje.experiencia_total}")
            elif accion == "4":
                print ("\n\033[7m\033[31mADVERTENCIA.\033[0m\n\nSi vuelves al menú principal perderás todos tus datos de la partida actual.")
                salir = input("\n¿Seguro que quieres volver al menú principal?\n\ns/n: ")
                if salir == "s":
                    return codigo_juego
                elif salir == "n":
                    pass
                else:
                    pass
            else:
                print("Elige un acción disponible")

            if combate.combatiente2.vida_actual <= 0:
                print("\n¡Slime eliminado!")
                personaje.experiencia_ganada()
                slime = Enemigos(40, 2, 20)
                break
#Menú principal
while True:
    nombre = input("\n¿Qué nombre le quieres poner al personaje?: ")
    personaje = Personaje(nombre, 1, 100, 100, 5, 1, 1.5, 0.1, 3, 0, 0, 100)
    slime = Enemigos(40, 2, 20)
    zona = Zonas(1, ["Bosque de las Sombras", "Ciudad de Cristal", "Montañas Rugientes"])
    juego = Juego(zona, personaje, slime)
    print("\nTu nombre es: ", juego.personaje.nombre)

    # Flag to break out of the inner loop
    salir_menu_principal = False

    while True:
        print("\n\033[7m\033[1m\033[32mMenú principal\033[0m\n")
        print("\033[1m 1. Nueva partida\n", "2. Opciones\n", "3. Instrucciones\n", "4. Salir del juego\n\033[0m")
        
        # Loop to handle non-numeric input
        while True:
            try:
                opcion = input("Elige una opción: ")
                break  # Break out of the input loop if conversion to int is successful
            except ValueError:
                print("\n\033[7m\033[31mERROR: Introduce una opción válida (número entero).\033[0m\n")

        # INTERIOR DEL JUEGO
        if opcion == "1":
            print("\033[1m 1. Bosque de las Sombras\n", "2. Ciudad de Cristal\n", "3. Montañas Rugientes\n", "4. Salir al menu Principal\n\033[0m")
            
            while True:
                juego.zonas.numero_zona = input("Elige el numero de la zona:")
                
                if juego.zonas.numero_zona == "4":
                    salir_menu_principal = True
                    break
                elif juego.zonas.numero_zona == "1":
                    codigo_juego(slime)
                elif juego.zonas.numero_zona == "2":
                    pass
                elif juego.zonas.numero_zona == "3":
                    pass
                else:
                    print("Elige una zona válida.")

            if salir_menu_principal:
                break

        elif opcion == 2:
            print("Por ahora no hay opciones")
            input("\nPresiona ENTER para volver al menú principal")
            pass
        elif opcion == 3:
            print("Por ahora, el juego es simple:\n" + "\nal atacar, tienes la posibilidad de hacer de 1-10 de daño, cuando el enemigo pierda toda la vida, habrás ganado.\n")
            input("\nPresiona ENTER para volver al menú principal")
            continue    
        elif opcion == 4:
            print("Saliendo del juego")
            break
        else:
            print("Por favor, seleccione una opción correcta\n\n " + "1. Entrar al juego\n", "2. Menú de opciones\n", "3. Instrucciones\n", "4. Salir del juego")