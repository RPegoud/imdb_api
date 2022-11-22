import os
import requests
from .response import Response
from dotenv import load_dotenv
import time

load_dotenv()

class MovieRequest:
    _api_key = os.environ.get("api-key")
    _base_url = os.environ.get("base-url")

    @classmethod # we don't need to instantiate the class to access this method
    def search_movie(cls, name:str = 'inception 2010'): # cls doesn't refer to the instance but the class
        '''
        Searches for a movie in the imDb database.

            Parameters:
                    name (str): the name of the movie to search for
            Returns:
                    search_response (Response): the SearchMovie response list containing the movies 
                    corresponding to the search
        '''

        search_url = f"SearchMovie/{cls._api_key}/{name}"
        full_url = cls._base_url + search_url
        response = requests.request("GET", full_url)
        
        return Response(status_code=response.status_code, content=response.json())


    @classmethod
    def get_score(cls, id:str = 'tt1375666'):
        '''
        Gets the imDb score for a movie

            Parameters:
                    id (str): the imDb ID of the movie
            Returns:
                    rating_response (Response): the Rating response containing the several ratings 
                    of the movie
        '''

        score_url = f'Ratings/{cls._api_key}/{id}'
        full_url = cls._base_url + score_url
        response = requests.request("GET", full_url)
        
        return Response(status_code=response.status_code, content=response.json())


    @classmethod
    def get_score_from_name(cls, movie_name = 'inception 2010'):
        '''
        Aggregates search_movie and get_score 

            Parameters:
                    movie_name (str): the imDb ID of the movie
            Returns:
                    score (dict): a dictionary containing the film features (title, id, score) 
        '''

        movie_features = {}

        search_response = cls.search_movie(name=movie_name)

        print(search_response._content)
        try: # avoids errors when the API is unusable (busy, limit of calls reached)
            # movie_id = search_response._content['results'][0].get('id', 'id not found')
            # movie_title = search_response._content['results'][0].get('title', 'title not found')
            print("Searching movie ...")
            movie_features['id'] = search_response._content['results'][0].get('id', 'id not found')
            movie_features['title'] = search_response._content['results'][0].get('title', 'title not found')
            movie_features['image'] = search_response._content['results'][0].get('image', 'image not found')
            movie_features['description'] = search_response._content['results'][0].get('description', 'description not found')

            print("Searching score ...")
            rating_response = cls.get_score(id=movie_features['id'])
            time.sleep(10)
            movie_features['imdb_score'] = rating_response._content['imDb']
            movie_features['metacritic_score'] = rating_response._content['metacritic']
            movie_features['rottenTomatoes_score'] = rating_response._content['rottenTomatoes']

            # print(f"Score for the  movie '{movie_features['title']}': {movie_features['score']}")

            return movie_features
            
        except (TypeError, KeyError) as e: 
            print(e)
            movie_features['error'] = search_response._content.get('errorMessage')
            return movie_features