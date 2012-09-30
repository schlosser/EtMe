# imports
import getdata
from flask import Flask, redirect, request, url_for, render_template, flash
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
    access_token = client.oauth.get_token(request.args.getlist("code"))
    session['access_token'] = access_token
    return render_template("main_page.html")

app.debug = True
if __name__ == "__main__":
    app.run()
