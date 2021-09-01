from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/<string:page>")
def page(page=None):
    return render_template(page)


@app.route("/submit_contact", methods=["POST", "GET"])
def submit_contact():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            return render_template("/thank_you.html", name=data["email"])
        except:
            return render_template("contact.html")
