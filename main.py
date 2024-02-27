import os

from flask import Flask, render_template, request

app = Flask(__name__)
href = '../static/img/img_2.png'


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {'surname': 'sdfgsf',
            'name': 'sfasfs',
            'education': 'sfs',
            'profession': 'sfsaf',
            'sex': 'male',
            'motivation': 'sfsf',
            'ready': 'True'}
    return render_template('auto_answer.html', title='Автоматический ответ', data=data)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
