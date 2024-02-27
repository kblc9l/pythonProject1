from flask import Flask
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from data import db_session
from data.users import User

SqlAlchemyBase = orm.declarative_base()

__factory = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = 'Ridley'
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)

    user = User()
    user.surname = "Scott2"
    user.name = 'Ridley2'
    user.age = 211
    user.position = "captain12123"
    user.speciality = "research engineerasdad"
    user.address = 'module_1adsads'
    user.email = 'scott_chief@mars.orgasdadasdaSD'
    db_sess = db_session.create_session()
    db_sess.add(user)

    user = User()
    user.surname = "Scott2QWEEQEW"
    user.name = 'Ridley2QWEQWEQE'
    user.age = 2113
    user.position = "captain12123QWEQWEE"
    user.speciality = "research engineerasdadQDWDQWE"
    user.address = 'module_1adsadQDWDQWDQDSs'
    user.email = 'scott_chief@mars.orgasdadasdaSDQDSDQD'
    db_sess = db_session.create_session()
    db_sess.add(user)

    db_sess.commit()

    user = db_sess.query(User).first()
    print(user.name)
    app.run()


if __name__ == '__main__':
    main()
