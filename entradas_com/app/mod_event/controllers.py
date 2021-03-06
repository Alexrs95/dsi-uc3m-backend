# Import flask dependencies
from flask import Blueprint, render_template, redirect, request
from app.models import *
from app import db
from flask import Session

mod_event = Blueprint('event', __name__,)

# Set the route and accepted methods
@mod_event.route('/event/<id>')
def event(id):
	#return id
    event = query_by_id(id)

    result = event_genre(event.eventId)
    genres_list = ""
    if len(result) > 0:
        genres_list = ", ".join(result) if len(result) > 1 else result[0]

    result = event_director(id)
    director = ""
    if len(result) > 0:
        director = ", ".join(result) if len(result) > 1 else result[0]

    result = event_cast(id)
    cast = ""
    if len(result) > 0:
        cast = ", ".join(result) if len(result) > 1 else result[0]

    return render_template("event/event.html", event=event, genres_list=genres_list, director = director, cast = cast)

# http://flask-sqlalchemy.pocoo.org/2.1/queries/
def query_by_id(id):
	result = Event.query.filter(Event.id==id).first()
	if result:
		return result
	else:
		return None


def event_genre(id):
    genre_list = Genre.query.filter_by(event_id=id).all()
    result = []
    for i in genre_list:
        genre = i.name.strip()
        if genre:
            result.append(genre)

    if len(result) > 1:
        return list(set(result))
    else:
        return []

def event_director(id):

    directors = db.session.query(movie_director).filter_by(event_id=id).all()
    result = []

    for director in directors:
        director_name = CrewMember.query.filter_by(id=director[1]).first()
        if director_name.firstName.strip():
            result.append(director_name.firstName.strip())

    return list(set(result[:2]))

def event_cast(id):

    cast = db.session.query(movie_actor).filter_by(event_id=id).all()
    result = []

    for actor in cast:
        actor_name = Actor.query.filter_by(id=actor[1]).first()
        new = actor_name.firstName.strip()
        if new:
            result.append(new)

    return result[:3]
