class Personaje:
    # atributos del personaje
    especie= "humano"
    nombre= "marcus fenix"
    altura= 1.90
    
    #metodos personaje
    def correr(self, status):
        if(status): 
            print("el personaje" + self.nombre + "esta correindo")
        else:
            print("el personaje"+ self.nombre + " se detuvo")
    def lanzargranada(self):
        print("se lanzo granada")
    def Recargararma(self, municion):
        cargador= 5
        cargador= cargador + municion
        print("el arma tiene ahora"+ cargador + "balas" )