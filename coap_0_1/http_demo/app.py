'''
Author: geekli
Date: 2021-01-25 11:07:59
LastEditTime: 2021-01-25 11:07:59
LastEditors: your name
Description: 
FilePath: /coap_0_1/http_demo/app.py
'''
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route('/value', methods=['POST'])
def cal_value():
  if request.method == 'POST':
    a = request.form.get('a', 0, type=int)
    b = request.form.get('b', 0, type=int)
    return jsonify(result = a + b)
    
if __name__=="__main__":
    app.run(host = '0.0.0.0',port = 8080, debug = True)
