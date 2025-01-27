from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        with open("data.json", "r") as file:
            movies = json.load(file)
            for movie, rate in movies.items():
                print(movie, rate)

    def add_movie(self, title, year, rating):
        try:
            # Load existing movies from the JSON file
            with open("data.json", "r") as file:
                movies = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty dictionary
            movies = {}

        # Add the new movie to the dictionary
        movies[title] = {"year": year, "rating": rating}

        print(f"Movie '{title}' (Year: {year}, Rating: {rating}) has been added.")

    def delete_movie(self, title):
        try:
            # Load existing movies from the JSON file
            with open("data.json", "r") as file:
                movies = json.load(file)
        except FileNotFoundError:
            print("Movies database not found. Nothing to delete.")
            return

        # Check if the movie exists in the database
        if title in movies:
            del movies[title]
            print(f"Movie '{title}' has been deleted.")
        else:
            print(f"Movie '{title}' not found in the database.")

    def update_movie(self, title, rating):
        try:
            # Load existing movies from the JSON file
            with open("data.json", "r") as file:
                movies = json.load(file)
        except FileNotFoundError:
            print("Movies database not found. Cannot update a movie.")
            return

        # Check if the movie exists in the database
        if title in movies:
            movies[title] = rating  # Update the movie's rating
            print(f"Movie '{title}' has been updated with a new rating: {rating}.")
        else:
            print(f"Movie '{title}' not found in the database.")