import os
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    flowers = os.listdir('/static/flowers')
    flowers.remove('.DS_Store')
    return render_template('index.html',flowers=flowers)
