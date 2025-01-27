from data_fetcher import fetch_data

def generate_html(data, movie_name):
    """Serializes movies into an HTML list item."""
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
        align-items: flex-start;
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
        <h2>Here you can find more info about your Movie</h2>
    """

    if data:
        # Handle single dictionary
        if isinstance(data, dict):
            data = [data]  # Convert to a list for uniform handling

        # Handle list of movies
        for movie in data:
            output += f'<div class="card">\n'
            output += f'    <section id="movie_poster">\n'
            output += f'        <img src="{movie.get("Poster", "#")}" alt="Movie Poster" width="150">\n'
            output += f'    </section>\n'
            output += f'    <section id="movie_info">\n'
            output += f'        <h2>{movie.get("Title", "N/A")}</h2>\n'
            output += f'        <p>Year: {movie.get("Year", "N/A")}</p>\n'
            output += f'        <p>IMDb Rating: {movie.get("imdbRating", "N/A")}</p>\n'
            output += f'        <p>{movie.get("Plot", "N/A")}</p>\n'
            output += f'    </section>\n'
            output += f'</div>\n'
    else:
        output += f"<h2 class='not-found'>Sorry, we couldn't find '{movie_name}'.</h2>"

    # Add closing tags outside the loop
    output += """
    </main>
</body>
</html>
    """
    return output


