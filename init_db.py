from models import db, Pizza
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()
    pizza1 = Pizza(name='Маргарита', price=3, ingredients='Помідори, сир, соус')
    pizza2 = Pizza(name='Пеппероні', price=3.5, ingredients='Салямі, сир, соус')
    pizza3 = Pizza(name='Гавайська', price=4, ingredients='Курка, ананас, сир, соус')
    db.session.add_all([pizza1, pizza2, pizza3])
    db.session.commit()