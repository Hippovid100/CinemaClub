from PySide2 import QtWidgets, QtCore
from movie import Movie, get_movies

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.setup_connections()
        self.populate_movies()
        

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.line_edit_Movietitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.List_movies = QtWidgets.QListWidget()
        self.List_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.line_edit_Movietitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.List_movies)
        self.layout.addWidget(self.btn_removeMovies)
    
    def setup_connections(self):
        self.line_edit_Movietitle.returnPressed.connect(self.add_movie)
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movies)
    
    def populate_movies(self):
        movies = get_movies()
        
        # for movie in movies: ##(une façon faire)
        #     self.List_movies.addItem(movie.title)

        for movie in movies: ##(une façon faire)
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.List_movies.addItem(lw_item)
    
    def add_movie(self):
        movie_title = self.line_edit_Movietitle.text()
        if not movie_title:
            return False
        
        movie = Movie(title=movie_title)
        resultat = movie.add_to_movies()

        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.List_movies.addItem(lw_item)
        
        self.line_edit_Movietitle.setText("")
            
    def remove_movies(self):
        for selected_item in self.List_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.List_movies.takeItem(self.List_movies.row(selected_item))
        
        

app = QtWidgets.QApplication([]) # il faut obligé de passer une liste vide
win = App()  #créer une instance
win.show()   # affice instance avec méthode show
app.exec_()  # execute 