from flask import Flask
from flask import abort, jsonify, request as f_request

import sys, requests, json, pprint, datetime

app = Flask(__name__)

ZTM_LINE_RESOURCE = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/22313c56-5acf-41c7-a5fd-dc5dc72b3851/download/routes.json"
ZTM_DELAY_RESOURCE = "http://ckan2.multimediagdansk.pl/delays?stopId="


@app.route("/")
def description():
    return (
        "API endpoints:<br>"
        "/disp?id=stopId&dw=16&dh=2<br>"
        "/json?id=stopId&dh=2<br>"
        "/json?id=stopId"
    )


# this endpoint returns very simplified JSON with only 3 datafields:
# ['busNum'] - containing bus number (199, N12)
# ['direction'] - containing text data with the bus' front headsign
# ['eta'] - estimated time of arrival on the stop. The API provider
#   promises that the vehicle should arrive between 1m. earlier and
#   3m. late.
# if ?dh=<n> parameter is provided, number of entries is reduced to <n>.
@app.route("/json")
def apiSimpleJson():
    if f_request.args.get("id") is None:
        abort(400)
    return jsonify(getTruncatedJson(f_request.args.get("id"), f_request.args.get("dh")))


# This API is dedicated for devices uncapable of handling JSON parsing
# It formats returned data so it can fit in WxH alphanumerical LCD,
# like standard hd44780 display.


@app.route("/disp")
def apiDisplay():
    if f_request.args.get("id") is None:
        abort(400)
    return getStopDataString(
        f_request.args.get("id"), f_request.args.get("dw"), f_request.args.get("dh")
    )


def getStopDataJson(stopId: int):

    try:
        stopData = requests.get(ZTM_DELAY_RESOURCE + str(stopId))

        stopJSON = json.loads(stopData.content)["delay"]
    except json.decoder.JSONDecodeError:
        abort(400)

    # todo - This file is rather large and updates only once a day - some kind
    # of caching would be quite beneficial
    linesData = requests.get(ZTM_LINES_RESOUCE)

    # The returned JSON must be querried with today's date.
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    linesJSON = json.loads(linesData.content)[today]["routes"]

    returnList = []
    for d in stopJSON:
        stopRow = {}
        stopRow["busNum"] = [
            l["routeShortName"] for l in linesJSON if l["routeId"] == d["routeId"]
        ][0]
        stopRow["direction"] = d["headsign"]
        stopRow["eta"] = d["estimatedTime"]
        returnList.append(stopRow)
    return returnList


def getTruncatedJson(stopId: int, rowNum: int = None):
    try:
        if rowNum is not None:
            return getStopDataJson(stopId)[0 : int(rowNum)]
        else:
            return getStopDataJson(stopId)
    except ValueError:
        return getStopDataJson(stopId)


def getStopDataString(stopId: int, colNum: int = 16, rowNum: int = 2):
    dataList = getTruncatedJson(stopId, rowNum)
    returnString = ""
    for l in dataList:
        returnString += l["busNum"] + " " + l["direction"] + " " + l["eta"] + "\n"
    return returnString
