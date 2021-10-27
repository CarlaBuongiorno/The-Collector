import os
import re
from functools import wraps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env  # noqa

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
    """
        Render template for homepage
    """
    return render_template("home.html")


@app.route("/get_comics")
@login_required
def get_comics():
    """
        Get all user's comics from database and
        display them on 'My Catalogue' page.
    """
    comics = []
    # Credit to Sean from Code Institute Tutor Support for his help with this code snippet
    user = mongo.db.user.find_one({"username": session["user"]})
    comic_id_collection = user["my_catalogue"]

    for comic_id in comic_id_collection:
        comic = mongo.db.comics.find_one({"_id": ObjectId(comic_id)})
        comics.append(comic)

    return render_template("my_catalogue.html", comics=comics, user=user)


@app.route("/get_collection")
@login_required
def get_collection():
    """
        Get all comics in the database to
        display on 'The Collection' page.
    """
    comics = list(mongo.db.comics.find())
    user = mongo.db.user.find_one({"username": session["user"].lower()})
    return render_template("the_collection.html", comics=comics, user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
        Get the user's username from the form and check if it already exists in the
        database. If it does, flash a message to the user and redirect to registration
        page. Check if passwords match and in the correct format. Save user in the database,
        put user into a session cookie and redirect to profile page.
    """
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

        # check if password conforms to pattern
        is_digit = re.compile(r"[0-9]")
        is_lower = re.compile(r"[a-z]")
        is_upper = re.compile(r"[A-Z]")

        if is_digit.search(password) is None or \
            is_lower.search(password) is None or \
                is_upper.search(password) is None:
            return redirect(url_for("register"))

        show_contact_details = "on"

        register = {
            "fullname": request.form.get("fullname").title(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email"),
            "avatar_no": int(request.form.get("avatar_no")),
            "show_contact_details": show_contact_details,
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
    """
        Find username in db, check that user's password matches what's in
        the db, render login page if no match, render profile page if match.
    """
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
    """
        Get username from db, get user's input for all fields and update in db.
        If user toggles on or off switch for showing their contact details to
        other collectors, save in db. Find user's comics and display/don't
        display email address to other users. Render profile page.
    """
    if request.method == "POST":
        # grab the session user's username from the db
        user = mongo.db.user.find_one(
            {"username": session["user"].lower()})
        show_contact_details = "on" if request.form.get(
            "show_contact_details") else "off"
        mongo.db.user.update_one(
            {"username": user["username"]},
            {"$set": {"fullname": request.form.get("fullname"),
                      "email": request.form.get("email"),
                      "username": request.form.get("username"),
                      "avatar_no": int(request.form.get("avatar_no")),
                      "show_contact_details": show_contact_details}})
        # Find all comics and update show comic details on or off
        mongo.db.comics.update_many(
            {"the_collector": user["username"]},
            {"$set": {"show_contact_details": show_contact_details}})

        flash("Your Profile Has Been Updated")
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
    """
    Remove user from session cookies. Render login page.
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route('/delete_account/<username>')
@login_required
def delete_account(username):
    """
    User can delete their account. Remove user from db.
    """
    mongo.db.user.remove({"username": username})
    flash("Your Account Has Been Deleted")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/add_comic", methods=["GET", "POST"])
@login_required
def add_comic():
    """
        Get session user, get input from user in add comic page, store it in
        db. If user chooses 'for sale' to be on, get price input. Save the
        comic Object Id in user collection as array. Render user's Catalogue
        page.
    """
    user = mongo.db.user.find_one({"username": session["user"].lower()})

    # User can add a comic
    if request.method == "POST":
        for_sale = "on" if request.form.get("for_sale") else "off"
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
            "the_collector": user["username"],
            "show_contact_details": user["show_contact_details"],
            "contact": user["email"]
        }

        catalogue = mongo.db.comics.insert_one(comic)
        _id = catalogue.inserted_id
        mongo.db.user.update_one({"username": session["user"]},
                                 {"$push": {"my_catalogue": _id}})
        flash("Comic Added")

        return redirect(url_for("get_comics"))

    publishers = mongo.db.publishers.find().sort("publisher_name", 1)
    return render_template("add_comic.html", publishers=publishers, user=user)


@app.route("/edit_comic/<comic_id>", methods=["GET", "POST"])
@login_required
def edit_comic(comic_id):
    """
    Render edit comic template. User can edit a comic. Get user's input and
    update in db. Redirect to My Catalogue page upon successful update.
    """
    if request.method == "POST":
        for_sale = "on" if request.form.get("for_sale") else "off"
        submit = {
            "title": request.form.get("title"),
            "publisher_name": request.form.get("publisher_name"),
            "year": request.form.get("year"),
            "issue_no": request.form.get("issue_no"),
            "grade": request.form.get("grade"),
            "for_sale": for_sale,
            "price": request.form.get("price"),
            "notes": request.form.get("notes"),
            "image_url": request.form.get("image_url")
        }

        mongo.db.comics.update({"_id": ObjectId(comic_id)}, submit)
        flash("Comic Successfully Updated")
        return redirect(url_for("get_comics"))

    comic = mongo.db.comics.find_one({"_id": ObjectId(comic_id)})

    publishers = mongo.db.publishers.find().sort("publisher_name", 1)
    return render_template("edit_comic.html",
                           comic=comic, publishers=publishers)


@app.route("/delete_comic/<comic_id>")
@login_required
def delete_comic(comic_id):
    """
    User can delete a comic. Find session user and user id, get
    the comic id from user's catalogue array. Delete comic from
    db, as well as comic id in user's array. Render My Catalogue page.
    If user is admin, user can delete other user's comics from the
    Collection.
    """
    user = mongo.db.user.find_one(
            {"username": session["user"]})
    user_id = user["_id"]
    mongo.db.user.update_one(
        {"_id": user_id},
        {"$pull": {"my_catalogue": ObjectId(comic_id)}}
    )
    mongo.db.comics.delete_one({"_id": ObjectId(comic_id)})
    flash("Comic Successfully Deleted")

    if user["is_admin"] is True:
        return redirect(url_for("get_collection"))

    return redirect(url_for("get_comics"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
