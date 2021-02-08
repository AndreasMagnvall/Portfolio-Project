#! /usr/bin/env python3
#-*- coding: utf-8 -*-

from flask import *
from data import *
from jinja2.ext import loopcontrols

app = Flask(__name__)

# returns the template page for an error specified by the "error_type" argument.
def get_error_page(error_type):
    message = ""
    if error_type == "database_load_error":
        message = "Database error.\nDatabase could not load correctly.\nEither the database file \"data.json\" doesn't exist, the json-file is formatted incorrectly, or multiple projects have the same id."
    elif error_type == "user_load_error":
        message = "User config error.\nUser info file could not load correctly.\nThere should be a file called \"user.json\" in the same folder as the portfolio program."
    elif error_type == "empty_database_error":
        message = "Database error.\nDatabase is empty."
    elif error_type == "project_search_error":
        message = "Search error.\nThe project with the specified id could not be found."
    elif error_type == "invalid_address_error":
        message = "Invalid address.\nThe specified address could not be found on the server."
    return render_template("error_template.html", error_message = message)

@app.route("/")
def index():
    try:
        db = load("data.json")
    except:
        return get_error_page("database_load_error")

    try:
        user_info = load("user.json")
    except:
        return get_error_page("user_load_error")

    print(db)
    return render_template("/portfolio/index.html",name = None,projects = db,startindex = 0,endindex = 4,user_info=user_info)

@app.route("/techniques")
def techniques():
    try:
        db = load("data.json")
    except:
        return get_error_page("database_load_error")

    tech_list = get_techniques(db)
    tech_stats = get_technique_stats(db)
    return render_template("/portfolio/techniques.html", projects = db, techniques = tech_list, stats = tech_stats)

@app.route("/list")
def list():
    try:
        db = load("data.json")
    except:
        return get_error_page("database_load_error")

    tech_list = get_techniques(db)
    keys = get_keys(db)
    return render_template("/portfolio/list.html", projects = db, techniques = tech_list, key_list = keys)

@app.route('/get_search_fields', methods=['POST','GET'])
def get_search_fields():
    try:
        db = load("data.json")
    except:
        return get_error_page("database_load_error")

    searchf = {"search":"","techniques":[],"search_fields":[]}
    print(searchf["techniques"])
    print(request.form["data"])
    searchf = json.loads(request.form["data"])
    print(len(searchf["search_fields"]))
    print(searchf)

    if(len(searchf["techniques"]) > 0 and len(searchf["search_fields"]) > 0):
        return jsonify(search(db,search= searchf["search"],techniques=searchf["techniques"],search_fields=searchf["search_fields"]))
    elif(len(searchf["techniques"]) > 0):
        return jsonify(search(db,search= searchf["search"],techniques=searchf["techniques"]))
    elif(len(searchf["search_fields"]) > 0):
        return jsonify(search(db,search= searchf["search"],search_fields=searchf["search_fields"]))
    else:
        return jsonify(search(db,search= searchf["search"]))

@app.errorhandler(404)
def error404(error):
   return get_error_page("invalid_address_error")

@app.route("/projects/<int:project_id>")
def project(project_id):
    try:
        db = load("data.json")
    except:
        return get_error_page("database_load_error")

    if not db:
        return get_error_page("empty_database_error")
    else:
        for project in db:
            if project["project_id"] == project_id:
                return render_template("project_template.html", project_dict = project)
        return get_error_page("project_search_error")

if __name__ == "__main__" :
    app.run(debug = True)
