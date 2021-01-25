import glob
import os
from flask import send_file, Flask, render_template

app = Flask(__name__, template_folder='./templates')
files = glob.glob("images/*.jpg")


@app.route('/')
def index():
    code_list = [i[7:10] for i in files]
    code_list.sort()
    return render_template('index.html', code_list=code_list, b_count=len(code_list))


@app.route('/a')
def a():
    return 'Hi! Im on Heroku'


@app.route('/<status>')
def get_image(status):
    file_name = f'images/{status}.jpg'
    # file_name = f'images\\{status}.jpg'
    if file_name in files:
        return send_file(file_name, mimetype='image/jpeg')
    else:
        return send_file('images/404.jpg', mimetype='image/jpeg')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(port=port, debug=True)
