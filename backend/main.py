
from flask import Flask, request


app = Flask(__name__)


@app.route('/db')
def get_text():
    print("getter: what do I do?")


@app.route('/db', methods=['POST'])
def add_text():
    print("setter: what do I do?")









