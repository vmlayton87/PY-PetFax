from flask import (Blueprint, render_template)
import json

# open the file containing the pet info but label it as pets, but pass it into json so that python can read the json file.
pets = json.load(open('pets.json'))
# print pets to see the data in the terminal
# print(pets)

# initializes the blueprint named pet that goes to /pets
bp = Blueprint('pet', __name__, url_prefix="/pets")

# creates a controller for the url extension /pets
@bp.route('/')
# render the html for the page
def index():
    # similar to res.render() in express, tell it the file to use, and any variables/attributes to be used.
    return render_template('index.html', pets = pets)

# create a show route for the individual pet
@bp.route('/<int:pet_id>')
def show(pet_id): 
    # not using a fetch to a database, so need to create an index for the pets.json objects
    pets_index = pet_id -1
    return render_template('show.html', pet=pets[pets_index])