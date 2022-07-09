from tkinter import *
from tkinter import messagebox
from Collection_manager_OOP import MoviesManager, MovieData, BooksManager, BookData, GamesManager, GameData

root = Tk()
root.title('George\'s Collection Manager')
root.geometry('500x350')

# TODO delete games

# MOVIES FUNCTIONS
def save_to_movies():
    manager = MoviesManager()
    m = MovieData(
        name_entry.get(),
        year_entry.get(),
        director_entry.get(),
        time_entry.get(),
        country_entry.get(),
        type_entry.get(),
        main_actor_entry.get(),
    )
    manager.save_movie(m)
    messagebox.showinfo('Adding...', f'{name_entry.get()} is added to your movie collection!')
    name_entry.delete(0, 'end')
    year_entry.delete(0, 'end')
    director_entry.delete(0, 'end')
    time_entry.delete(0, 'end')
    country_entry.delete(0, 'end')
    type_entry.delete(0, 'end')
    main_actor_entry.delete(0, 'end')


def show_movies_collection():
    with open('movies_collector.txt', 'r+') as file:
        lines = file.readlines()
        messagebox.showinfo('All Movies', '\n'.join(lines))


def show_movie_window():
    top = Toplevel()
    top.geometry('600x500')
    top.title('Movies')
    mainframe = Frame(top, width=100, highlightbackground='red', highlightthickness=3)
    mainframe.grid(row=0, column=0, padx=150, pady=20, ipadx=20, ipady=20)

    name_label = Label(mainframe, text='Enter movie name')
    name_label.grid(row=1, column=1, padx=10, pady=10)
    global name_entry
    name_entry = Entry(mainframe)
    name_entry.grid(row=1, column=2)

    year_label = Label(mainframe, text='Enter movie year')
    year_label.grid(row=2, column=1, padx=10, pady=10)
    global year_entry
    year_entry = Entry(mainframe)
    year_entry.grid(row=2, column=2)

    director_label = Label(mainframe, text='Enter movie director')
    director_label.grid(row=3, column=1, padx=10, pady=10)
    global director_entry
    director_entry = Entry(mainframe)
    director_entry.grid(row=3, column=2)

    time_label = Label(mainframe, text='Enter movie time')
    time_label.grid(row=4, column=1, padx=10, pady=10)
    global time_entry
    time_entry = Entry(mainframe)
    time_entry.grid(row=4, column=2)

    country_label = Label(mainframe, text='Enter movie country')
    country_label.grid(row=5, column=1, padx=10, pady=10)
    global country_entry
    country_entry = Entry(mainframe)
    country_entry.grid(row=5, column=2)

    type_label = Label(mainframe, text='Enter movie type')
    type_label.grid(row=6, column=1, padx=10, pady=10)
    global type_entry
    type_entry = Entry(mainframe)
    type_entry.grid(row=6, column=2)

    main_actor_label = Label(mainframe, text='Enter movie main actor')
    main_actor_label.grid(row=7, column=1, padx=10, pady=10)
    global main_actor_entry
    main_actor_entry = Entry(mainframe)
    main_actor_entry.grid(row=7, column=2)

    button_save = Button(mainframe, text='Save to movies manager', command=save_to_movies)
    button_save.grid(row=8, column=1, columnspan=2, padx=10, pady=10)

    button_show_collection = Button(mainframe, text='See all movies', command=show_movies_collection)
    button_show_collection.grid(row=9, column=1, columnspan=2, padx=10, pady=10)

    button_close = Button(mainframe, text='Close Window', command=top.destroy)
    button_close.grid(row=10, column=1, columnspan=2,padx=10, pady=10)


# BOOKS FUNCTIONS
def save_to_books():
    manager = BooksManager()
    b = BookData(
        book_entry.get(),
        author_entry.get(),
        year_entry.get(),
        genre_entry.get(),
    )

    manager.save_book(b)
    messagebox.showinfo('Adding...', f'{book_entry.get()} is added to your book collection!')
    book_entry.delete(0, 'end'),
    author_entry.delete(0, 'end'),
    year_entry.delete(0, 'end'),
    genre_entry.delete(0, 'end'),


