from flask import Flask 

def create_app(): 
    # initializing a flask application
    app = Flask(__name__)

    # creating a route for the url extenstion /
    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    # from the same folder, import the blueprint named pet
    from . import pet

    # register the blueprint in our app by using the corresponding built in method
    app.register_blueprint(pet.bp)

    return app
