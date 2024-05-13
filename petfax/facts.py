from flask import (Blueprint, render_template)
# import json

# open the file containing the pet info but label it as pets, but pass it into json so that python can read the json file.
# pets = json.load(open('pets.json'))
# print pets to see the data in the terminal
# print(pets)

# initializes the blueprint named pet that goes to /facts
bp = Blueprint('facts', __name__, url_prefix="/facts")

# creates a controller for the url extension /pets
@bp.route('/new')
# render the html for the page
def new():
    # similar to res.render() in express, tell it the file to use, and any variables/attributes to be used.
    return render_template('facts.html')

