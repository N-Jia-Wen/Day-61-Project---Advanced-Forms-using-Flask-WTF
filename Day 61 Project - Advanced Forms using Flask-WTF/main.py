from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


# Just a test key, do change to something more secure:
WTF_CSRF_SECRET_KEY = '123456789'


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='Log In', validators=[DataRequired()])


app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = WTF_CSRF_SECRET_KEY


@app.route("/")
def home():
    return render_template('index.html', bootstrap=bootstrap)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit() is True:
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html", bootstrap=bootstrap)
        else:
            return render_template("denied.html", bootstrap=bootstrap)
    return render_template("login.html", form=form, bootstrap=bootstrap)


if __name__ == '__main__':
    app.run(debug=True)
