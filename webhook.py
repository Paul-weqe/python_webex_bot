from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    return "Cool"


@app.route("/messages", methods=["POST"])
def messages():
    data = request.get_json()
    print(data)
    return "Message"
    

if __name__ == "__main__":
    app.run(debug=True)




