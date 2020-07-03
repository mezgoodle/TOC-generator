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
    data = request.form['text']
    with open(f'{consts.PATH}/test.md', 'w') as file:
        file.write(data)
    main(consts.PATH)
    with open(f'{consts.PATH}/test.md', 'r') as file:
        result = file.read()
    return render_template('index.html', rows=consts.ROWS, input=data, result=result)


@app.route('/file', methods=['GET','POST'])
def file():
    if request.method == 'GET':
        return redirect(url_for('index'))
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'All good'


if __name__ == "__main__":
    app.run(debug=True)
