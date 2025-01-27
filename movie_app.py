import json
import random
from statistics import mean, median
import data_fetcher
import storage_json
import website_generator


def menu():
    """
     Displays the menu options for the user.
     """
    print("********** My Movies Database **********")
    print('''Menu:
    0. Exit
    1. List movies
    2. Add movie
    3. Delete movie
    4. Update movie
    5. Stats
    6. Random movie
    7. Search movie
    8. Movies sorted by rating
    9.Generate Website''')

def random_movie():
    """
    Selects and displays a random movie along with its rating from the movies dictionary.

    """
    with open("data.json", "r") as file:
        movies = json.load(file)
    random_key = random.choice(list(movies.keys()))
    random_value = movies[random_key]
    print(f"Random movie is: {random_key}, {random_value}")

def sorted_movie():
    """
    Sorts and displays movies by their rating in descending order.
    """
    with open("data.json", "r") as file:
        data = json.load(file)

    movies = {}
    for title, value in data.items():
        if isinstance(value, (int, float)):
            movies[title] = value
        elif isinstance(value, dict) and "rating" in value:
            movies[title] = value["rating"]

    sorted_movies = sorted(movies.items(), key=lambda item: item[1], reverse=True)

    for movie, rating in sorted_movies:
        print(f"{movie}: {rating}")

class MovieApp:
    def __init__(self, storage):
        self._storage = storage


    def _command_list_movies(self):
        movies = self._storage.list_movies()
        return movies

    def _command_movie_stats(self):
        """
           Calculates and displays the average, median, highest, and lowest ratings along with
           the corresponding movies.
           """
        with open("data.json", "r") as file:
            data = json.load(file)

        # Extract movies and their ratings, ignoring invalid entries
        movies = {}
        for title, value in data.items():
            if isinstance(value, (int, float)):  # Directly check if value is a number
                movies[title] = value
            elif isinstance(value, dict) and "rating" in value:  # Handle nested objects with "rating" keys
                movies[title] = value["rating"]

        average_rating = mean(movies.values())
        median_rating = median(movies.values())
        max_rating = max(movies.values())
        min_rating = min(movies.values())

        best_movies = []
        for title, rating in movies.items():
            if rating == max_rating:
                best_movies.append(title)

        worst_movies = []
        for title, rating in movies.items():
            if rating == min_rating:
                worst_movies.append(title)

        print("Average Rating:", round(average_rating, 2))
        print("Median Rating:", round(median_rating, 2))
        print("Best Movie(s):")
        for movie in best_movies:
            print(f"  - {movie} (Rating: {max_rating})")
        print("Worst Movie(s):")
        for movie in worst_movies:
            print(f"  - {movie} (Rating: {min_rating})")

    def _generate_website(self):
        movie_title = input("Enter the title of Movie: ")
        data = data_fetcher.fetch_data(movie_title)

        # Write to movie_website.html
        if data is not None:
            html_content = website_generator.generate_html(data, movie_title)
            with open("movie_web.html", "w") as file:
                file.write(html_content)
            print("Website was successfully generated to the file movie_web.html.")

        website_generator.generate_html(data,movie_title)

    def run(self):
        while True:
            try:
                menu()
                user_input = int(input("Enter choice (1-8): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 8.")
                continue
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue

            if user_input == 0:
                print("Bye!")
                break

            if user_input == 1:
                MovieApp._command_list_movies(self)
            elif user_input == 2:
                name = input("Please enter your favorite movie: ")
                rate = float(input("Enter movie rating: "))
                year = int(input("Enter year of movie : "))
                storage_json.StorageJson.add_movie(self,title=name,year=rate,rating=year)
            elif user_input == 3:
                name = input("Enter the name of the movie you want to delete: ")
                storage_json.StorageJson.delete_movie(self,name)
            elif user_input == 4:
                storage_json.StorageJson.list_movies(self)
                movie_name = input("Enter name of movie that you want to update rating: ")
                new_rating = float(input("Enter new rate : "))
                storage_json.StorageJson.update_movie(self,movie_name,new_rating)
            elif user_input == 5:
                MovieApp._command_movie_stats(self)
            elif user_input == 6:
                random_movie()
            elif user_input == 7:
                name = input("What is the name of the movie you are looking for? ...")
                data = data_fetcher.fetch_data(name)
                if data:
                    # Handle single dictionary
                    if isinstance(data, dict):
                        data = [data]  # Convert to a list for uniform handling
                    for movie in data:
                        print(f"Title: {movie.get('Title', 'N/A')}")
                        print(f"Year: {movie.get('Year', 'N/A')}")
                        print(f"IMDb Rating: {movie.get('imdbRating')}")
            elif user_input == 8:
                sorted_movie()
            elif user_input == 9:
                MovieApp._generate_website(self)
            else:
                print("Invalid choice. Please choose a number between 1 and 8.")
