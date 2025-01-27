import json


def generate_html(movie_name=None):
    """Generates HTML for all movies in the JSON storage or a specific movie."""
    output = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Masterschool's Movie App</title>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Open+Sans:wght@300;600&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        font-size: 16px;
        background-color: rgb(235, 234, 234);   
        color: #333;
        margin: 0;
        padding: 0;
    }
    h1, h2 {
        font-family: 'Open Sans', sans-serif;
        font-weight: 600;
        margin-bottom: 10px;
        color: #222;
    }
    h1 {
        font-size: 2.5rem;
    }
    h2 {
        font-size: 1.8rem;
    }
    h3 {
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0;
        color: #444;
    }
    p {
        font-size: 1rem;
        line-height: 1.6;
        margin: 5px 0;
        color: #555;
    }
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 20px;
        margin: 50px auto;
        max-width: 80%;
        background-color: rgb(179, 181, 181);
        border-radius: 10px;
    }
    .movie {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 20px;
        gap: 5px;
    }
    .card {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        background-color: white;
        text-align: left;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 20px;
        max-width: 70%;
        gap: 20px;
    }
    img {
        border-radius: 10px;
        max-width: 150px;
    }
</style>
</head>
<body>
    <main>
        <h1>Masterschool's Movie App</h1>
        <h2>Movie Collection</h2>
    """

    try:
        # Read the JSON file
        with open("data.json", "r") as file:
            movies_data = json.load(file)

        if movie_name:
            # If a specific movie is requested, filter for just that movie
            if movie_name in movies_data:
                movies_to_display = {movie_name: movies_data[movie_name]}
            else:
                return output + f"<h2 class='not-found'>Sorry, we couldn't find '{movie_name}'.</h2></main></body></html>"
        else:
            # Display all movies
            movies_to_display = movies_data

        # Generate cards for each movie
        for title, movie_info in movies_to_display.items():
            output += f'<div class="card">\n'
            output += f'    <section id="movie_poster">\n'

            # Handle both old and new data formats
            if isinstance(movie_info, dict):
                poster = movie_info.get('poster', '#')
                year = movie_info.get('year', 'N/A')
                rating = movie_info.get('rating', 'N/A')
                plot = movie_info.get('plot', 'No plot available')
                director = movie_info.get('director', 'N/A')
                actors = movie_info.get('actors', 'N/A')
            else:
                # For old format where movie_info is just the rating
                poster = '#'
                year = 'N/A'
                rating = movie_info
                plot = 'No plot available'
                director = 'N/A'
                actors = 'N/A'

            # Use a placeholder image if no poster is available
            if poster == '#' or not poster:
                output += f'        <img src="/api/placeholder/150/225" alt="Movie Poster">\n'
            else:
                output += f'        <img src="{poster}" alt="Movie Poster" width="150">\n'

            output += f'    </section>\n'
            output += f'    <section id="movie_info">\n'
            output += f'        <h2>{title}</h2>\n'
            output += f'        <p>Year: {year}</p>\n'
            output += f'        <p>Rating: {rating}</p>\n'
            output += f'        <p>Director: {director}</p>\n'
            output += f'        <p>Actors: {actors}</p>\n'
            output += f'        <p>{plot}</p>\n'
            output += f'    </section>\n'
            output += f'</div>\n'

    except FileNotFoundError:
        output += "<h2 class='not-found'>No movies database found.</h2>"
    except Exception as e:
        output += f"<h2 class='not-found'>An error occurred: {str(e)}</h2>"

    # Add closing tags
    output += """
    </main>
</body>
</html>
    """
    return output