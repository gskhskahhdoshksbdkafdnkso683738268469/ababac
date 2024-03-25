from flask import Flask
import requests as r

app = Flask(__name__)

@app.route("/<path:b>")
def aa(b):
    x = r.get("http://51.159.98.123:80/"+b)
    h = {"Content-Type":x.headers["Content-Type"],"Access-Control-Allow-Origin":"*"}
    return x.content,200,h

@app.route("/ab")
def bb():
    x = r.get("http://51.159.98.123:80/live/415663775/826262627/109987.ts?token=GhMNBEZcR1gRUARbB18BBAIOVlVYVQsHVlZUAFBeBlUEVVUGBFVXVANEGBoXEhZRBVtrXgVGAgFSXw4MBBQUFhJUFzpcUEdYEVADC1xQUhZIFEBeDAEaClNRBgUADgZWVAFJR0VdAUAJRAwIU1ZGGEZTTEMEFlZRDjlTUUVRVQZDCwsQWVhJQFwIa1wBCwVaABQOFVBGFBILFUcWCVZDDw0dRwdcQBcDRwMWAkZXUwxXFBgVAgtNXhYUThYJGnQnQx1HAE1AAAxAD1tWRlxGQBcUGBUIF2dCBxVDRlZZWwYTE19HBRZJQF4HTGcHCQpaAVVAXg4KSxJYRAYWHxpbDA9YEQpHaxULV0QOGlxWUgJGSw==")
    h = {"Content-Type":x.headers["Content-Type"],"Access-Control-Allow-Origin":"*"}
    return x.content,200,h

app.run(host="0.0.0.0")
