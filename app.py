from flask import Flask, render_template, request, redirect, url_for
from models import db, Pizza, Review
from r import response, translate_weather
from form import Reviews

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = 'SECRET_KEY'
db.init_app(app)

@app.route("/homepage")
def homepage():
    data = {
        "weather": translate_weather,
        "temp": response["main"]["temp"]
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
    return render_template("form_for_get_pizza.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = Reviews()
    if form.validate_on_submit():
        if form.grade.data > 5 or form.grade.data < 1:
            return "Оцінка повинна бути від 1 до 5"
        new_review = Review(review=form.review.data, grade=form.grade.data)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('rewiew.html', form=form)

@app.route('/success')
def success():
    return 'Дякуємо за ваш відгук'

@app.route("/reviews")
def reviews():
    all_reviews = Review.query.all()
    return render_template("check_reviews.html", reviews=all_reviews)

@app.route("/get-pizza", methods=["POST"])
def get_user_data():
    user_email = request.form.get("email")
    bank_card = request.form.get("bank_card")
    return "Ваша піцца приїде за 20 хвилин"

@app.route("/")
def navigation():
    return render_template("navigation.html")

if __name__ == '__main__':
    app.run(debug=True)