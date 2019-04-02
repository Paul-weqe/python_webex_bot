from flask import Flask, request

app = Flask(__name__)
bot = None

@app.route("/", methods=['GET', 'POST'])
def index():
    # print(request.get_json())

    json_data = request.get_json()
    
    bot.hears_to_function["hi"]()
    
    
    return "POPO"

