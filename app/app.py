from flask import Flask, request, render_template
from .processors import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Home', ServiceName='Сделаем это!')


@app.route('/team')
def team():
    return render_template('team.html', title='Считалка слов', ServiceName='Считалка слов')


@app.route('/keyword/generator')
def generator():
    return render_template('/keyword/generator.html', title='Генератор фраз', ServiceName='Генератор фраз')


@app.route('/keyword/generator/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceGenerator():
    words = generator(request.form["words"])
    return render_template('/keyword/generator.html', title='Генератор фраз', ServiceName='Генератор фраз',
                           result=words)


@app.route('/keyword/crossminus', methods=['GET', 'POST'])
def crossminus():
    return render_template('/keyword/crossminus.html', title='Кросс-минусовка фраз', ServiceName='Кросс-минусовка фраз')


@app.route('/keyword/crossminus/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceCrossminus():
    words = CrossMinus(request.form["words"])

    return render_template('/keyword/crossminus.html', title='Кросс-минусовка фраз', ServiceName='Кросс-минусовка фраз',
                           result=words)


@app.route('/keyword/inclinator')
def inclinator():
    return render_template('/keyword/inclinator.html', title='Склонятор', ServiceName='Склонение ключевых слов')


@app.route('/keyword/inclinator/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceInclinator():
    words = (modifier(request.form["words"], 'all'))

    return render_template('/keyword/inclinator.html', title='Склонятор', ServiceName='Склонение ключевых слов',
                           result=words)

@app.route('/keyword/lemmatizer')
def lemmatizer():

    return render_template('/keyword/lemmatizer.html', title='Лемматизатор', ServiceName='Лемматизатор')


@app.route('/keyword/lemmatizer/submit', methods=['GET', 'POST'])  # принимает текст
def inclinatorLemmatizer():
    words = lemma(modifier(request.form["words"], 'all'))

    return render_template('/keyword/lemmatizer.html', title='Лемматизатор', ServiceName='Лемматизатор', result=words)


@app.route('/keyword/synonymizer')
def synonymizer():
    return render_template('/keyword/synonymizer.html', title='Синонимайзер', ServiceName='Синонимайзер')


@app.route('/keyword/synonymizer/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceSynonymizer():
    words = synonym(request.form["words"])

    return render_template('/keyword/synonymizer.html', title='Синонимайзер', ServiceName='Синонимайзер', result=words)


@app.route('/keyword/wordcount')
def wordcount():
    return render_template('/keyword/wordcount.html', title='Считалка слов', ServiceName='Считалка слов')


@app.route('/keyword/wordcount/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceWordcount():
    words = counter(modifier(request.form["words"], 'allpass'))

    return render_template('/keyword/wordcount.html', title='Считалка слов', ServiceName='Считалка слов', result=words)


@app.route('/keyword/trimutm')
def TrimUtm():
    return render_template('/keyword/trimutm.html', title='Удаление UTM меток', ServiceName='Удаление UTM меток')


@app.route('/keyword/trimutm/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceTrimUtm():
    words = trim_utm(request.form["words"])

    return render_template('/keyword/trimutm.html', title='Удаление UTM меток', ServiceName='Удаление UTM меток',
                           result='\n'.join(words))


@app.route('/keyword/cityremover')
def CityRemover():
    return render_template('/keyword/cityremover.html', title='Удаление городов', ServiceName='Удаление городов')


@app.route('/keyword/cityremover/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceCityRemover():
    words = cityremover(modifier(request.form["words"], 'all'))

    return render_template('/keyword/cityremover.html', title='Удаление городов', ServiceName='Удаление городов',
                           result=words)