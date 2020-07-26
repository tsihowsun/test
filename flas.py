from flask import *
# from main import app
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"
    #return send_file('media.mp4')

app.run(host='0.0.0.0',port=80)
