"""CRUD operations."""

from model import db, User, Timeslot, connect_to_db


def create_user(name, email):
    """Create and return a new user."""

    user = User(name=name, email=email)

    return user

def create_timeslot(date, user=None):
    """Create and return a new timeslot."""

    timeslot = Timeslot(date=date, user=user)

    return timeslot

def get_timeslots():
    """Return all timeslots."""

    return Timeslot.query.all()

def get_timeslots_by_users(user):
    '''get timeslot by user id'''

    return Timeslot.query.filter(Timeslot.user == user).all()

def get_user_by_id(user_id):
    '''get user by id'''

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)