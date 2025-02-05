from movie_app import MovieApp
from storage.storage_json import StorageJson
from storage.storage_csv import StorageCsv


def get_storage_type():
    """Ask user for storage type preference"""
    while True:
        print("\nChoose storage type:")
        print("1. JSON Storage")
        print("2. CSV Storage")
        try:
            choice = int(input("Enter your choice (1-2): "))
            if choice in [1, 2]:
                return choice
            print("Please enter 1 or 2")
        except ValueError:
            print("Please enter a valid number")


def main():
    try:
        # Get storage preference
        storage_choice = get_storage_type()

        # Initialize appropriate storage
        if storage_choice == 1:
            storage = StorageJson('data/data.json')
        else:
            storage = StorageCsv('data/movies.csv')

        # Create and run the movie app
        movie_app = MovieApp(storage)
        movie_app.run()

    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()