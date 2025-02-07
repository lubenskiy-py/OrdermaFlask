from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Reviews(FlaskForm):
    review = StringField('Відгук', validators=[DataRequired()])
    grade = IntegerField('Оцінка', validators=[DataRequired()])
    submit = SubmitField('Відправити')
