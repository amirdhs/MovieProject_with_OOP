import json
import random
from statistics import mean, median
import website_generator


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """List all movies"""
        self._storage.list_movies()

    def _command_add_movie(self):
        """Add a movie"""
        name = input("Please enter your favorite movie: ")
        self._storage.add_movie(title=name, year=None, rating=None)

    def _command_delete_movie(self):
        """Delete a movie"""
        name = input("Enter the name of the movie you want to delete: ")
        self._storage.delete_movie(name)

    def _command_update_movie(self):
        """Update a movie's rating"""
        self._storage.list_movies()
        movie_name = input("Enter name of movie that you want to update rating: ")
        try:
            new_rating = float(input("Enter new rate : "))
            self._storage.update_movie(movie_name, new_rating)
        except ValueError:
            print("Invalid rating. Please enter a number.")

    def _command_movie_stats(self):
        """Calculate movie statistics"""
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

            movies = {}
            for title, value in data.items():
                if isinstance(value, (int, float)):
                    movies[title] = value
                elif isinstance(value, dict) and "rating" in value:
                    movies[title] = value["rating"]

            if not movies:
                print("No movies with ratings found.")
                return

            ratings = list(movies.values())
            average_rating = mean(ratings)
            median_rating = median(ratings)
            max_rating = max(ratings)
            min_rating = min(ratings)

            print(f"Average Rating: {round(average_rating, 2)}")
            print(f"Median Rating: {round(median_rating, 2)}")
            print("Best Movie(s):")
            for title, rating in movies.items():
                if rating == max_rating:
                    print(f"  - {title} (Rating: {rating})")
            print("Worst Movie(s):")
            for title, rating in movies.items():
                if rating == min_rating:
                    print(f"  - {title} (Rating: {rating})")

        except FileNotFoundError:
            print("Movie database not found.")
        except Exception as e:
            print(f"An error occurred while calculating statistics: {e}")

    def _command_random_movie(self):
        """Select a random movie"""
        try:
            with open("data.json", "r") as file:
                movies = json.load(file)
            if not movies:
                print("No movies in database.")
                return
            random_key = random.choice(list(movies.keys()))
            random_value = movies[random_key]
            if isinstance(random_value, dict):
                print(f"Random movie is: {random_key}, {random_value['rating']}")
            else:
                print(f"Random movie is: {random_key}, {random_value}")
        except FileNotFoundError:
            print("Movie database not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _command_search_movie(self):
        """Search for a movie"""
        name = input("What is the name of the movie you are looking for? ...")
        try:
            with open("data.json", "r") as file:
                movies = json.load(file)

            matches = {title: data for title, data in movies.items()
                       if name.lower() in title.lower()}

            if matches:
                print("\nFound movies:")
                for title, movie_data in matches.items():
                    if isinstance(movie_data, dict):
                        print(f"\nTitle: {title}")
                        print(f"Year: {movie_data.get('year', 'N/A')}")
                        print(f"Rating: {movie_data.get('rating', 'N/A')}")
                        if 'plot' in movie_data:
                            print(f"Plot: {movie_data['plot']}")
                    else:
                        print(f"\nTitle: {title}")
                        print(f"Rating: {movie_data}")
            else:
                print(f"No movies found matching '{name}'")
        except FileNotFoundError:
            print("Movie database not found.")
        except Exception as e:
            print(f"An error occurred while searching: {e}")

    def _command_sorted_movies(self):
        """Display movies sorted by rating"""
        try:
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
        except FileNotFoundError:
            print("Movie database not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _generate_website(self):
        """Generate website"""
        html_content = website_generator.generate_html()
        try:
            with open("index.html", "w", encoding='utf-8') as file:
                file.write(html_content)
            print("Website was successfully generated to the file index.html.")
        except Exception as e:
            print(f"Error generating website: {str(e)}")

    def run(self):
        """Main application loop"""
        while True:
            try:
                self._print_menu()
                choice = input("Enter choice (0-9): ")

                if not choice.isdigit():
                    print("Please enter a number between 0 and 9.")
                    continue

                choice = int(choice)

                if choice == 0:
                    print("Bye!")
                    break
                elif choice == 1:
                    self._command_list_movies()
                elif choice == 2:
                    self._command_add_movie()
                elif choice == 3:
                    self._command_delete_movie()
                elif choice == 4:
                    self._command_update_movie()
                elif choice == 5:
                    self._command_movie_stats()
                elif choice == 6:
                    self._command_random_movie()
                elif choice == 7:
                    self._command_search_movie()
                elif choice == 8:
                    self._command_sorted_movies()
                elif choice == 9:
                    self._generate_website()
                else:
                    print("Invalid choice. Please choose a number between 0 and 9.")

            except Exception as e:
                print(f"An error occurred: {e}")

    def _print_menu(self):
        """Display the menu"""
        print("\n********** My Movies Database **********")
        print("""Menu:
    0. Exit
    1. List movies
    2. Add movie
    3. Delete movie
    4. Update movie
    5. Stats
    6. Random movie
    7. Search movie
    8. Movies sorted by rating
    9. Generate Website""")