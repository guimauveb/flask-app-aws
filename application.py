from flask import Flask, jsonify, redirect, url_for, render_template

import MySQLdb

application = Flask(__name__)
application.config["TEMPLATES_AUTO_RELOAD"] = True

# Keep the browser from using cache so it always gets the latest version of the files from the server
@application.after_request
def after_request(response):

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"

    return response

@application.route('/', methods=["GET"])
def index():

    db = MySQLdb.connect(host="host",
            		 port=3306,
            		 user="user",
            		 passwd="password",
            		 db="db",
            		 autocommit=True,
            		 use_unicode=True
            		)
    cursor = db.cursor()
    query = """SELECT * FROM languages;"""
    cursor.execute(query)
    languages = cursor.fetchall()
    # convert to a list
    languages = [list(l) for l in languages]

    print(languages)

    return render_template("index.html", languages=languages)
