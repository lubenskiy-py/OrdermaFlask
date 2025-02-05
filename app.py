from flask import Flask, render_template, request
from models import db, Pizza
from r import response, translate_weather



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)


@app.route("/homepage")
def homepage():
    data = {
        "weather" : translate_weather,
        "temp" : response["main"]["temp"]
    }
    return render_template("homepage.html", data=data)


@app.route("/menu")
def menu():
    pizzas = Pizza.query.all()
    context = {
        'title': 'Меню',
        'pizzas': pizzas,
    }
    return render_template("menu.html", **context)


@app.route("/form-for-get-pizza")
def get_pizza():
    return render_template ("form_for_get_pizza.html")


@app.route("/get-pizza", methods=["POST"])
def get_user_data():
    user_email = request.form.get("email") # тут можна було б зробити так щоб користувач отримав на свою пошту письмо з підтвердженням але це дуже складно для мене, я пробував це зробити але не вийшло
    bank_card = request.form.get("bank_card")
    return "Ваша піцца приїде за 20 хвилин"


@app.route("/")
def navigation():
    return render_template("navigation.html")




if __name__ == '__main__':
    app.run(debug=True)