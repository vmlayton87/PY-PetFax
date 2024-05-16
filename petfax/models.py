from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

# creating the Fact model
class Fact(db.Model):
    # adding a table named facts
    __tablename__ = 'facts'

    # adding items to the table
    id = db.Column(db.Integer, primary_key = True)
    submitter = db.Column(db.String(250))
    fact = db.Column(db.Text)