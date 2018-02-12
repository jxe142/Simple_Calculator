from flask import Flask, render_template

application = Flask(__name__)
application.debug = True
application.secret_key = 'cC1YCsdOjQQWEGgWsApgNEo2'


@application.route("/", methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


if __name__ == "__main__":
    application.run()
