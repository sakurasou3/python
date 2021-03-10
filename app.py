from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/hello')
def hello():
    return '<h1>こんにちは</h1>'

@app.route('/hello/<string:name1>/<string:name2>')
def hello_name(name1, name2):
    return '<h1>こんにちは{}さん{}さん</h1>'.format(name1, name2)

@app.route('/add/<int:num1>/<int:num2>')
def hello_add(num1, num2):
    return '<p>{} + {} = {}</p>'.format(num1, num2, num1 + num2)

@app.route('/div/<float:num1>/<float:num2>')
def hello_div(num1, num2):
    return '<p>{} / {} = {}</p>'.format(num1, num2, num1 // num2)   # 小数点以下切り捨て

if __name__ == '__main__':
    app.run(debug=True)
