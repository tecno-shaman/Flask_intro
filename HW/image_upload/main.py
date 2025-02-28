from flask import url_for, Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Загрузка фото</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии</h1>
                            <p>для участия в миссии</p>
                            <div>

                                <form class="login_form" method="post" enctype="multipart/form-data">
                                     
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                        <img src='{url_for('static', filename='img/photo.png')}' alt='лицо астронавта'>
                                    </div>

                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files["file"]
        try:
            f.save("static/img/photo.png")

        except Exception:
            print("Не удалось сохранить фото")
        print(f)
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port='8080', host='127.0.0.1')
