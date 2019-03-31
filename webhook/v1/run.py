from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.get_json())
    print(request)
    return "POPO"

