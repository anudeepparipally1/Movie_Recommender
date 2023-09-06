import streamlit as st
import pickle
import pandas as pd
import numpy as np


def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distance = similarity[movie_index]
    Movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    # recommended_movies = []
    r = []
    m = []
    rt = []
    for i in Movie_list:
        r.append(float(movies[movies['original_title'] == "{}".format(movies.iloc[i[0]].original_title)]["rating"]))
        # recommended_movies.append(movies.iloc[i[0]].original_title)
        m.append(movies.iloc[i[0]].original_title)
    for j in range(10):
        rt.append(r[j])

    s = np.array(rt)
    c = 1
    tm = []
    sort_index = np.argsort(s)
    for i in sort_index[::-1]:
        if c <= 5:
            tm.append(m[i])
            c = c + 1

    # return recommended_movies
    return tm


def recommend2(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].original_title)

    return recommended_movies


movie_list = pickle.load(open("movies2.pkl", 'rb'))
movies = pd.DataFrame(movie_list)
# print(movies)

similarity = pickle.load(open("similarity.pkl", 'rb'))
st.title("MOVIE RECOMMENDATION SYSTEM")

movie_name = st.selectbox('Enter the movie name', movies['original_title'].values)

if st.button('Recommend'):
    topMovies = recommend(movie_name)
    top=recommend2(movie_name)
    for j in top:
        st.write(j)
    st.title("--------TOP RATED MOVIES---------")
    for i in topMovies:
        st.write(i)





