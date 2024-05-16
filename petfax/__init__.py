from flask import Flask 
import os
from dotenv import (load_dotenv, find_dotenv)

from flask_migrate import Migrate

load_dotenv(find_dotenv())

def create_app(): 
    # initializing a flask application
    app = Flask(__name__)

    # #connect to postgres database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_CONNECTION')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


    # config models
    from . import models
    # initializing SQLAlchemy to connect postgres to this flask app
    models.db.init_app(app)
    # initializes flask migrate to connect the models to the database
    migrate = Migrate(app, models.db)

    # creating a route for the url extenstion /
    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    # from the same folder, import the blueprint named pet
    from . import pet

    # register the blueprint in our app by using the corresponding built in method
    app.register_blueprint(pet.bp)

    from . import facts
    app.register_blueprint(facts.bp)

    return app
