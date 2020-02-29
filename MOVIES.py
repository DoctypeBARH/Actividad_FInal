#Importacion de Random
import random
dic_pelis={}
class Movie:
    """Esta es la clases que se encargara de darle los rangos 
        , los likes y los dislikes desde varios metodos
         - Crear una clase llamada Movie (documentar la clase)
         - La clase tiene los siguientes atributos:
         - Title - Titulo de la pelicula en minusculas
         - Rank - Rango inicial de la pelicula un random de 0 a 10
    """
    def __init__ (self,titulo,rango=6):
        self.titulo=titulo.title()
        self.rango=rango
    # y los siguientes Metodos (documentarlos):
    #- Like - Aumenta en 1 el Rank de la pelicula 
    #- Dislike - Reduce en 1 el Rank de la pelicula
    #- Display - Muestra el titulo de la pelicula con Mayuscula la primer letra de cada palabra y el Rank.
  
    def like (self):
        """Este metodo incrementa 1 punto a la pelicula """
        print("Metodo LIKE")
        print("El rango se la Pelicula",self.titulo,"es",self.rango)
        if self.rango>=10:
            print("El rango de la Pelicula",self.titulo,"esta al maximo y es",self.rango)
        else:
            self.rango=self.rango+1
            print("El rango de la Pelicula",self.titulo,"aumento y ahora es",self.rango)
            print("....................................................................")
    def dislike(self):
        """Este metodo desincrementa 1 punto a la pelicula"""
        print("Metodo DISLIKE")
        print("El rango de la Pelicula",self.titulo,"es",self.rango)
        self.rango=self.rango-1
        print("El rango de la Pelicula",self.titulo,"disminuyo y ahora es",self.rango)
        print("....................................................................")
    def display(self):
        print("Pelicula:",self.titulo.title())
        print("Rango:",self.rango)
        print("___________________________________________________________________")
    pass
def rank():
    rango=(random.randint(0, 10))
    return rango



p=Movie("Terminator",rank())
p2=Movie("alicia en el Pais de las Maravillas",rank())
p3=Movie("Avengers era de ultron",rank())
p4=Movie("los cuatro fantasticos",rank())
p5=Movie("soy leyenda",rank())
p6=Movie("joker",rank())
p7=Movie("Batman el caballero de la noche asciende",rank())
p8=Movie("buccando a nemo",rank())
p9=Movie("red social",rank())
p10=Movie("La pimpinela escarlata",rank())
p11=Movie("escuadron suicida",rank())
p12=Movie("Avengers the end game",rank())


peliculas=[p,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]
for peli in peliculas:
    peli.like()
    peli.like()
    peli.dislike()
    peli.display()
#definimos un a lista para guardar solo los titulos de nuestras peliculas
ptitulos=[]
ptitulos=[p.titulo,p2.titulo,p3.titulo,p4.titulo,p5.titulo,p6.titulo,p7.titulo,p8.titulo,p9.titulo,p10.titulo,p11.titulo]#Agrgamos a la lista nuestrso titulos
peliculass=sorted(ptitulos)











