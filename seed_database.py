"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb melontasting")
os.system("createdb melontasting")

model.connect_to_db(server.app)
model.db.create_all()

# automatically populate the database with data:
# data/movies.json for movies

# with open('data/movies.json') as f:
#     movie_data = json.loads(f.read())

# movies_in_db = []
# for movie in movie_data:
#     title = movie['title']
#     overview = movie['overview']
#     poster_path = movie['poster_path']
#     release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")

#     db_movie = crud.create_movie(title, overview, release_date, poster_path)
#     movies_in_db.append(db_movie)

# model.db.session.add_all(movies_in_db)
# model.db.session.commit()



name = 'Lauren'
email = 'lauren@hb.com'

user = crud.create_user(name, email)
model.db.session.add(user)
model.db.session.commit()
