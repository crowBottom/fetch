from flask import Flask, flash, request, render_template, redirect
from methods import *

app = Flask(__name__)

@app.route("/")
def root_route():
    return redirect("/home")

@app.route("/home")
def home_route():
    list = get_all_list_items()
    return render_template("home.html", list=list)
