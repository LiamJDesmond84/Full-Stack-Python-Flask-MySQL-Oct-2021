from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("dojos.html", all_dojos=Dojo.get_all())

@app.route("/newninja")
def newninja():
    return render_template("newninjas.html",all_dojos=Dojo.get_all())

@app.route("/createninja", methods=["POST"])
def createninja():
    data = {
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    id = request.form['dojo_id']
    Ninja.save(data)
    return redirect(f'/dojoshow/{id}')

@app.route("/createdojo", methods=["POST"])
def createdojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route("/dojoshow/<int:dojo_id>")
def dojoshow(dojo_id):
    data = {"id": dojo_id}
    dojos=Dojo.get_dojo_with_ninjas(data)
    return render_template("dojoshow.html", dojos=dojos)

@app.route('/roster')
def ninjas1():
    return render_template("roster.html",all_ninjas=Ninja.get_all())

@app.route('/show/<int:ninja_id>')
def detail_page(ninja_id):
    data = {
        'id': ninja_id
    }
    return render_template("details_page.html",ninja=Ninja.get_one(data))

@app.route('/edit_page/<int:ninja_id>')
def edit_page(ninja_id):
    data = {
        'id': ninja_id
    }
    return render_template("edit_page.html", ninja = Ninja.get_one(data))

@app.route('/update/<int:ninja_id>', methods=['POST'])
def update(ninja_id):
    data = {
        'id': ninja_id,
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age']
    }
    Ninja.update(data)
    return redirect(f"/show/{ninja_id}")

@app.route('/delete/<int:ninja_id>')
def delete(ninja_id):
    data = {
        'id': ninja_id,
    }
    Ninja.destroy(data)
    return redirect('/roster')