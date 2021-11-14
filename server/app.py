from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import Flask, make_response, request, current_app
from flask_cors import CORS


app = Flask(__name__);
CORS(app);

@app.route('/', methods=['GET', 'POST'])
def index():
   
    if request.method == 'POST':
        return jsonify({'chicken': 'dinner'});
    elif request.method == 'GET':
        return jsonify({'chicken': 'ok'});
    else:
        return jsonify({'status': 'error'});

       