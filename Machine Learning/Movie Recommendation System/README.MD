# Movie Recommendation System
This project demonstrates a basic movie recommendation system through the use of data science techniques and machine learning libraries and techniques.
The uploaded notebook demonstrates the following features:
- **Data Preprocessing:** Handles missing data, cleans datasets, and prepares data for analysis.
- **Recommendation techniques:** Employs content-based filtering in the model for recommendation based on user selection
-**Frontend (UI):** A simple UI is developed using `Streamlit` framework using features such as st.title, st.selectbox and st.button

## Dataset:
The dataset used in this project is sourced from TMDB movie database from Kaggle. It contains user ratings, movie information, metadata, and other essential features used in building the model.

## Frontend:
The frontend application that implements the developed model is created using streamlit, and the data and the required dependencies for the similarity of the results is pipelined through the use of `pickle` library.  
Run the notebook and 2 .pkl files will be created automatically.  
Then, run the app locally on your browser by passing the following command in the terminal:
```
streamlit run app.py
```

## Prerequisites:
Firstly, download the project files and then extract the datasets into the same directory that you are storing the .ipynb and .py files.

To run this notebook, you'll need:  
- `Python 3.9` and above  
- Libraries: `numpy`, `pandas`, `scikit-learn`, `nltk`, `pickle`.  
You can install the libraries using the following command in your terminal:
```
pip install <library name>
```  
To run the app, ensure the following libraries are installed:

- `Streamlit`
- `Pickle`
- `requests`
