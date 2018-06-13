# Creating instances for the movie class

import MovieClass
import fresh_tomatoes

avengers = MovieClass.Movie("Avengers : Infinity Wars\n", "https://www.youtube.com/watch?v=6ZfuNTqbHE8\n", "https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Avengers_%28Marvel_Comics%29_vol_3_num_38.jpg/220px-Avengers_%28Marvel_Comics%29_vol_3_num_38.jpg", "Thor,Iron Man & many more ...\n","3.8/5\n")

toy_story = MovieClass.Movie("Toy Story\n", "https://www.youtube.com/watch?v=KYz2wyBy3kc\n", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", "Thor,Iron Man & many more ...\n","3.8/5\n")

star_wars = MovieClass.Movie("Star Wars\n", "https://www.youtube.com/watch?v=jPEYpryMp2s\n", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/250px-Star_Wars_Logo.svg.png", "Thor,Iron Man & many more ...\n","3.8/5\n")

narnia = MovieClass.Movie("Narnia \n", "https://www.youtube.com/watch?v=pYcGFLgJ8Uo\n", "https://upload.wikimedia.org/wikipedia/en/thumb/c/cb/The_Chronicles_of_Narnia_box_set_cover.jpg/220px-The_Chronicles_of_Narnia_box_set_cover.jpg", "Thor,Iron Man & many more ...\n","3.8/5\n")

harry_potter = MovieClass.Movie("Harry Potter\n", "https://www.youtube.com/watch?v=K1KPcXRMMo4\n", "https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg/220px-Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg\n", "Thor,Iron Man & many more ...\n", "3.8/5\n")

ice_age = MovieClass.Movie("Ice Age\n", "https://www.youtube.com/watch?v=5utbt2Ycenw\n", "https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Ice_Age_%282002_film%29_poster.jpg/220px-Ice_Age_%282002_film%29_poster.jpg", "Thor,Iron Man & many more ...\n","3.8/5\n")

movies_list = [avengers, toy_story, star_wars, narnia, harry_potter, ice_age]

fresh_tomatoes.open_movies_page(movies_list)
