Movies=[]
class Movie:
    """Esta es la clases que se encargara de darle los rangos 
        , los likes y los dislikes desde varios metodos
         - Crear una clase llamada Movie (documentar la clase)
         - La clase tiene los siguientes atributos:
         - Title - Titulo de la pelicula en minusculas
         - Rank - Rango inicial de la pelicula un random de 0 a 10
    """
    def __init__ (self,titulo,rango):
        self.titulo=titulo
        self.rango=rango
    # y los siguientes Metodos (documentarlos):
    #- Like - Aumenta en 1 el Rank de la pelicula 
    #- Dislike - Reduce en 1 el Rank de la pelicula
    #- Display - Muestra el titulo de la pelicula con Mayuscula la primer letra de cada palabra y el Rank.
  
    def like (self):
        """Este metodo incrementa 1 punto a la pelicula """
        print("El rango se la Pelicula",self.titulo,"es",self.rango)
        self.rango=+1
        print("El rango se la Pelicula",self.titulo,"aumento y ahora es",self.rango)
    def dislike(self):
        """Este metodo desincrementa 1 punto a la pelicula"""
        print("El rango se la Pelicula",self.titulo,"es",self.rango)
        self.rango=-1
        print("El rango se la Pelicula",self.titulo,"aumento y ahora es",self.rango)
    def display(self):
        print("Pelicula:",self.titulo.title())
        print("Rango:",self.rango)
        Movies.append(self.titulo.title())

    pass



