"""Models for the Melon Tasting Reservation Scheduler app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""
 
    __tablename__ = "users"
    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    
    
    def __repr__(self):
        return f'<User user_id={self.user_id} name={self.name} email={self.email}>'


class Timeslot(db.Model):
    """A timeslot."""
 
    __tablename__ = "timeslots"

    timeslot_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    date = db.Column(db.Datetime, nullable=False, unique=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", backref="timeslots")
    
    def __repr__(self):
        return f'<Timeslot timeslot_id={self.timeslot_id} date={self.date}>'



def connect_to_db(flask_app, db_uri="postgresql:///melontasting", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
