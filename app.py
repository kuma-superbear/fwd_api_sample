from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, jsonify, abort
import json

# call other modules

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# for test
@app.route('/')
def index():
    return 'Hello World!'


# return json
@app.route('/v1/exceptions/<string:hawb>', methods=['GET'])
def get_exceptions(hawb):
    json_open = open('fwd_api_sample_exception.json', 'r')
    json_obj = json.load(json_open)
    for i in range(3):
        if json_obj['shipments_exceptions'][i]['HAWB'] == hawb:
            response = jsonify(json_obj['shipments_exceptions'][i])
            break
        else:
            response = 'nodata'
    return response


# add json
@app.route('/v1/exceptions/<test_data>/add', methods=['GET', 'POST'])
def post_exceptions(test_data):
    return test_data


# main
if __name__ == '__main__':
  app.run(debug = True)