def show_books_collection():
    with open('books_collector.txt', 'r+') as file:
        lines = file.readlines()
        messagebox.showinfo('All Books', '\n'.join(lines))


def show_books_window():
    top = Toplevel()
    top.geometry('600x500')
    top.title('Books')
    mainframe = Frame(top, width=100, highlightbackground='red', highlightthickness=3)
    mainframe.grid(row=0, column=0, padx=150, pady=20, ipadx=20, ipady=20)

    book_name = Label(mainframe, text='Enter book name')
    book_name.grid(row=1, column=1, padx=10, pady=10)
    global book_entry
    book_entry = Entry(mainframe)
    book_entry.grid(row=1, column=2)

    author_label = Label(mainframe, text='Enter book author')
    author_label.grid(row=2, column=1, padx=10, pady=10)
    global author_entry
    author_entry = Entry(mainframe)
    author_entry.grid(row=2, column=2)

    year_label = Label(mainframe, text='Enter book year')
    year_label.grid(row=3, column=1, padx=10, pady=10)
    global year_entry
    year_entry = Entry(mainframe)
    year_entry.grid(row=3, column=2)

    genre_label = Label(mainframe, text='Enter book genre')
    genre_label.grid(row=4, column=1, padx=10, pady=10)
    global genre_entry
    genre_entry = Entry(mainframe)
    genre_entry.grid(row=4, column=2)

    button_save = Button(mainframe, text='Save to books manager', command=save_to_books)
    button_save.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

    button_show_collection = Button(mainframe, text='See all books', command=show_books_collection)
    button_show_collection.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

    button_close = Button(mainframe, text='Close Window', command=top.destroy)
    button_close.grid(row=7, column=1, columnspan=2, padx=10, pady=10)


# GAMES FUNCTIONS
def save_to_games():
    manager = GamesManager()
    g = GameData(
        game_entry.get(),
        year_entry.get(),
        creator_entry.get(),
    )
    manager.save_game(g)
    messagebox.showinfo('Adding...', f'{game_entry.get()} is added to your book collection!')
    game_entry.delete(0, 'end'),
    year_entry.delete(0, 'end'),
    creator_entry.delete(0, 'end'),


def show_games_collection():
    with open('games_collector.txt', 'r+') as file:
        lines = file.readlines()
        messagebox.showinfo('All Games', '\n'.join(lines))


def show_game_window():
    top = Toplevel()
    top.geometry('600x500')
    top.title('Books')
    mainframe = Frame(top, width=100, highlightbackground='red', highlightthickness=3)
    mainframe.grid(row=0, column=0, padx=150, pady=20, ipadx=20, ipady=20)

    game_name = Label(mainframe, text='Enter game name')
    game_name.grid(row=1, column=1, padx=10, pady=10)
    global game_entry
    game_entry = Entry(mainframe)
    game_entry.grid(row=1, column=2)

    year_label = Label(mainframe, text='Enter game year')
    year_label.grid(row=2, column=1, padx=10, pady=10)
    global year_entry
    year_entry = Entry(mainframe)
    year_entry.grid(row=2, column=2)

    creator_label = Label(mainframe, text='Enter game creator')
    creator_label.grid(row=3, column=1, padx=10, pady=10)
    global creator_entry
    creator_entry = Entry(mainframe)
    creator_entry.grid(row=3, column=2)

    button_save = Button(mainframe, text='Save to games manager', command=save_to_games)
    button_save.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    button_show_collection = Button(mainframe, text='See all games', command=show_games_collection)
    button_show_collection.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

    button_close = Button(mainframe, text='Close Window', command=top.destroy)
    button_close.grid(row=6, column=1, columnspan=2, padx=10, pady=10)


button_books_window = Button(root, text='Go to Movies', command=show_movie_window)
button_books_window.pack(pady=20, ipady=15, ipadx=15)

button_movie_window = Button(root, text='Go to Books', command=show_books_window)
button_movie_window.pack(pady=30, ipady=15, ipadx=15)

button_game_window = Button(root, text='Go to Games', command=show_game_window)
button_game_window.pack(pady=40, ipady=15, ipadx=15)

root.mainloop()
