from flask import Flask
from models import db, Game

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    game = Game(name='super mario', genre='platformer', rating='9/10')
    db.session.add(game)
    db.session.commit()

    games = Game.query.all()
    for game in games:
        print(game)