from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, jsonify, abort
import json
# call other modules

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


# for test
@app.route('/')
def index():
    return 'Hello World!'


# 貨物数取得(ETD)
@app.route('/v1/shipments-etd/<string:type>', methods=['GET'])
def get_number_of_shipments_etd(type):
    json_open = open('fwd_api_sample_number_of_shipments.json', 'r')
    json_obj = json.load(json_open)
    if type == 'region':
        response = jsonify(json_obj['region_daily'])
    else:
        response = 'nodata'
    return response


# return json
# 異常貨物取得
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


# return json
# 貨物情報取得
@app.route('/v1/references/<string:hawb>', methods=['GET'])
def get_shipments(hawb):
    json_open = open('fwd_api_sample_shipments.json', 'r')
    json_obj = json.load(json_open)
    for i in range(2):
        if json_obj['shipments'][i]['HAWB'] == hawb:
            response = jsonify(json_obj['shipments'][i])
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