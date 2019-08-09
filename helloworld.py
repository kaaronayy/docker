from flask import Flask, Response
import time
# from flask_cors import CORS
# import JSON

app = Flask(__name__)
 
@app.route("/test")
def hello():
    return "Hello World!"

@app.route("/time")
def webtime():
    def eventStream():
        while True:
            yield currentTime() + '\n'
    return Response(eventStream(), status=200, mimetype="text/event-stream")
 
def currentTime():
    time.sleep(1.0)
    tt = time.ctime(time.time())
    return tt

if __name__ == "__main__":
    app.run(debug=True)

def bootapp():
    app.run(port=8080, threaded=True, host=('0.0.0.0'))

if __name__ == '__main__':
     bootapp()