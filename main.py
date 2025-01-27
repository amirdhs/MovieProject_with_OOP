# Using JSON Storage
from movie_app import MovieApp
from storage_json import StorageJson


def main():
    # Initialize storage with the path to your JSON file
    storage = StorageJson('data.json')

    # Create the movie app instance
    movie_app = MovieApp(storage)

    try:
        # Run the application
        movie_app.run()
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()

# Using CSV Storage
"""
from movie_app import MovieApp
from storage_csv import StorageCsv

def main():
    # Initialize storage with the path to your CSV file
    storage = StorageCsv('movies.csv')

    # Create the movie app instance
    movie_app = MovieApp(storage)

    try:
        # Run the application
        movie_app.run()
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
"""