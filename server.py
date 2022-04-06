"""Server for melon tasting scheduler app."""
from flask import Flask, render_template, request, flash, session, redirect
from model import db, connect_to_db
from jinja2 import StrictUndefined
import crud
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/appointments')
def show_app():
    """View available appointments page."""

    return render_template('appointments.html')


@app.route("/appointments", methods=["POST"])
def create_app():
    """Create a new appointment."""

    year = request.form.get("year")
    month = request.form.get("month")
    day = request.form.get("day")
    time = request.form.get("time")

    date_str = f"{day}/{month}/{year} {time}"
    date = datetime.strptime(date_str, '%d/%m/%y %H:%M:%S')

    #get user from session
    user_logged_in = session.get("user_id")
    user = crud.get_user_by_id(user_logged_in)

    #create new appointment
    new_app = crud.create_timeslot(date, user)
    db.session.add(new_app)
    db.session.commit()
    flash("Your appointment has been set!")

    return redirect('/')


@app.route("/upcoming_apps")
def show_upcoming_apps():
    """Show all of user's reservations."""

    user_logged_in = session.get("user_id")
    user = crud.get_user_by_id(user_logged_in)

    upcoming_apps = crud.get_timeslots_by_user(user)

    return render_template('user_reservations.html',
                            upcoming_apps=upcoming_apps)


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")

    user = crud.get_user_by_email(email)
    if not user:
        flash("The email you entered was incorrect.")

        return redirect(request.referrer)

    else:
        session["user_email"] = user.email
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.name.title()}!")
        return redirect('/appointments')



@app.route("/logout")
def process_logout():
    """Log user out."""

    del session["user_id"]
    flash("You have logged out!")

    return redirect("/")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
