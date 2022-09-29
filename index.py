import requests as req,json
import urllib.parse

from flask import Flask , jsonify ,request, send_file , render_template
from flask_cors import CORS
  
app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def page_not_found(e):
    
    return "Wkwkwkw", 404

def matchWord(hint,words):

	result = None

	for w in words:

		if set(hint.lower()).issubset(set(w['word'].lower())):

			result = {"result":True,"word":w['word'].upper()}

			break
		
		else:

			result = {"result":False,"word":"None"}

	return result


@app.route("/getWord/<term>/<hint>")
def getWord(term,hint):
  
	term = term.replace(" ","%20")

	url = f"https://reversedictionary.org/api/related?term={term}"

	fetch = req.get(url).json()[:20]

	result = matchWord(hint,fetch)

	return jsonify(result)


@app.route("/")
def hello_world():
  
  return 'Hello Ecandl.net'



  