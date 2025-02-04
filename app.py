from flask import Flask, render_template
from models import db, Pizza

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

@app.route("/homepage")
def homepage():
    return render_template("homepage.html", title='Orderman')

@app.route("/menu")
def menu():
    pizzas = Pizza.query.all()
    context = {
        'title': 'Меню',
        'pizzas': pizzas,
    }
    return render_template("menu.html", **context)


@app.route("/")
def navigation():
    return render_template("navigation.html")




if __name__ == '__main__':
    app.run(debug=True)