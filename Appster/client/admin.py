from flask import Blueprint, render_template
from flask import jsonify
from flask import request
from Appster.models.users import User
from flask import Response

admin = Blueprint('admin', __name__)

@admin.route('/api', methods=['GET', 'POST'])
def authentication():
    if request.method == 'GET':
        myDict = {'text': 'Hello World'}
        return jsonify(myDict);
    else:
        name = request.form['username']
        test = User.finOneByName(name)
        myDict = { 'name': test.name, "login" :  test.email }
        return jsonify(myDict);



"""
Account creation on POST method
param1(String): name
param2(String): email
"""
@admin.route('/create', methods=['POST'])
def create_account():
    data = User.createNewUser(request.form['name'], request.form['email'])
    resp = jsonify(data)
    resp.status_code = 200
    return resp
