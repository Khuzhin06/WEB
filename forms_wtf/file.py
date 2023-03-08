from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField


class FileForm(FlaskForm):
    file = FileField('Загрузите файл')
    submit = SubmitField('Загрузить')
