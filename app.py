import os
from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
from util.index import main
from util import consts

UPLOAD_FOLDER = './util'
ALLOWED_EXTENSIONS = {'md'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = consts.MEMORY_LIMIT


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/home')
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', rows=consts.ROWS)


@app.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == 'GET':
        return redirect(url_for('index'))
    path = f'{consts.PATH}/test.md'
    data = request.form['text']
    with open(path, 'w') as file:
        file.write(data)
    main(consts.PATH)
    with open(path, 'r') as file:
        result = file.read()
    os.remove(path)
    return render_template('index.html', rows=consts.ROWS, input=data, result=result)


@app.route('/file', methods=['GET', 'POST'])
def file():
    if request.method == 'GET':
        return redirect(url_for('index'))
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = f'{consts.PATH}/{filename}'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with open(path, 'r') as file:
            data = file.read()
        main(consts.PATH)
        with open(path, 'r') as file:
            result = file.read()
        os.remove(path)
        return render_template('index.html', rows=consts.ROWS, input=data, result=result)


if __name__ == "__main__":
    app.run()
