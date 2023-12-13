from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add_page():
    '''adds and returns two passed parameters'''
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a,b)
    return str(result)

@app.route('/sub')
def sub_page():
    '''subracts two passed in parameters'''
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def mult_page():
    '''multiplies two passed in parameters'''
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = mult(a,b)
    return str(result)

@app.route('/div')
def div_page():
    '''divides two passed in parameters'''
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a,b)
    return str(result)

