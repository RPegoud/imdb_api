from package import MovieRequest
from package import Response
import requests
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    review = MovieRequest.get_score_from_name(movie_name='titanic')
    # assert isinstance(review, Response)
    # assert not isinstance(review,requests.Response)
    
    print(review)


