from flask import Flask, render_template

application = Flask(__name__)
app = application
app.debug = True
app.secret_key = 'cC1YCsdOjQQWEGgWsApgNEo2'


@app.route("/", methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
