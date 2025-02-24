from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def goals():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def ad():
    message = """Человечество вырастает из детства.

Человечеству мала одна планета.

Мы сделаем обитаемыми безжизненные пока планеты.

И начнем с Марса!

Присоединяйся!"""
    return "<br>".join(message.split('\n'))


@app.route('/image_mars')
def show_mars():
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for("static", filename="img/MARS.png")}" alt="Изображение марса">
                    <p>Вот она какая красная планета</p>
                  </body>
                </html>'''


@app.route('/promotion_image')
def modern_ad():
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for("static", filename="css/style.css")}">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for("static", filename="img/MARS.png")}" alt="Изображение Марса">
                    <div class="alert alert-primary" role="alert" id="n1">
                      Человечество вырастет из детства.
                    </div>
                    <div class="alert alert-primary" role="alert" id="n2">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-primary" role="alert" id="n3">
                        Мы сделаем обитаемым безжизненные пока планеты.
                    </div>
                    <div class="alert alert-primary" role="alert" id="n4">
                      И начнем с Марса!
                    </div>
                    </div>
                    <div class="alert alert-primary" role="alert" id="n5">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
