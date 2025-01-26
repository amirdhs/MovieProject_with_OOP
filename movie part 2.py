from statistics import mean, median
import random
import movie_storage
from movie_storage import get_movies
import json

def list_movie():
    """
    Displays the total number of movies and lists each movie with its rating.
    """
    get_movies()

def stats():
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

def random_movie():
    """
    Selects and displays a random movie along with its rating from the movies dictionary.

    """
    with open("data.json", "r") as file:
        movies = json.load(file)
    random_key = random.choice(list(movies.keys()))
    random_value = movies[random_key]
    print(f"Random movie is: {random_key}, {random_value}")


def search_movie(name):
    """
    Searches for movies containing the specified name (case-insensitive) and returns the results.

    """
    with open("data.json", "r") as file:
        movies = json.load(file)
    results = []
    for key, val in movies.items():
        if name.lower() in key.lower():
            results.append(f"'{key}', {val}")
    return results


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
    8. Movies sorted by rating''')


def main():
    while True:
        try:
            menu()
            user_input = int(input("Enter choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue  # Re-display the menu for valid input
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue  # Re-display the menu for valid input

        if user_input == 0:
            print("Bye!")
            break

        if user_input == 1:
            list_movie()
        elif user_input == 2:
            name = input("Please enter your favorite movie: ")
            rate = float(input("Enter movie rating: "))
            year = int(input("Enter year of movie : "))
            movie_storage.add_movie(name, year, rate)
        elif user_input == 3:
            name = input("Enter the name of the movie you want to delete: ")
            movie_storage.delete_movie(name)
        elif user_input == 4:
            get_movies()
            movie_name = input("Enter name of movie that you want to update rating: ")
            new_rating = float(input("Enter new rate : "))
            movie_storage.update_movie(movie_name, new_rating)
        elif user_input == 5:
            stats()
        elif user_input == 6:
            random_movie()
        elif user_input == 7:
            name = input("What is the name of the movie you are looking for? ...")
            results = search_movie(name)
            if results:
                print("\n".join(results))
            else:
                print("No movies found.")
        elif user_input == 8:
            sorted_movie()
        else:
            print("Invalid choice. Please choose a number between 1 and 8.")

if __name__ == "__main__":
    main()

