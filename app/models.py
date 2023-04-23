from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

# For a one-to-many relationship, a db.relationship field is normally defined on the "one" side, and is used as a convenient way to get access to the "many". 
# So for example, if I have a user stored in u, the expression u.posts will run a database query that returns all the posts written by that user. The first argument to db.relationship is the model class that represents the "many" side of the relationship. This argument can be provided as a string with the class name if the model is defined later in the module. The backref argument defines the name of a field that will be added to the objects of the "many" class that points back at the "one" object. 
# This will add a post.author expression that will return the user given a post.

    def __repr__(self):
        return '<User {}>'.format(self.username)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# In general, you will want to work with UTC dates and times in a server application. 
# This ensures that you are using uniform timestamps regardless of where the users are located. 
# These timestamps will be converted to the user's local time when they are displayed.

    def __repr__(self):
        return '<Post {}>'.format(self.body)