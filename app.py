import os
from functools import wraps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Initialize app
app = Flask(__name__)

# Config app
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# @login_required decorator
# https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # no "user" in session
        if "user" not in session:
            flash("You must log in to view this page")
            return redirect(url_for("login"))
        # user is in session
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/home")
def home():
    return render_template("base.html") # build home.html for this def


@app.route("/get_comics")
@login_required
def get_comics():
    comics = list(mongo.db.comics.find())
    user = mongo.db.user.find_one(
        {"username": session["user"]})

    return render_template("comics.html", comics=comics, user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # check if passwords match
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        if password != confirm_password:
            flash("Your passwords don't match", 'error')
            return redirect(url_for("register"))

        register = {
            "fullname": request.form.get("fullname").title(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email"),
            "avatar_no": int(request.form.get("avatar_no")),
            "is_admin": False,
            "my_catalogue": []
        }
        mongo.db.user.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    if request.method == "POST":
        # grab the session user's username from the db
        user = mongo.db.user.find_one(
            {"username": session["user"]})
        show_contact_details = "on" if request.form.get("show_contact_details") else "off"
        mongo.db.user.update_one(
            {"username": session["user"]},
            {"$set": {"fullname": request.form.get("fullname"),
                "email": request.form.get("email"),
                "username": request.form.get("username"),
                "avatar_no": int(request.form.get("avatar_no")),
                "show_contact_details": show_contact_details}})

        session["user"] = request.form.get("username").lower()
        username = user["username"]

        return redirect(url_for("profile", username=username))

    if "user" in session:
        user = mongo.db.user.find_one(
            {"username": session["user"]})
        return render_template("profile.html", user=user)

    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_comic", methods=["GET", "POST"])
@login_required
def add_comic():
    if request.method == "POST":
        for_sale = "on" if request.form.get("for_sale") else "off"
        show_contact_details = "on" if request.form.get("show_contact_details") else "off"
        comic = {
            "title": request.form.get("title"),
            "publisher_name": request.form.get("publisher_name"),
            "year": request.form.get("year"),
            "issue_no": request.form.get("issue_no"),
            "grade": request.form.get("grade"),
            "for_sale": for_sale,
            "price": request.form.get("price"),
            "notes": request.form.get("notes"),
            "image_url": request.form.get("image_url"),
            "show_contact_details": request.form.get("show_contact_details"),
        }

        mongo.db.comics.insert_one(comic)
        flash("Comic Successfully Added")
        return redirect(url_for("get_comics"))

    publishers = mongo.db.publishers.find().sort("publisher_name", 1)
    return render_template("add_comic.html", publishers=publishers)


@app.route("/edit_comic/<comic_id>", methods=["GET", "POST"])
@login_required
def edit_comic(comic_id):
    if request.method == "POST":
        for_sale = "on" if request.form.get("for_sale") else "off"
        show_contact_details = "on" if request.form.get("show_contact_details") else "off"
        submit = {
            "title": request.form.get("title"),
            "publisher_name": request.form.get("publisher_name"),
            "year": request.form.get("year"),
            "issue_no": request.form.get("issue_no"),
            "grade": request.form.get("grade"),
            "for_sale": for_sale,
            "price": request.form.get("price"),
            "notes": request.form.get("notes"),
            "image_url": request.form.get("image_url"),
            "show_contact_details": request.form.get("show_contact_details"),
        }

        mongo.db.comics.update({"_id": ObjectId(comic_id)}, submit)
        flash("Comic Successfully Updated")

    comic = mongo.db.comics.find_one({"_id": ObjectId(comic_id)})

    publishers = mongo.db.publishers.find().sort("publisher_name", 1)
    return render_template("edit_comic.html", comic=comic, publishers=publishers)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
