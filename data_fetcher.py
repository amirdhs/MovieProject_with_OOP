import requests

# URL with your API key
def fetch_data(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey=d5776c1"
    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        movie_data = response.json()
        return movie_data
        # print(f"Title: {movie_data.get('Title')}}")
        # print(f"Year: {movie_data.get('Year')}")
        # print(f"Plot: {movie_data.get('Plot')}")
        # print(f"IMDb Rating: {movie_data.get('imdbRating')}")
    else:
        print(f"Error: {response.status_code}")

#