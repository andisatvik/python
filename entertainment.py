# Creating instances for the movie class

import MovieClass

def insert_movies():
    
    Avengers = MovieClass.Movie("Avengers : Infinity Wars", "https://www.youtube.com/watch?v=6ZfuNTqbHE8", "Thor,Iron Man & many more ...","3.8/5")
    print(Avengers.name, Avengers.trailer, Avengers.cast, Avengers.rating)

insert_movies()
