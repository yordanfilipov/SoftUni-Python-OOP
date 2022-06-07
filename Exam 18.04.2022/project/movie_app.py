from project.movie_specification.fantasy import Fantasy
from project.movie_specification.movie import Movie
from project.movie_specification.action import Action
from project.movie_specification.thriller import Thriller
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []  # An empty list that will contain all the movies (objects)
        self.users_collection = []  # An empty list that will contain all the users (objects)

    def register_user(self, username: str, age: int):
        user = [u for u in self.users_collection if u.username == username]
        if user:
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)
        return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username]
        if not user:
            raise Exception("This user does not exist!")
        user = user[0]
        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = [u for u in self.users_collection if u.username == username][0]
        searched_movie = [m for m in self.movies_collection if m.title == movie.title]
        if not searched_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        movie = searched_movie[0]
        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for key in kwargs:
            if key == "title":
                movie.title = kwargs[key]
            if key == "year":
                movie.year = kwargs[key]
            if key == "age_restriction":
                movie.age_restriction = kwargs[key]
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        searched_movie = [m for m in self.movies_collection if m.title == movie.title]
        if not searched_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        movie = searched_movie[0]
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        movie = [m for m in self.movies_collection if m.title == movie.title][0]
        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        movie = [m for m in self.movies_collection if m.title == movie.title][0]
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        available_movies = [x for x in self.movies_collection]
        if not available_movies:
            return "No movies found."
        first_sort = sorted([x for x in available_movies], key=lambda x: x.year, reverse=True)
        movies = sorted([x for x in first_sort], key=lambda x: x.title, reverse=True)
        result = ''
        ll = []
        for movie in movies:
            ll.append(movie.details())
        result += '\n'.join(ll)
        return result

    def __str__(self):
        result = ''
        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            result += f'All users: {", ".join([x.username for x in self.users_collection])}\n'
        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            result += f'All movies: {", ".join([x.title for x in self.movies_collection])}'
        return result


# movie_app = MovieApp()
# print(movie_app.register_user('Martin', 24))
# user = movie_app.users_collection[0]
# movie = Action('Die Hard', 1988, user, 18)
# print(movie_app.upload_movie('Martin', movie))
# print(movie_app.movies_collection[0].title)
# print(movie_app.register_user('Alexandra', 25))
# user2 = movie_app.users_collection[1]
# movie2 = Action('Free Guy', 2021, user2, 16)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.like_movie('Alexandra', movie))
# print(movie_app.dislike_movie('Martin', movie2))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.delete_movie('Alexandra', movie2))
# movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.display_movies())
# print(movie_app)
