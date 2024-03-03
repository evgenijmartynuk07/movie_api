# Movie Django App

This Django app provides functionality for managing movies, directors, actors, and genres. It includes both regular URLs and API URLs for accessing and manipulating data.

## Regular URLs

The regular URLs are used for rendering views for users interacting with the application through a web browser.

### Installation and Usage

1. Clone the repository:
```shell
git clone https://github.com/evgenijmartynuk07/movie_api.git
```
2. Create venv and install dependencies:
```shell
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```
3. Create .env and Run migrations:
```shell
create .env based on .env.sample
python manage.py migrate
```
4. Start the Django server:
```shell
python manage.py runserver
```

5. Access the application in your browser at http://localhost:8000.

### URLs

- `/`: Home page.
- `/movie/list/`: View a list of movies.
- `/movie/<int:pk>/`: View details of a specific movie.
- `/movie/create/`: Create a new movie.
- `/movie/<int:pk>/update/`: Update details of a movie.
- `/movie/<int:pk>/delete/`: Delete a movie.
- `/movie/director/list/`: View a list of directors.
- `/movie/director/create/`: Create a new director.
- `/movie/director/<int:pk>/delete/`: Delete a director.
- `/movie/actor/list/`: View a list of actors.
- `/movie/actor/create/`: Create a new actor.
- `/movie/actor/<int:pk>/delete/`: Delete an actor.
- `/movie/genre/list/`: View a list of genres.
- `/movie/genre/create/`: Create a new genre.
- `/movie/genre/<int:pk>/delete/`: Delete a genre.

## API URLs

The API URLs are used for programmatically accessing and manipulating data.

### Installation and Usage

1. Ensure the Django app is running as described in the Regular URLs section.

### URLs

- `/api/movie/`: Endpoint for managing movies.
- `/api/movie/<int:pk>/`: Endpoint for a specific movie (update, delete).
- `/api/movie/actors/`: Endpoint for managing actors.
- `/api/movie/actors/delete/<int:pk>/`: Endpoint for deleting an actor.
- `/api/movie/directors/`: Endpoint for managing directors.
- `/api/movie/directors/delete/<int:pk>/`: Endpoint for deleting a director.
- `/api/movie/genres/`: Endpoint for managing genres.
- `/api/movie/genres/delete/<int:pk>/`: Endpoint for deleting a genre.

