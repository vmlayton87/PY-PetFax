from flask import (Blueprint, render_template, request, redirect)
from . import models
# import json

# open the file containing the pet info but label it as pets, but pass it into json so that python can read the json file.
# pets = json.load(open('pets.json'))
# print pets to see the data in the terminal
# print(pets)

# initializes the blueprint named pet that goes to /facts
bp = Blueprint('facts', __name__, url_prefix="/facts")

# creates a controller for the url extension /pets
@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        
        # using the request method and form input names to set variables
        submitter = request.form['submitter']
        fact = request.form['fact']

        # adding requested info to database
        new_fact = models.Fact(submitter=submitter, fact=fact)
        # creates the instance
        models.db.session.add(new_fact)
        # commits the instance to the db
        models.db.session.commit()

        
        return redirect('/facts')

    # for the get route query the facts table from the db
    results = models.Fact.query.all()
    # returns an object that can use dot notation
    # for result in results:
    #     print(result) 

    # passing the results as a paramater so the index.html can access it. 
    return render_template('facts/index.html', facts=results)

@bp.route('/new')
# render the html for the page
def new():
    # similar to res.render() in express, tell it the file to use, and any variables/attributes to be used.
    return render_template('facts/new.html')

