#Crear una carpeta que se llame clases y dentro poner los archivos dino.py y persona.py

#Crear una clase persona() en el archivo persona.py que tenga como atributos 
# nombre, edad y profesion
#Al instanciar la clase tiene que saludar igul que el dino diciendo sus
#atributos

class Persona:
    def __init__(self, un_nombre="", una_edad="", una_profesion=""):
        self.nombre=un_nombre
        self.edad=una_edad
        self.profesion=una_profesion
        print ("Hola me llamo", self.nombre, "tengo", self.edad, "años", "y mi profesion es", self.profesion)



Var= Persona("Hèrika", 16, "estudiante")
