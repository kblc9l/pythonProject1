import os

from flask import Flask, render_template, request

app = Flask(__name__)
href = '../static/img/img_2.png'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route("/training/<prof>")
def train(prof):
    return render_template("prif.html", prof=prof)


@app.route('/results/<nickname>/<level>/<rating>')
def res(nickname, level, rating):
    return render_template('result.html', nickname=nickname, level=str(level), rating=str(rating))


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    global href
    if request.method == 'GET':
        return f'''<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Title</title>
                        <link rel="stylesheet" type='text/css' href="../static/css/style.css">
                    </head>
                    <body>
                    <h1>Загрузите фотографии</h1>
                    <h2>для участия в миссии</h2>


                    <form method="post" enctype="multipart/form-data">
                        <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                            <img src='{href}' alt="">
                        </div>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>


                    </body>
                    </html>
'''
    elif request.method == 'POST':

        f = request.files['file']
        href = '../static/img/2.png'
        if f:
            f.save('static/img/2.png')
            return f'''<!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <title>Title</title>
                                    <link rel="stylesheet" type='text/css' href="../static/css/style.css">
                                </head>
                                <body>
                                <h1>Загрузите фотографии</h1>
                                <h2>для участия в миссии</h2>


                                <form method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                        <img src='{href}' alt="">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>


                                </body>
                                </html>'''


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)