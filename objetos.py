#1. importar la clase
from Personaje import *

#2. instanciar un objeto
heroe= Personaje()

#3. acceder a sus atributos
print("el personaje pertenece a la raza:"+ heroe.especie)
print("el nombre del personajes es:"+ heroe.nombre)
print("La estatura es:"+ str(heroe.altura)+ " metros")

#4.acceder a los metodos
heroe.correr(True)
heroe.lanzargranada
heroe.Recargararma(12)
