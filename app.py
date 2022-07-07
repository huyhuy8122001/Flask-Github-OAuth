from lib2to3.pgen2 import token
from flask import Blueprint, Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = 'my_secret_key'

blueprint = make_github_blueprint(client_id='454e4bd6363b54e3f8a6', client_secret='decec8007aa38e4acd55b0c61b714a81f0079e1e')

app.register_blueprint(blueprint, url_prefix='/github_login')

@app.route('/')
def login_github():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return account_info_json
@app.route('/token')
def token():
    token = blueprint.token
    return token
if __name__ == "__main__":
    app.run(debug=True, port=5050)