# joining the path with the main files
import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

# import flask libaries
from flask import Flask, render_template, request,url_for
from flask_caching import Cache
from BlogScrapper.kdnuggets import kdnuggetsData
from BlogScrapper.analyticsVidhyads import analyticsdsData
from BlogScrapper.analyticsVidhyaml import analyticsMLData
from BlogScrapper.mygreatlearning import myGreatLearning
from BlogScrapper.tobbots import Aitrends


config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/kd')
@cache.cached(timeout=50,key_prefix='getdatakd')
def kdnuggets_page():
	data = kdnuggetsData()
	return render_template('kdnuggets.html',data=data)


@app.route('/avds')
# @cache.cached(timeout=50,key_prefix='getdataav')
def analyticsDs_page():
	data = analyticsdsData()
	return render_template('analyticsds.html',data=data)


@app.route('/avml')
# @cache.cached(timeout=50,key_prefix='getdataav')
def analyticsml_page():
	data = analyticsMLData()
	return render_template('analyticsml.html',data=data)

@app.route('/mgl')
def greatlearning_page():
	data = myGreatLearning()
	return render_template('greatlearning.html',data = data)

@app.route('/ai')
def aitrends_page():
	data = Aitrends()
	return render_template('aitrends.html',data = data)


if __name__ == '__main__':
	app.run(debug=True)

# print(data)