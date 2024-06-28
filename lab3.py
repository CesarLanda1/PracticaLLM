'''DEFINICIÓN DE CLASES Y OBJETOS'''
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.set_edad(edad)
        self.ciudad = ciudad
    def presentarse(self): #metodo1
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad}.")
    
    def cumplir_años(self): #metodo2
        self.edad += 1
    
    def cambiar_ciudad(self, nueva_ciudad): #metodo3
        self.ciudad = nueva_ciudad
     
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad1):
        if edad1 >= 0:
            self.edad = edad1
        else:
            print("La edad debe ser un valor mayor o igual a 0.")

'''Creación de Objetos'''
persona1 = Persona("Juan", 25, "Lima")
persona2 = Persona("Maria", 30, "Arequipa")
persona3 = Persona("Pedro", 35, "Cusco")

'''Acceder a objetos'''
print(f"Accedo a Persona1: {persona1.nombre} con {persona1.edad} y de {persona1.ciudad}")

'''Modificar objetos'''
persona1.nombre = "Luis"
persona1.edad = 31
print(f"Modifico Persona1, ahora es: {persona1.nombre} de {persona1.edad} y de {persona1.ciudad}")

'''Llamar a metodos creados en los objetos'''
persona1.presentarse()
persona2.cumplir_años()
persona3.cambiar_ciudad("Tacna")
print(f"Cambio de ciudad para Persona3: {persona3.nombre}, {persona3.edad}, {persona3.ciudad}")

'''Herencia de clase Persona'''
class Estudiante(Persona):
    def __init__(self, nombre, edad, ciudad, grado):
        super().__init__(nombre, edad, ciudad)
        self.grado = grado #agregar atributo grado
    def estudiar(self): #metodo estudiar
        print(f"{self.nombre} esta estudiando en el {self.grado} grado.")

estudiante1 = Estudiante("Carlos", 20, "Puno", "5") #Objeto de la clase Estudiante

'''Metodos heredados'''
estudiante1.presentarse()
estudiante1.cumplir_años()
estudiante1.cambiar_ciudad("Arequipa")
print(f"Estudiante1 es {estudiante1.nombre} con {estudiante1.edad} de {estudiante1.ciudad} y en el {estudiante1.grado} grado")

estudiante1.estudiar() # Llamar al método específico de la clase Estudiante

'''Encapsulamiento'''
# Probar los métodos get_edad y set_edad
print(persona1.get_edad())

persona1.set_edad(30)
print(persona1.get_edad())

'''POLIMORFISMO'''
class Animal: #clase animal
    def hacer_sonido(self):
        print("Sonido  de animal")

class Perro(Animal): #clase hija1
    def hacer_sonido(self):
        print("El perro hace: ¡Guau guau!")

class Gato(Animal): #clase hija2
    def hacer_sonido(self):
        print("El gato hace: ¡Miau miau!")

def hacer_que_suenen(animales): #funcion hacer que suenen
    for animal in animales:
        animal.hacer_sonido()

perro1 = Perro()
gato1 = Gato()

animales = [perro1, gato1] #lista de objetos animal

hacer_que_suenen(animales) #lista con funcion

