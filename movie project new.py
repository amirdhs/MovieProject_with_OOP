import statistics
import random


def list_movie(movies):
    print(f"{len(movies)} movies in total")
    for key, val in movies.items():
        print(key, val)


def add_movie(movies, name, rate):
    movies[name] = rate
    print(f"{name} added with a rating of {rate}")
    list_movie(movies)


def delete_movie(movies, name):
    if name in movies:
        del movies[name]
        print(f"{name} deleted.")
    else:
        print(f"{name} not found in the database.")
    list_movie(movies)


def update_movie(movies, old_name, new_name):
    if old_name in movies:
        movies[new_name] = movies.pop(old_name)
        print(f"{old_name} updated to {new_name}.")
    else:
        print(f"{old_name} not found in the dictionary.")
    list_movie(movies)


def stats(movies):
    average_rating = sum(movies.values()) / len(movies)
    median_rating = statistics.median(movies.values())
    max_key = max(movies, key=movies.get)
    max_value = movies[max_key]
    min_key = min(movies, key=movies.get)
    min_value = movies[min_key]
    print(f"""Average rating: {average_rating:.2f}
Median rating: {median_rating:.2f}
Best movie: {max_key}, {max_value}  
Worst movie: {min_key}, {min_value}
    """)


def random_movie(movies):
    random_key = random.choice(list(movies.keys()))
    random_value = movies[random_key]
    print(f"Random movie is: {random_key}, {random_value}")


def search_movie(movies, name):
    results = []
    for key, val in movies.items():
        if name.lower() in key.lower():
            results.append(f"'{key}', {val}")
    return results


def sorted_movie(movies):
    sorted_movies = sorted(movies.items(), key=lambda item: item[1], reverse=True)
    for movie, rating in sorted_movies:
        print(f"{movie}: {rating}")


def main():
    movies = {  # Define the movies dictionary here
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    print("********** My Movies Database **********")
    print(f'''Menu:
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating''')

    while True:
        user_input = int(input("Enter choice (1-8): "))
        if user_input == 1:
            list_movie(movies)
        elif user_input == 2:
            name = input("Please enter your favorite movie: ")
            rate = float(input("Enter movie rating: "))  # Changed to float
            add_movie(movies, name, rate)
        elif user_input == 3:
            name = input("Enter the name of the movie you want to delete: ")
            delete_movie(movies, name)
        elif user_input == 4:
            old_name = input("Enter name of movie that you want to update: ")
            new_name = input("Enter new name of movie: ")
            update_movie(movies, old_name, new_name)
        elif user_input == 5:
            stats(movies)
        elif user_input == 6:
            random_movie(movies)
        elif user_input == 7:
            name = input("What is the name of the movie you are looking for? ...")
            results = search_movie(movies, name)
            if results:
                print("\n".join(results))
            else:
                print("No movies found.")
        elif user_input == 8:
            sorted_movie(movies)
        else:
            print("Invalid choice. Please choose a number between 1 and 8.")


if __name__ == "__main__":
    main()
