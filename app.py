from flask import Flask, current_app


app = Flask(__name__)


@app.route('/')
@app.route('/view1')
@app.route('/view2')
@app.route('/view3')
def index():
    return current_app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=False)