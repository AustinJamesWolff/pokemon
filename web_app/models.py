from flask_sqlalchemy import SQLAlchemy

# Open a DB connection
DB = SQLAlchemy()

class Pokemon(DB.Model):
    # Create table schema
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    name = DB.Column(DB.String, nullable=False)
    ability = DB.Column(DB.String, nullable=False)