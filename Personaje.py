class Personaje:    
    # atributos del personaje
    def __init__(self, esp, nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    #metodos personaje
    def correr(self, status):
        if(status): 
            print("el personaje" + self.__nombre + "esta corriendo")
        else:
            print("el personaje"+ self.__nombre + " se detuvo")
    def lanzargranada(self):
        print("se lanzo granada")
    def Recargararma(self, municion):
        cargador= 5
        cargador= cargador + municion
        print("el arma tiene ahora"+ str(cargador) + "balas" )
    #EJEMPLO DE METODO PRIVADO
    def __pensar(self):
        print("hoy pensando.......")
        
        
    #DECLARACION  LOS GETTERS Y SETTERS DE ATRIBUTOS PRIVADO
    
    def getespecie(self):
        return self.__especie
    
    def setespecie(self,esp):
        self.__especie=esp
        
    def getnombre(self):
        return self.__nombre
    
    def setnombre(self, nom):
        self.__nombre=nom
        
    def getaltura(self):
        return self.__altura
    
    def setaltura(self, alt):
        self.__altura=alt
    
    
    
    