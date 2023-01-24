import sqlite3

def get_one_movie(query):
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        result = conn.execute(query).fetchone()
        return dict(result)

def get_all_movies(query):
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        result = []
        for movie in conn.execute(query).fetchall():
            result.append(dict(movie))

        return result




def get_movies_by_user_discr(type: str, release_year: str, genre: str):
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        query = f"""
                   SELECT * 
                   FROM netflix
                   WHERE `type` = '{type}'
                   AND `release_year` = '{release_year}'
                   AND `listed_in` = '{genre}'
        """

        result = []
        for movie in conn.execute(query).fetchall():
            result.append({
                "title": movie["title"],
                "description": movie["description"]
            })

        return result