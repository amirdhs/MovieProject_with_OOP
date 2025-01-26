import json

def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data. 

    """
    with open("data.json", "r") as file:
        movies = json.load(file)
        for movie,rate in movies.items():
            print(movie,rate)


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """

    with open("data.json", "w") as file:
        json.dump(movies, file, indent=4)
    print("Movies saved to the JSON file.")

def add_movie(name, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, adds the movie,
    and saves it. The function doesn't need to validate the input.

    """
    try:
        # Load existing movies from the JSON file
        with open("data.json", "r") as file:
            movies = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty dictionary
        movies = {}

    # Add the new movie to the dictionary
    movies[name] = {"year": year, "rating": rating}

    # Save the updated movies dictionary back to the JSON file
    save_movies(movies)
    print(f"Movie '{name}' (Year: {year}, Rating: {rating}) has been added.")


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """

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
        save_movies(movies)
        print(f"Movie '{title}' has been deleted.")
    else:
        print(f"Movie '{title}' not found in the database.")


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
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
        save_movies(movies)
        print(f"Movie '{title}' has been updated with a new rating: {rating}.")
    else:
        print(f"Movie '{title}' not found in the database.")


