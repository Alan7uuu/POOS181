class Personaje:    
    # atributos del personaje
    def __init__(self, esp, nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
    
    #metodos personaje
    def correr(self, status):
        if(status): 
            print("el personaje" + self.nombre + "esta corriendo")
        else:
            print("el personaje"+ self.nombre + " se detuvo")
    def lanzargranada(self):
        print("se lanzo granada")
    def Recargararma(self, municion):
        cargador= 5
        cargador= cargador + municion
        print("el arma tiene ahora"+ str(cargador) + "balas" )