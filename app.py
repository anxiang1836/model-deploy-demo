import os
import sys
import logging
from flask import Flask, request, render_template
from flask_cors import CORS

from serve import get_model_api

# define the app
app = Flask(__name__, static_url_path='')
CORS(app)  # needed for cross-domain requests, allow everything by default

# logging for heroku
if 'DYNO' in os.environ:
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.INFO)

# load the model
model_api = get_model_api()


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        my_prediction = model_api(message)
        return render_template('result.html', prediction=my_prediction)


@app.route('/')
def index():
    return render_template("home.html")


# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404


@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally.
    # app.run(host='0.0.0.0', debug=True)
    app.run()

