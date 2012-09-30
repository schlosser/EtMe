# imports
import sqlite3
from flask import Flask, redirect, url_for, render_template, flash
from foursquare import Foursquare

app = Flask(__name__)
base_url = "http://localhost:5000"

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/auth")
def foursquare_connect():
    # oauth
    client = Foursquare(client_id = "3GZG0BE3SQSWRKGCXXSEJD4FM2TWGXTQOFQUWOKCQ3ZILXEP",
            client_secret = "EXTDHANAPBAR3PDAGJU2DLLZFJPPH1KZYESMY00LXZCVTEBW",
            redirect_uri = base_url + "/auth2")
    auth_uri = client.oauth.auth_url()
    return redirect(auth_uri);

@app.route("/auth2")
def main_page():
    return render_template("main_page.html")

app.debug = True
if __name__ == "__main__":
    app.run()
