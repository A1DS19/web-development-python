from flask import Flask, render_template, request
from dotenv import load_dotenv
from config.db import db

app = Flask(__name__)
load_dotenv()

contacts = db.contacts


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:page>")
def page(page=None):
    return render_template(page)


@app.route("/submit_contact", methods=["POST", "GET"])
def submit_contact():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            contacts.insert_one(data)
            return render_template("/thank_you.html", name=data["email"])
        except Exception as err:
            print(err)
            return render_template("contact.html")
