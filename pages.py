from flask import Blueprint, render_template, request, redirect, url_for, session, flash

pages = Blueprint("pages", __name__)  # Changed from home to pages

# Temporary in-memory storage for users
users_db = {}

@pages.route("/")
def home_page():
    return render_template("home.html")

@pages.route("/profile")
def profile():
    user = session.get("user")
    if not user:
        flash("You need to log in first!", "error")
        return redirect(url_for("pages.login"))
    return render_template("profile.html", username=user)

@pages.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users_db and users_db[username] == password:
            session["user"] = username
            return redirect(url_for("pages.profile"))
        else:
            flash("Invalid username or password!", "danger")
            return redirect(url_for("pages.login"))

    return render_template("login.html")

@pages.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users_db:
            flash("Username already exists! Choose another.", "danger")
            return redirect(url_for("pages.signup"))

        users_db[username] = password
        flash("Account created successfully! You can now log in.", "success")
        return redirect(url_for("pages.login"))

    return render_template("signup.html")

@pages.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("pages.home_page"))
