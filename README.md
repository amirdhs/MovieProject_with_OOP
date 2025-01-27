# Movie Database Application

A Python application for managing your movie collection. Features include fetching movie details from OMDB API, local storage management, and HTML website generation for your movie library.

## Features

- Add, update, and delete movies
- Fetch detailed movie information from OMDB API
- Search movies in local database
- Generate responsive HTML movie gallery
- View movie statistics
- Random movie selector
- Sort movies by rating
- Support for both JSON and CSV storage

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Internet connection (for OMDB API)

### Installation

1. Clone the repository
```bash
git clone [repository-url]
cd movie-database
```

2. Install dependencies
```bash
pip install requests python-dotenv
```

3. Configure API Key
- Sign up for an API key at [OMDB API](http://www.omdbapi.com/)
- Create a `.env` file in the project root
- Add your API key:
```
OMDB_API_KEY=your_api_key_here
```

4. Initialize storage
```bash
echo {} > data.json
```

### Running the Application

```bash
python main.py
```

## Usage

The application provides the following options:

0. Exit - Close the application
1. List movies - Display all movies in database
2. Add movie - Add a new movie with details from OMDB
3. Delete movie - Remove a movie from database
4. Update movie - Modify movie rating
5. Stats - View statistics about your movie collection
6. Random movie - Get a random movie suggestion
7. Search movie - Search your local movie database
8. Movies sorted by rating - View movies sorted by rating
9. Generate Website - Create HTML gallery of your movies


## Generated Website

The application generates a responsive HTML website featuring:
- Movie posters
- Title and release year
- IMDb rating
- Plot summary
- Cast and crew information

