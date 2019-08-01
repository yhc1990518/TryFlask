from flask import Flask, request
from pyon import PyonObject
import orjson


import TestJsonOBJ

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


'''
测试json
'''
@app.route('/testjson', methods=['POST'])
def testjson():
    jsValue = request.get_json()
    jsValue["id"] = 2
    jsValue["name"] = "修改了"
    return orjson.dumps(jsValue)





if __name__ == '__main__':
    app.run()
