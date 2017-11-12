import sys
import glob
import os
from math import log
import nltk
from nltk import word_tokenize
from nltk import FreqDist
import sys
import math
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
import json
import store_scores_gui
from store_scores_gui import main_class
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		query = request.form["query"]

	html="<!DOCTYPE html> <head><link rel=stylesheet type=text/css href=static/styles/bootstrap.min.css></head><body>"
	html+="<div class='text-center'><h2>Search results for <i><b>"+query+"</b></i></h2></div><hr>"

	result = main_class.process_function(query)
	for docname in result:
		html+="<div class='col-xs-12'><a>"+docname+"</a></div>"

	html+="<div class='text-center'><h3><a href=/>Search Again</a></h3></div>"
	html+="</body></html>"

	return html


if __name__ == '__main__':
	app.run(debug = True)