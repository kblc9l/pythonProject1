from flask import Flask, render_template, request
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['GET', 'POST'])
def work():
    db_sess = db_session.create_session()
    return render_template('index.html', info=db_sess.query(User, Jobs).filter(User.id == Jobs.team_leader))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        password = request.form['password']
        user = User()
        user.surname = request.form['surname']
        user.name = request.form['name']
        user.age = request.form['age']
        user.position = request.form['position']
        user.speciality = request.form['speciality']
        user.address = request.form['address']
        user.email = request.form['login']
        user.hashed_password = request.form['confirm_password']

        db_session.global_init("db/blogs.db")
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        db_sess.close()

        return 'Registration successful'

    return render_template('register.html')

def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8000, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
