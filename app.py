from flask import send_file, Flask
import glob

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home of HTTP Status Birbs. Add /status_code to access.'


@app.route('/<status>')
def get_image(status):
    files = glob.glob("images/*.jpg")
    file_name = f'images\\{status}.jpg'
    if file_name in files:
        return send_file(file_name, mimetype='image/jpeg')
    else:
        return send_file('images/404.jpg', mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
