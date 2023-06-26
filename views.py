from flask import render_template, redirect, url_for, request
from models import db, Game
from app import app

@app.route("/")
def index():
    games = Game.query.all()
    return render_template("index.html", games=games)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    elif request.method == "POST":
        name = request.form.get("name")
        genre = request.form.get("genre")
        rating = request.form.get("rating")
        game = Game(name=name, genre=genre, rating=rating)
        db.session.add(game)
        db.session.commit()
        return redirect(url_for("index"))  

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    game = Game.query.get_or_404(id)
    if request.method == "GET":
        return render_template("update.html", game=game)
    elif request.method == "POST":
        name = request.form.get("name")
        genre = request.form.get("genre")
        rating = request.form.get("rating")
        game.name = name
        game.genre = genre
        game.rating = rating
        db.session.commit()
        return redirect(url_for("index"))
    
@app.route("/delete/<int:id>")
def delete(id):
    game = Game.query.get_or_404(id)
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        query = request.form['query']
        results = db.session.query(Game).filter(Game.name.like(f'%{query}%')).all()
        return render_template('search_results.html', results=results)
    return render_template('search.html')