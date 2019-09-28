from flask import Flask
import sys
import requests

app = Flask(__name__)
# Port forwarding will be working for different localhost ports
URL = 'http://127.0.0.1'


#GET requests
@app.route('/<int:port>/')
def change_port_root(port):
    resp = requests.get(url = URL+':'+str(port)+'/')
    return resp.content

@app.route('/<int:port>/<path:way>')
def change_port(port,way):
    resp = requests.get(url = URL+':'+str(port)+'/'+way)
    return resp.content

app.run(host='0.0.0.0',port=5050,debug=False)
