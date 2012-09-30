# imports
import getdata
from flask import Flask, redirect, session, request, url_for, render_template, flash
from foursquare import Foursquare

app = Flask(__name__)
base_url = "http://localhost:5000"

@app.route("/")
def login_page():
    return render_template("login.html")

def makeClient():
    return Foursquare(client_id = "3GZG0BE3SQSWRKGCXXSEJD4FM2TWGXTQOFQUWOKCQ3ZILXEP",
            client_secret = "EXTDHANAPBAR3PDAGJU2DLLZFJPPH1KZYESMY00LXZCVTEBW",
            redirect_uri = base_url + "/auth2")

@app.route("/auth")
def foursquare_connect():
    return redirect(makeClient().oauth.auth_url());

@app.route("/auth2")
def main_page():
    client = makeClient()
    code = request.args.getlist("code")
    access_token = client.oauth.get_token(str(code[0]))
    session['access_token'] = access_token
    return render_template("main_page.html")

# @app.route("/test_session")
# def test():
#     return session['access_token'];

app.debug = True
app.secret_key = "/x85/xfe/x98j/xc8FQb-/x88/xaf/x87/xda/xed/xba/n/x1dk/xbb//0b/xb06/xd2/x87"
if __name__ == "__main__":
    app.run()
