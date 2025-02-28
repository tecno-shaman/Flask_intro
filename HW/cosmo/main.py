from flask import Flask, url_for, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
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
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <p>на участие в миссии</p>
                            <div>
                            
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                
                                <div class="name_group">
                                <input type="last_name" class="form-control" id="last_name" placeholder="Введите фамилию" name="last_name">
                                <input type="first_name" class="form-control" id="first_name" placeholder="Введите имя" name="first_name">
                                </div>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>

                                        <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skill" id="job1" value="Инженер-исследователь">
                                          <label class="form-check-label" for="job1">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skill" id="job2" value="Инженер-строитель">
                                          <label class="form-check-label" for="job2">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                        <div clas="form-check">
                                          <input class="form-check-input" type="checkbox" name="skill" id="job3" value="Пилот">
                                          <label class="form-check-label" for="job3">
                                            Пилот
                                          </label>
                                          <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skill" id="job4" value="Метеоролог">
                                          <label class="form-check-label" for="job4">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div clas="form-check">
                                          <input class="form-check-input" type="checkbox" name="skill" id="job5" value="Инженер по жизнеобеспечению">
                                          <label class="form-check-label" for="job5">
                                            Инженер по жизнеобеспечению
                                          </label>
                                        </div>
                                    </div>
                                    <div clas="form-check">
                                          <input class="form-check-input" type="checkbox" name="skill" id="job6" value="Инженер по радиационной защите">
                                          <label class="form-check-label" for="job6">
                                            Инженер по радиационной защите
                                          </label>
                                          <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skill" id="job7" value="Врач">
                                          <label class="form-check-label" for="job7">
                                            Врач
                                          </label>
                                        </div>
                                        <div clas="form-check">
                                          <input class="form-check-input" type="checkbox" name="skill" id="job8" value="Экзобиолог">
                                          <label class="form-check-label" for="job8">
                                            Экзобиолог
                                          </label>
                                        </div>
                                    </div>
                                    
        
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    
                                                                        <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="reasons"></textarea>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group">
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['last_name'])
        print(request.form['first_name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form.getlist('skill'))
        print(request.form['sex'])
        print(request.form['reasons'])
        f = request.files["file"]
        print(f.read())
        print(False if not request.form.get('accept') else True)
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for("static", filename="css/style_hw.css")}">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <p>Эта планета близка к Земле;</p>
                    <div class="alert alert-primary" role="alert" id="n1">
                      На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-primary" role="alert" id="n2">
                      На ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-primary" role="alert" id="n3">
                      На ней есть небольшое магнитное поле;
                    </div>
                    <div class="alert alert-primary" role="alert" id="n5">
                      Наконец, она просто красива!
                    </div>
                  </body>
                </html>'''


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
