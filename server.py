"""Server for melon tasting scheduler app."""
from flask import Flask, render_template, request, flash, session, redirect
from model import db, connect_to_db
from jinja2 import StrictUndefined
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/appointments')
def all_movies():
    """View available appointments page."""

    avail_timeslots = crud.get_available_timeslots()

    return render_template('appointments.html', avail_timeslots=avail_timeslots)


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
