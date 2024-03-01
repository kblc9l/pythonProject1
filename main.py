import datetime

from flask import Flask
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from data import db_session
from data.jobs import Jobs
from data.users import User

SqlAlchemyBase = orm.declarative_base()

__factory = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    # name_db = input()
    # db_session.global_init(name_db)
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    people = db_sess.query(User).filter(User.address == 'module_1')
    print(*people)

    app.run()


if __name__ == '__main__':
    main()
