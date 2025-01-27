from istorage import IStorage
import csv
import os


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'year', 'rating'])

    def list_movies(self):
        self._ensure_file_exists()
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(f"{row['title']} (Year: {row['year']}, Rating: {row['rating']})")
        except Exception as e:
            print(f"Error reading movies: {e}")

    def add_movie(self, title, year, rating):
        self._ensure_file_exists()
        movies = []

        # Read existing movies
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            movies = list(reader)

        # Check if movie already exists
        if any(movie['title'] == title for movie in movies):
            print(f"Movie '{title}' already exists.")
            return

        # Add new movie
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ['title', 'year', 'rating']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            movies.append({'title': title, 'year': str(year), 'rating': str(rating)})
            writer.writerows(movies)

        print(f"Movie '{title}' (Year: {year}, Rating: {rating}) has been added.")

    def delete_movie(self, title):
        self._ensure_file_exists()
        movies = []
        found = False

        # Read existing movies
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            movies = [movie for movie in reader if movie['title'] != title]
            found = len(movies) < reader.line_num - 1

        # Write updated movies
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ['title', 'year', 'rating']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(movies)

        if found:
            print(f"Movie '{title}' has been deleted.")
        else:
            print(f"Movie '{title}' not found in the database.")

    def update_movie(self, title, rating):
        self._ensure_file_exists()
        movies = []
        found = False

        # Read existing movies
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            movies = list(reader)

            for movie in movies:
                if movie['title'] == title:
                    movie['rating'] = str(rating)
                    found = True
                    break

        # Write updated movies
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ['title', 'year', 'rating']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(movies)

        if found:
            print(f"Movie '{title}' has been updated with a new rating: {rating}.")
        else:
            print(f"Movie '{title}' not found in the database.")