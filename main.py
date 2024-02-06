from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index2():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '<br>'.join(['Человечество вырастает из детства.',
                        'Человечеству мала одна планета.',
                        'Мы сделаем обитаемыми безжизненные пока планеты.',
                        'И начнем с Марса!',
                        'Присоединяйся!'])


@app.route('/promotion_image')
def image_mars():
    with open('index.html', encoding='utf8') as f:
        return f.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
