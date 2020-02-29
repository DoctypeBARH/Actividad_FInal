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
    pass
