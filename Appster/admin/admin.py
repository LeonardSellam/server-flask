from flask import Blueprint, render_template
from flask import jsonify

admin = Blueprint('admin', __name__)

@admin.route('/api')
def authentication():
    myDict = {'text': 'Hello World'}
    return jsonify(myDict);
