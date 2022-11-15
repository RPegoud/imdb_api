import os
import requests
from .response import Response
from dotenv import load_dotenv

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
        Returns the imDb score of a movie, provided its imDb ID.

            Parameters:
                    movie_name (str): the imDb ID of the movie
            Returns:
                    score (int): the imDb rating 
        '''

        search_response = cls.search_movie(name=movie_name)
        movie_id = search_response._content['results'][0].get('id', 'id not found')
        movie_title = search_response._content['results'][0].get('title', 'title not found')

        rating_response = cls.get_score(id=movie_id)
        score = rating_response._content['imDb']
        print(f"Score for the  movie '{movie_title}': {score}")
        return score