#1. importar la clase
from Personaje import *
#2. solicitar atributos para el objeto
print("")
print("### solicitud de datos del heroe ###")
espH= input("Escribe la especie del heroe:")
nomH= input("Escribe el nombre del heroe:")
altH= float(input("Escribe la altura del heroe:"))
cargaH= int(input("cuantas balas se recargaran al heroe:"))



print("")
print("### solicitud de datos del villano ###")
espV= input("Escribe la especie del villano:")
nomV= input("Escribe el nombre del villano:")
altV= float(input("Escribe la altura del villano:"))
cargaV= int(input("cuantas balas se recargaran al villano :"))

#3. creamos 2 objetos
heroe= Personaje(espH,nomH,altH)
villano= Personaje(espV,nomV,altV)
heroe.setnombre("pepe pecas")



#3. acceder a sus atributos Y  metodos de cada OBJ
#HEROE
print("")
print("## Atributos y Metodos del Heroe ##")
print("el personaje pertenece a la raza:"+ heroe.getespecie())
print("el nombre del personajes es:"+ heroe.getnombre())
print("La estatura es:"+ str(heroe.getaltura())+ " metros")
heroe.correr(True)
heroe.lanzargranada
heroe.Recargararma(cargaH)
#ejemplo de lo que no se puede hacer

#heroe.__pensar()

#VILLANO
print("")
print("## Atributos y Metodos del Villano ##")
print("el personaje pertenece a la raza:"+ villano.getespecie())
print("el nombre del personajes es:"+ villano.getnombre())
print("La estatura es:"+ str(villano.getaltura())+ " metros")
heroe.correr(False)
heroe.lanzargranada
heroe.Recargararma(cargaV)