from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file

from flask import render_template


app = Flask(__name__)

from flask_cors import CORS
CORS(app)

@app.route('/')
def my_page():
    print("building my page")
    #return jsonify({'text': 'get_text()'})

    #return send_file('../templates/my-page.html')
    return send_file('../frontend2/public/index.html')

    #return 'welcome'


@app.route('/', methods=['POST'])
def add_text():
    print("Setter: got stuff by POST!")
    #return jsonify({'text': 'add_text()'})

    text =request.form['text']
    #pr_text = text.upper()

    return text


@app.route("/synthesize_data", methods=['GET', 'POST'])
def datasynthesize():
    data = request.get_json()
    if data:
        print ("Calling synthesizer for ", data['name'], " rows.")
        main(int(data['name']))
    return "TEST"


if __name__ == '__main__':

    app.debug = True
    app.run(port=5000)




