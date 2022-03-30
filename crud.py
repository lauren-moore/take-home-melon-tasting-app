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

def get_timeslot_by_date(date):
    '''get timeslot by date'''

    return Timeslot.query.filter(Timeslot.date == date).first()

def get_user_by_id(user_id):
    '''get user by id'''

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def update_timeslot(date, user):
    '''update timeslot by adding user'''

    timeslot =  Timeslot.query.filter(Timeslot.date == date).first()
    timeslot.user = user

    return timeslot

def delete_reservation(timeslot, user):
    '''delete a user's reservation.'''




if __name__ == '__main__':
    from server import app
    connect_to_db(app)