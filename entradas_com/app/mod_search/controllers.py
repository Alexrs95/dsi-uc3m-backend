from flask import Blueprint, render_template, request, make_response, session
from app.models import *

mod_search = Blueprint('search', __name__,)


@mod_search.route('/search/', methods=['POST'])
def search():
	query = request.form['query']
	events = query_by_event_name(query)
	if request.cookies.get('busqueda'):
		value = str(request.cookies.get('busqueda') + ',' + str(query))
	else:
		value = str(query)
	if 'username' in session:
		user = session['username']
		resp = make_response(render_template("search/search-results.html", query=query, events=events, user=user))
	else:
		resp = make_response(render_template("search/search-results.html", query=query, events=events))
	resp.set_cookie('busqueda', value)
	return resp

# http://flask-sqlalchemy.pocoo.org/2.1/queries/
def query_by_event_name(look_for):
	result = Event.query.filter(Event.title.like("%" + look_for + "%")).all()
	if result:
		return result
	else:
		return []
