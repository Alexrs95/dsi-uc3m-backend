##Dependencies
###Add new dependency
Edit the file requirements.txt adding the new dependency and the version.
###Install dependencies
Run `pip install -r requirements.txt` to download the dependencies
##Running
Execute `python run.py` et voilà from inside the `app/` folder.

## Libraries
- [SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/quickstart/)
- [Flask](http://flask.pocoo.org/)
- [Blueprints](http://flask.pocoo.org/docs/0.10/blueprints/)
- [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/)

**The default branch is integration.**

- New feature: git checkout -b feature/nameofyourfeature
- Bugfix: git checkout -b bugfix/nameofthefix

**If you push to master, I will find you and I will kill you**

##Endpints
- `/`: index
- `/search?query={query}&category={category}`:
	- `{query}`: text of the search
	- `{category}`: category for searching
	- Example: /search?query=Star&category=2
	- TODO: Define IDs for the categories