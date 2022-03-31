from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return """<meta http-equiv="refresh" content="1" /> 
        <br>The current time is 
        {}</br>""".format(datetime.strftime(datetime.now(), "%d %B %Y %X"))

if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=5000)

