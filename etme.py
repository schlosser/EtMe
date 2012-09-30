# imports
from init import makeClient
import getdata
import getproducts
from flask import Flask, redirect, session, request, url_for, render_template, flash
from foursquare import Foursquare

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/auth")
def foursquare_connect():
    return redirect(makeClient().oauth.auth_url());

@app.route("/auth2")
def main_page():
    client = makeClient()
    code = request.args.getlist("code")
    access_token = client.oauth.get_token(str(code[0]))
    session['access_token'] = access_token
    products = getproducts.getProducts(getdata.getData())
    return render_template("main_page.html")

app.debug = True
app.secret_key = "/x85/xfe/x98j/xc8FQb-/x88/xaf/x87/xda/xed/xba/n/x1dk/xbb//0b/xb06/xd2/x87"
if __name__ == "__main__":
    app.run()
