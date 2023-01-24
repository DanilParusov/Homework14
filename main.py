from flask import Flask, jsonify
from utils import get_one_movie, get_all_movies

app = Flask(__name__)


@app.route('/movie/<title>')
def get_movie(title):
    query = f"""
                SELECT *
                FROM netflix
                WHERE title = '{title}'
    """

    result = get_one_movie(query)

    movie = {'title': result['title'],
             "country": result['country'],
             "release_year": result['release_year'],
             "genre": result["listed_in"],
             "description": result["description"]
             }

    return jsonify(movie)


@app.route('/movie/<year1>/to/<year2>')
def get_movies(year1: str, year2: str):
    query = f"""
                        SELECT *
                        FROM netflix
                        WHERE release_year BETWEEN {year1} AND {year2}
                        LIMIT 100
            """

    result = []
    for movie in get_all_movies(query):
        result.append({
            "title": movie["title"],
            "release_year": movie["release_year"]
        })
    return result


@app.route('/rating/<person>')
def get_movies_for_children(person):

    if person == "children":
        query = f"""
                            SELECT *
                            FROM netflix
                            WHERE rating IN ('G')
                            LIMIT 10
                """
    elif person == "adult":
        query = f"""
                                    SELECT *
                                    FROM netflix
                                    WHERE rating IN ('R', 'NC-17')
                                    LIMIT 10
                        """
    elif person == "family":
        query = f"""
                                    SELECT *
                                    FROM netflix
                                    WHERE rating IN ('G', 'PG', 'PG-13')
                                    LIMIT 10
                        """

    result = []

    for movie in get_all_movies(query):
        result.append(
            {
                "title": movie["title"],
                "rating": movie["rating"],
                "description": movie["description"]
            }
        )
    return result


@app.route('/genre/<genre>')
def get_movies_by_genre(genre):
    query = f"""
                            SELECT *
                            FROM netflix
                            WHERE listed_in LIKE '%{genre}%'
                            ORDER BY release_year
                            LIMIT 10
                """

    result = []

    for movie in get_all_movies(query):
        result.append(
            {
                "title": movie["title"],
                "description": movie["description"]
            }
        )
    return result

app.run()
