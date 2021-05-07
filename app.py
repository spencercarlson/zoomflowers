import os
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    flowers = os.listdir('static/flowers')
    flowers.sort()
    # flowers.remove('.DS_Store')
    # ^ this line is only needed on the Mac OS - if you include when you deploy to Netlify it will break things :) 
    return render_template('index.html',flowers=flowers)
