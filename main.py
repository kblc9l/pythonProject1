from flask import Flask, render_template

app = Flask(__name__)


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

# @app.route('/choice/<planet_name>')
# def choice(planet_name):
#     with open('1lesson/choice.html', encoding='utf8') as f:
#         return str(f.read()).replace('{planet}', planet_name)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
