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


@app.route('/astronaut_selection')
def astronaut_selection():
    with open('astronaut_selection.html', encoding='utf8') as f:
        return f.read()


# @app.route('/choice/<planet_name>')
# def choice(planet_name):
#     return f'''<!DOCTYPE html>
#                     <html lang="en">
#                     <head>
#                         <meta charset="UTF-8">
#                         <title>Title</title>
#                         <link rel="stylesheet" href="C:\\Users\\User\
#                         \PycharmProjects\\pythonProject1\\static\\css\\style.css">
#                     </head>
#                     <body>
#                     <h2 class="choice_planet">Мое предложение: {planet_name}</h2>
#                     <p class="p1">Эта планета близка к Земле;</p>
#                     <p class="p2">На ней много необходимых ресурсов;</p>
#                     <p class="p3">На ней есть вода и атмосфера;</p>
#                     <p class="p4">На ней есть небольшое магнитное поле;</p>
#                     <p class="p5">Наконец, она просто красива!</p>
#                     </body>
#                     </html>'''

@app.route('/choice/<planet_name>')
def choice(planet_name):
    with open('choice.html', encoding='utf8') as f:
        return str(f.read()).replace('{planet}', planet_name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
