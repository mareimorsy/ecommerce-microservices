import flask
from flask import request, jsonify,render_template
from flask_pymongo import PyMongo

app = flask.Flask(__name__,template_folder='template')
app.config["DEBUG"] = True
app.config["MONGO_URI"] = "mongodb://172.17.0.2:27017/booksDB"
mongo = PyMongo(app)



@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/books', methods=['GET'])
def returnBooks():
    return render_template("books.html",books=mongo.db.myCollection.find())




@app.route('/getSpecificBook', methods=['GET'])
def getSpecificBook():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    book = mongo.db.myCollection.find({"id":id})
    return render_template("books.html",books=book)
app.run()
