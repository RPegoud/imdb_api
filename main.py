from package import MovieRequest
from package import Response
import requests
import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from utils import movie_list
import plotly.express as px

load_dotenv()

# assert isinstance(review, Response)
# assert not isinstance(review,requests.Response)

with st.sidebar:
    st.title('imDb Charts 🔥')
    search = st.text_input(label='Search for a movie !', value='Titanic')

    st.write('Lacking inspiration ?\nHere\'s a list of movies with Dwayne Johnson 🪨:')
    # for movie in movie_list:
    #     st.button(label=movie, on_click=MovieRequest.get_score_from_name(movie_name=movie))

    if search:
        query = MovieRequest.get_score_from_name(movie_name=search)
        print(query)

col1, col2 = st.columns(2)
with col1:
    if "imdb_score" in query.keys():
    # try:
        st.title(f'Best result : {query.get("title")}')
        st.write(f'imDb ID : {query.get("id")}')
        st.write(f'imDb score : {query.get("imdb_score")}/10')
        st.write(f'Metacritic score : {query.get("metacritic_score")}/100')
        st.write(f'Rotten Tomato score : {query.get("rottenTomatoes_score")}/100')

    # except AttributeError:
    else:
        st.error(f'Error encountered: {query.get("error")}')

with col2:
    try:
        image_url = query.get("image")
        image = Image.open(requests.get(image_url, stream=True).raw)
        st.image(image, width=300)
    except:
        pass

try:
    st.plotly_chart(
        px.bar(x = ['imDb','Metacritic','Rotten Tomatoes'],
        y = [float(query.get("imdb_score"))*10, 
            float(query.get("metacritic_score")), 
            float(query.get("rottenTomatoes_score"))])
    )
except TypeError as e:
    print(e)