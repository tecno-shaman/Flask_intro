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


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
