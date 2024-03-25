from flask import Flask
import requests as r

app = Flask(__name__)

@app.route("/<path:b>")
def aa(b):
    x = r.get("https://prod-ec-eu-central-1.video.pscp.tv/"+b)
    h = {"Content-Type":x.headers["Content-Type"],"Access-Control-Allow-Origin":"*"}
    return x.content,200,h

app.run(host="0.0.0.0")
