from storage.istorage import IStorage
import json
import data_fetcher

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Ensure the JSON file exists, create if it doesn't"""
        try:
            with open(self.file_path, "r") as file:
                json.load(file)
        except FileNotFoundError:
            with open(self.file_path, "w") as file:
                json.dump({}, file)
        except json.JSONDecodeError:
            with open(self.file_path, "w") as file:
                json.dump({}, file)

    def get_movies_data(self):
        """Get all movies data from storage"""
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def list_movies(self):
        """List all movies with their ratings"""
        movies = self.get_movies_data()
        if not movies:
            print("No movies found in the database.")
            return

        for movie, data in movies.items():
            rating = data['rating'] if isinstance(data, dict) else data
            print(f"{movie}: {rating}")

    def add_movie(self, title, year=None, rating=None):
        """Add a movie to storage with optional API data fetch"""
        try:
            movies = self.get_movies_data()

            # Check if movie already exists
            if title in movies:
                print(f"Movie '{title}' already exists in the database.")
                return

            # Fetch movie data from API
            movie_data = data_fetcher.fetch_data(title)

            if movie_data and movie_data.get('Response') != 'False':
                # Extract year and rating from API if not provided
                if year is None:
                    year = int(movie_data.get('Year', '0').split('–')[0])
                if rating is None:
                    rating = float(movie_data.get('imdbRating', '0'))

                # Create movie entry with additional data
                movies[title] = {
                    "year": year,
                    "rating": rating,
                    "plot": movie_data.get('Plot'),
                    "poster": movie_data.get('Poster'),
                    "director": movie_data.get('Director'),
                    "actors": movie_data.get('Actors')
                }
            else:
                # Fallback to basic addition
                movies[title] = {
                    "year": year if year is not None else 0,
                    "rating": rating if rating is not None else 0
                }

            # Save updated movies
            with open(self.file_path, "w") as file:
                json.dump(movies, file, indent=4)

            print(f"Movie '{title}' has been added successfully.")

        except Exception as e:
            print(f"An error occurred while adding the movie: {e}")

    def delete_movie(self, title):
        """Delete a movie from storage"""
        try:
            movies = self.get_movies_data()
            if title in movies:
                del movies[title]
                with open(self.file_path, "w") as file:
                    json.dump(movies, file, indent=4)
                print(f"Movie '{title}' has been deleted.")
            else:
                print(f"Movie '{title}' not found in the database.")
        except Exception as e:
            print(f"An error occurred while deleting the movie: {e}")

    def update_movie(self, title, rating):
        """Update a movie's rating"""
        try:
            movies = self.get_movies_data()
            if title in movies:
                if isinstance(movies[title], dict):
                    movies[title]["rating"] = rating
                else:
                    movies[title] = {"year": 0, "rating": rating}

                with open(self.file_path, "w") as file:
                    json.dump(movies, file, indent=4)
                print(f"Movie '{title}' has been updated with new rating: {rating}")
            else:
                print(f"Movie '{title}' not found in the database.")
        except Exception as e:
            print(f"An error occurred while updating the movie: {e}")