from flask import Flask, request, jsonify
from functools import wraps


app = Flask(__name__)


def oauth2_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # This should be replaced with real OAuth2 token validation
        if not 'Authorization' in request.headers:
            return jsonify({"message": "Authorization header missing"}), 403
        return f(*args, **kwargs)
    return decorated_function


@app.route('/api1/')
@oauth2_required
def hello_world():
    return 'Hello, World!'


@app.route('/api2/')
def api_no_auth():
    return 'This is API2!'




if __name__ == '__main__':
    app.run()

