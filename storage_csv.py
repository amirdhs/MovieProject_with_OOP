from istorage import IStorage
import csv
import os
import data_fetcher


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Ensure the CSV file exists with headers"""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'year', 'rating', 'plot', 'poster', 'director', 'actors'])

    def get_movies_data(self):
        """Get all movies data from storage"""
        movies = {}
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row['title']] = {
                        'year': int(row['year']) if row['year'].isdigit() else 0,
                        'rating': float(row['rating']) if row['rating'] else 0,
                        'plot': row.get('plot', ''),
                        'poster': row.get('poster', ''),
                        'director': row.get('director', ''),
                        'actors': row.get('actors', '')
                    }
        except FileNotFoundError:
            self._ensure_file_exists()
        return movies

    def list_movies(self):
        """List all movies with their ratings"""
        movies = self.get_movies_data()
        if not movies:
            print("No movies found in the database.")
            return

        for title, data in movies.items():
            print(f"{title}: {data['rating']}")

    def add_movie(self, title, year=None, rating=None):
        """Add a movie to storage with optional API data fetch"""
        try:
            movies = self.get_movies_data()

            if title in movies:
                print(f"Movie '{title}' already exists in the database.")
                return

            # Fetch movie data from API
            movie_data = data_fetcher.fetch_data(title)

            if movie_data and movie_data.get('Response') != 'False':
                if year is None:
                    year = int(movie_data.get('Year', '0').split('–')[0])
                if rating is None:
                    rating = float(movie_data.get('imdbRating', '0'))

                new_movie = {
                    'title': title,
                    'year': str(year),
                    'rating': str(rating),
                    'plot': movie_data.get('Plot', ''),
                    'poster': movie_data.get('Poster', ''),
                    'director': movie_data.get('Director', ''),
                    'actors': movie_data.get('Actors', '')
                }
            else:
                new_movie = {
                    'title': title,
                    'year': str(year if year is not None else 0),
                    'rating': str(rating if rating is not None else 0),
                    'plot': '',
                    'poster': '',
                    'director': '',
                    'actors': ''
                }

            # Read existing movies
            existing_movies = []
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                existing_movies = list(reader)

            # Add new movie and write all movies back
            existing_movies.append(new_movie)
            with open(self.file_path, 'w', newline='') as file:
                fieldnames = ['title', 'year', 'rating', 'plot', 'poster', 'director', 'actors']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(existing_movies)

            print(f"Movie '{title}' has been added successfully.")

        except Exception as e:
            print(f"An error occurred while adding the movie: {e}")

    def delete_movie(self, title):
        """Delete a movie from storage"""
        try:
            movies = []
            found = False

            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for movie in reader:
                    if movie['title'] != title:
                        movies.append(movie)
                    else:
                        found = True

            if found:
                with open(self.file_path, 'w', newline='') as file:
                    fieldnames = ['title', 'year', 'rating', 'plot', 'poster', 'director', 'actors']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(movies)
                print(f"Movie '{title}' has been deleted.")
            else:
                print(f"Movie '{title}' not found in the database.")

        except Exception as e:
            print(f"An error occurred while deleting the movie: {e}")

    def update_movie(self, title, rating):
        """Update a movie's rating"""
        try:
            movies = []
            found = False

            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for movie in reader:
                    if movie['title'] == title:
                        movie['rating'] = str(rating)
                        found = True
                    movies.append(movie)

            if found:
                with open(self.file_path, 'w', newline='') as file:
                    fieldnames = ['title', 'year', 'rating', 'plot', 'poster', 'director', 'actors']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(movies)
                print(f"Movie '{title}' has been updated with new rating: {rating}")
            else:
                print(f"Movie '{title}' not found in the database.")

        except Exception as e:
            print(f"An error occurred while updating the movie: {e}")