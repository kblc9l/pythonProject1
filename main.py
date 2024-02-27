import os

from flask import Flask, render_template, request

app = Flask(__name__)
href = '../static/img/img_2.png'


@app.route('/list_prof/<typeL>')
def list_prof(typeL: str):
    profs = ''' менеджер по продажам,
                продавец-консультант,
                водитель,
                бухгалтер,
                программист, разработчик программного обеспечения,
                врач,
                инженер,
                повар,
                упаковщик и комплектовщик,
                слесарь,
                сантехник'''.strip().split(',')
    return render_template('prof_list.html', title='Список профессий для полёта на Марс', profs=profs, typeL=typeL, )


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
