from flask import Flask, request
from flask import jsonify
from lib.commute import commute_search


app = Flask(__name__)
app.debug = True

# @required: subway_stop, time
@app.route("/")
def nearby():
  if("subway_stop" in request.args and "time" in request.args):
    subway_stop=request.args["subway_stop"]
    time=request.args["time"]
    ret = commute_search(subway_stop,time)
  else:
    ret = dict()
  return jsonify(ret)



if __name__ == "__main__":
  app.run()