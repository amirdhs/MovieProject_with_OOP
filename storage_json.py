from istorage import IStorage
import json
import data_fetcher


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        with open("data.json", "r") as file:
            movies = json.load(file)
            for movie, rate in movies.items():
                print(movie, rate)

    def add_movie(self, title, year=None, rating=None):
        try:
            # Load existing movies from the JSON file
            with open("data.json", "r") as file:
                movies = json.load(file)
        except FileNotFoundError:
            movies = {}

        # Fetch movie data from API
        movie_data = data_fetcher.fetch_data(title)

        if movie_data and movie_data.get('Response') != 'False':
            # Extract year and rating from API if not provided
            if year is None:
                year = int(movie_data.get('Year', '0').split('–')[0])  # Handle series years like "2019–2023"
            if rating is None:
                rating = float(movie_data.get('imdbRating', '0'))

            # Create movie entry with additional data
            movies[title] = {
                "year": year,
                "rating": rating,
                "plot": movie_data.get('Plot'),
                "poster": movie_data.get('Poster')
            }

            # Save updated movies back to JSON file
            with open("data.json", "w") as file:
                json.dump(movies, file, indent=4)

            print(f"Movie '{title}' has been added with data from OMDB API.")
            print(f"Year: {year}")
            print(f"Rating: {rating}")
            print(f"Plot: {movie_data.get('Plot')}")
        else:
            # Fallback to basic addition if API data is not available
            movies[title] = {
                "year": year if year is not None else 0,
                "rating": rating if rating is not None else 0
            }

            # Save updated movies back to JSON file
            with open("data.json", "w") as file:
                json.dump(movies, file, indent=4)

            print(f"Movie '{title}' has been added with basic information only.")

    def delete_movie(self, title):
        try:
            with open("data.json", "r") as file:
                movies = json.load(file)
        except FileNotFoundError:
            print("Movies database not found. Nothing to delete.")
            return

        if title in movies:
            del movies[title]
            with open("data.json", "w") as file:
                json.dump(movies, file, indent=4)
            print(f"Movie '{title}' has been deleted.")
        else:
            print(f"Movie '{title}' not found in the database.")

    def update_movie(self, title, rating):
        try:
            with open("data.json", "r") as file:
                movies = json.load(file)
        except FileNotFoundError:
            print("Movies database not found. Cannot update a movie.")
            return

        if title in movies:
            if isinstance(movies[title], dict):
                movies[title]["rating"] = rating
            else:
                movies[title] = {"year": 0, "rating": rating}

            with open("data.json", "w") as file:
                json.dump(movies, file, indent=4)
            print(f"Movie '{title}' has been updated with a new rating: {rating}.")
        else:
            print(f"Movie '{title}' not found in the database.")