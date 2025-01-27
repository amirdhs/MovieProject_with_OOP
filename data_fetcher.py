import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def fetch_data(title):
    """Fetch movie data from OMDB API using environment variable for API key."""
    api_key = os.getenv('OMDB_API_KEY')
    if not api_key:
        raise ValueError("OMDB API key not found in environment variables")

    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        movie_data = response.json()
        return movie_data
    else:
        print(f"Error: {response.status_code}")
        return None