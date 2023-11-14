import logging
import json
import os

Cur_Dir= os.path.dirname(__file__)
Data_file = os.path.join(Cur_Dir, "data", "movies.json")

def get_movies():
    
    with open(Data_file, "r") as f:
            movies_title = json.load(f)

    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies
    
class Movie:

    def __init__(self, title): #title == arguments (parametre)
        self.title = title.title()  #title==attribute instant .title==methode

    def __str__(self):
        return self.title
    
    def _get_movie(self):
        with open(Data_file, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(Data_file, "w") as f:
            json.dump(movies, f, indent=4)
    
    def add_to_movies(self):
        movies = self._get_movie()

        if self.title in movies:
            logging.warning(f"le film {self.title} est déjà dans la liste.")
            return False
        else:
            movies.append(self.title)
            self._write_movies(movies)
            return True
    
    def remove_from_movies(self):
        movies = self._get_movie()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        return False

    
if __name__ == "__main__":
    movies = get_movies()
    print(movies)