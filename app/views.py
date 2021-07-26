from flask import Flask, render_template, redirect, url_for, request, abort

app = Flask(__name__)


@app.route("/")
def Index():
    return render_template("index.html")


@app.route("/contactlist")
def ContactList():
    kisiler = [
        ["hazal", "yd@gmail.com", "12345"],
        ["hasem", "yd@gmail.com", "123"],
        ["beryas", "ydyd@gmail.com", "9876"]
    ]
    return render_template("contact_list.html", kisiler_list=kisiler)


@app.route("/contact", methods=["POST", "GET"])
def Contact():
    if request.method == "POST":
        pass
    return render_template("contact.html")


@app.route("/login", methods=["POST", "GET"])
def Login():
    if request.method == "POST":
        if request.form:
            if "username" in request.form and "password" in request.form:
                username = request.form["username"]
                password = request.form["password"]
                if username == "hazal" and password == "12345":
                    return redirect(url_for("Index"))
                else:
                    return redirect(url_for("Login"))
        abort(400)
    return render_template("login.html")
