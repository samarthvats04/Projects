#import required libraries
import streamlit as st
import pickle
import pandas as pd
import requests

#function to display movie posters
def fetch_poster(movie_id):
	#fetch data of movie poster using the id tag through TMDB API
	response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
	data = response.json()
	return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
	
#function to fetch the recommended movies	
def recommend(movie):
	movie_index = movies[movies['title'] == movie].index[0]
	#distances to show the degree of similarity between the input movie and the output movies
	distances = similarity[movie_index]
	'''return the movies in a sorted manner, 
	where the most similar one is displayed first down to the least similar out of the top 5'''
	movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]

	#display the movies along with the posters
	recommended_movies = []
	recommended_posters = []
	for i in movies_list:
		movie_id = movies.iloc[i[0]].movie_id
		recommended_movies.append(movies.iloc[i[0]].title)
		recommended_posters.append(fetch_poster(movie_id))
	return recommended_movies, recommended_posters

#pipelining the dataset and the similarity matrix using a pkl file into the streamlit app
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommendation System')

#adding a selection box for title selection. Title can be typed in the placeholder as well.
selected_movie = st.selectbox(
	'Recommended movies:',
	movies['title'].values
)


if st.button('Find Similar Movies'):
	names, posters = recommend(selected_movie)

	#displaying the movies and the posters in a columnar layout
	col1, col2, col3, col4, col5 = st.columns(5)
	with col1:
		st.text(names[0])
		st.image(posters[0])
	with col2:
		st.text(names[1])
		st.image(posters[1])
	with col3:
		st.text(names[2])
		st.image(posters[2])
	with col4:
		st.text(names[3])
		st.image(posters[3])
	with col5:
		st.text(names[4])
		st.image(posters[4])

#run the app locally on your web browser by passing the commands: 'streamlit run app.py' in the terminal
