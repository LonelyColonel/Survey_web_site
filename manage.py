from flask import Flask, render_template, redirect
from forms.login_form import LoginForm
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
@app.route('/index')
@app.route('/page')
def index():
    return render_template(template_name_or_list='page.html', title='test')


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        return redirect('/success')

    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
