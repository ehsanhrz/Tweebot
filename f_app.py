from flask import Flask,request,jsonify
from threading import Thread
import sch

app = Flask(__name__)
# th = Thread(__name__)
main = "1362243124@#$76"
command = "run"
run_sch = False
# async def execute():
#     sch.algho()
@app.post('/')
def run():
    data = request.get_json()
    passwords = data['password']
    script = data['script']
    if not script:
        response = {'error':'Please give the script'}
        return jsonify(response)
    if not passwords:
        response = {'error':'Please give the password'}
        return jsonify(response)
    if passwords != main:
        response = {'error':'invalid passwords'}
        return jsonify(response)
    if script != command:
        response = {'error':'invalid script'}
        return jsonify(response)
    if passwords == main and script == command:
        # response = {'tweebot':'im running the command'}
        sch.algho()
        # Thread(target = sch.algho()).start()
        # return jsonify(response)
    else:
        response = {'error':'something went wrong'}


if __name__ == '__main__':
    app.run()