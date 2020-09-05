# app.py
from flask import Flask, request, jsonify
import random
import excuseggen
from excuses import ExcuseSituation
from textgen import TextGenerator

app = Flask(__name__)

@app.route('/getx/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    response = {}

    # Check if user sent a name at all
    if False:#not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif False: #str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        excuseStr= excuseggen.makeExcuse()
        response["MESSAGE"] = excuseStr

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": "Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

@app.route('/excuse/gen')
def excuse():
    def show_word(w):
        print('>', w)
    model_size = 'gpt2'
    gen = TextGenerator(model_size)
    s = ExcuseSituation(gen, assignment=random.choice(excuseggen.perpetrator) +" "+random.choice(excuseggen.delay), tasks=[
        # 'plan the menu',
        # 'go to the grocery store to buy the ingredients',
        # 'cook it up',
        # 'plate the meal in an attractive way',
    ], word_callback=show_word)
    excuses = s.generate_excuses(count=1)
    result =  {
        'excuses' : excuses
    }
    return result
# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(host='0.0.0.0', port=80)



# print a random excuse
