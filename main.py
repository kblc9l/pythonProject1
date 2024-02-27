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
    db_session.global_init("db/blogs.db")
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now
    job.is_finished = False

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    job = db_sess.query(Jobs).first()
    print(job.name)
    app.run()


if __name__ == '__main__':
    main()
