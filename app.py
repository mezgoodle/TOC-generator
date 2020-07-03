from flask import Flask, render_template, request, redirect, url_for
from util.index import main
from util import consts

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'md'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/home')
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', rows=consts.ROWS)

@app.route('/text', methods=['POST'])
def text():
    data = request.form['text']
    with open(f'{consts.PATH}/test.md', 'w') as file:
        file.write(data)
    main(consts.PATH)
    with open(f'{consts.PATH}/test.md', 'r') as file:
        result = file.read()
    return render_template('index.html', rows=consts.ROWS, input=data, result=result)
    

if __name__ == "__main__":
    app.run(debug=True)
