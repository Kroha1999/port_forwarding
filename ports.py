from flask import Flask, render_template, redirect, url_for
from builtins import ConnectionRefusedError
import sys
import werkzeug
import requests

app = Flask(__name__)
# Port forwarding will be working for different localhost ports'
PORT = 5050       #port forwarding application port
DEFAULT_PORT = 80 #default port which will be represented by default 
HOST = "127.0.0.1"
URL = 'http://'+HOST

#GET requests
@app.route('/', defaults={'port':DEFAULT_PORT,'way': ''})
@app.route('/<int:port>/', defaults={'way': ''})
@app.route('/<int:port>/<path:way>')
def change_port(port,way):
    if port == PORT:
        return "THIS IS PORTFORWARDING APP"

    resp = requests.get(url = URL+':'+str(port)+'/'+way)
    result = handle_resp(resp)
    return result

#ERROR codes handler for received requestes
def handle_resp(resp):
    code = resp.status_code
    print(code, file=sys.stderr)
    if code == 200:
        return resp.content
    elif code == 404:
        return render_template("error404.html")
    elif code == 500:
        return render_template("error500.html")
    else:
        return resp.content

#ERROR handlers for port forwarding app
@app.errorhandler(ConnectionRefusedError)
def handle_connection(e):
    return render_template("error500.html")

@app.errorhandler(requests.exceptions.ConnectionError)
def handle_connection(e):
    return render_template("error500.html")

app.errorhandler(werkzeug.exceptions.NotFound)
def handle_not_found(e):
    return render_template("error404.html")


app.run(host=HOST,port=PORT,debug=False)

