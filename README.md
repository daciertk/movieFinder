Movie Finder  
Movie Finder is a tool that filters data from a dataset of movies and TV shows. The tool allows the user to filter by Genre, type, and minimum IMDB rating. 

Data Source: [https://www.kaggle.com/datasets/octopusteam/imdb-top-rated-titles-movies-and-tv-series](https://www.kaggle.com/datasets/octopusteam/imdb-top-rated-titles-movies-and-tv-series)

Running:  
The program connects to a local mysql database, and uses the Flask and Jinja framework to deploy the site. The program requires Flask and mysql-connector-python to be installed 

pip install Flask  
pip install mysql-connecter-python

The program can be run using

Flask –app app run