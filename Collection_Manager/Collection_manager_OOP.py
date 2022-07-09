class MovieData:
    def __init__(self, movie_name, year, director, time, country, movie_type, main_actor):
        self.movie_name = movie_name
        self.year = year
        self.director = director
        self.time = time
        self.country = country
        self.type = movie_type
        self.main_actor = main_actor


class MoviesManager:
    def __init__(self):
        self.movies_array = []
        self._save_array = []

    def save_movie(self, current_movie: MovieData):
        if current_movie not in self.movies_array:
            self.movies_array.append(current_movie)
            info = ""
            for i in self.movies_array:
                if i not in self._save_array:
                    self._save_array.append(f"Movie: {i.movie_name}, Year: {i.year}, Director: {i.director}, "
                                            f"Time: {i.time}, Country: {i.country}, Type: {i.type},"
                                            f" Main Actor: {i.main_actor}.")
            for i in self._save_array:
                info += "".join(i)
                info += "\n"
            with open('movies_collector.txt', 'w') as file:
                file.write(info)
        self._save_array.clear()

    def remove_movie(self, name, year):
        for i in self.movies_array:
            with open('movies_collector.txt', 'r+') as file:
                if i.movie_name == name and i.year == year:
                    self.movies_array.remove(i)
                    lines = file.readlines()
                    file.seek(0)
                    for k in lines:
                        if str(year) not in k:
                            file.write(k)
                    file.truncate()
                    return f"Movie: {name} has been deleted from your movie collector."
        return "This movie does not exist!"


class GameData:
    def __init__(self, game_name, year, creator):
        self.game_name = game_name
        self.year = year
        self.creator = creator


class GamesManager:
    def __init__(self):
        self.games_array = []
        self._save_array = []

    def save_game(self, current_game: GameData):
        if current_game not in self.games_array:
            self.games_array.append(current_game)
            info = ""
            for i in self.games_array:
                if i not in self._save_array:
                    self._save_array.append(f"Game: {i.game_name}, Year: {i.year}, Creator: {i.creator}")
            for i in self._save_array:
                info += "".join(i)
                info += "\n"
            with open('games_collector.txt', 'w') as file:
                file.write(info)
        self._save_array.clear()

    def remove_game(self, name, year):
        for i in self.games_array:
            with open('games_collector.txt', 'r+') as file:
                if i.game_name == name and i.year == year:
                    self.games_array.remove(i)
                    lines = file.readlines()
                    file.seek(0)
                    for k in lines:
                        if str(year) not in k:
                            file.write(k)
                    file.truncate()
                    return f"Game: {name} has been deleted from your game collector."
        return "This game does not exist!"


class BookData:
    def __init__(self, book_name, author, year, genre):
        self.book_name = book_name
        self.author = author
        self.year = year
        self.genre = genre


class BooksManager:
    def __init__(self):
        self.books_array = []
        self._save_array = []

    def save_book(self, current_book: BookData):
        if current_book not in self.books_array:
            self.books_array.append(current_book)
            info = ""
            for i in self.books_array:
                if i not in self._save_array:
                    self._save_array.append(f"Book: {i.book_name}, Year: {i.year}, Author: {i.author},"
                                            f"Genre: {i.genre}")
            for i in self._save_array:
                info += "".join(i)
                info += "\n"
            with open('books_collector.txt', 'w') as file:
                file.write(info)
        self._save_array.clear()

    # def search_book(self, name):
    #     for i in self.books_array:
    #         if i.book_name == name:
    #             return f"{i.book_name} exists in your library."
    #     return f"{name} is not in your library!"

    def remove_book(self, name, year):
        for i in self.books_array:
            with open('books_collector.txt', 'r+') as file:
                if i.book_name == name and i.year == year:
                    self.books_array.remove(i)
                    lines = file.readlines()
                    file.seek(0)
                    for k in lines:
                        if str(year) not in k:
                            file.write(k)
                    file.truncate()
                    return f"Book: {name} has been deleted from your book collector."
        return "This book does not exist!"


# Movie Tests
movie = MovieData('Titanic', 1997, 'James Cameron', 'don\'t know', 'USA', 'DRAMA', 'Leonardo Dicaprio')
movie2 = MovieData('Scarface', 1983, 'Brian de Palma', 'don\'t know', 'USA', 'Action', 'Al Pacino')
movie3 = MovieData('OOOOGABOOOGA', 1999, 'Gosho', 'asd', 'Bulgaria', 'COmdey', 'GOSHOU')
movie_manager = MoviesManager()
movie_manager.save_movie(movie)
movie_manager.save_movie(movie2)
movie_manager.save_movie(movie3)
movie_manager.remove_movie('Scarface', 1983)
movie_manager.remove_movie('Titanic', 1997)

print()

# Game Tests
game = GameData('God of war', 2014, 'Santa Monica', )
game2 = GameData('God of war II', 2015, 'Santa Monica', )
game3 = GameData('God of war III', 2016, 'Santa Monica', )
game_manager = GamesManager()
game_manager.save_game(game)
game_manager.save_game(game2)
game_manager.save_game(game3)
game_manager.remove_game('God of war', 2014)

print()

# Book Tests
book = BookData('Sicilian', 'Mario Puzzo', 1984, 'Drama')
book2 = BookData('ASDASD', 'Ivan Ivanov', 1983, 'Drama')
book3 = BookData('DSADSA', 'Gosho Goshev', 1982, 'Drama')
book_manager = BooksManager()
book_manager.save_book(book)
book_manager.save_book(book2)
book_manager.save_book(book3)
book_manager.remove_book('Sicilian ', 1984)  # TODO Fix deleting Function for Books
