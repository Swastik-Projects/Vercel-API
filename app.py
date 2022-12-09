from data import data
from asyncio import tasks
from flask import Flask, request, jsonify
import requests
import time
import random
import string
import secrets
import json
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)
# MAIN PAGE
teams_collection = db.collection('Teams')
teams_data = teams_collection.document('Team1')
team_data = teams_data.get().to_dict()

events_collection = db.collection('Events')
events_data = events_collection.document('Event1')
event_data = events_data.get().to_dict()

upcoming_collection = db.collection('Upcoming')
upcoming_data = upcoming_collection.document('Features')
upcoming_data = upcoming_data.get().to_dict()

information = [
    {
        "level": 2,
        "name": "Dillusioners",
        "leader": team_data["Leader"],
        "rank": team_data["Rank"],
        "site_level": "Not Protected",
        "experience": "N/A[PROTECTED WITH UILO73]",
        "best": team_data['Best'],
        "wins": team_data['Wins'],
        "ANTI_PRESENT": True,
        "Max": team_data["Max"],
        "tried": team_data['tried'],
        "league": event_data['EventPresent'],
        "members": team_data["Members"],
        "state": team_data['State']
    },
]


@app.route('/')
def superb():
    teams_collection = db.collection('Teams')
    teams_data = teams_collection.document('Team1')
    team_data = teams_data.get().to_dict()

    events_collection = db.collection('Events')
    events_data = events_collection.document('Event1')
    event_data = events_data.get().to_dict()

    upcoming_collection = db.collection('Upcoming')
    upcoming_data = upcoming_collection.document('Features')
    upcoming_data = upcoming_data.get().to_dict()
    information = [
        {
            "level": 2,
            "name": "Dillusioners",
            "leader": team_data["Leader"],
            "rank": team_data["Rank"],
            "site_level": "Not Protected",
            "experience": "N/A[PROTECTED WITH UILO73]",
            "best": team_data['Best'],
            "wins": team_data['Wins'],
            "ANTI_PRESENT": True,
            "Max": team_data["Max"],
            "tried": team_data['tried'],
            "league": event_data['EventPresent'],
            "members": team_data["Members"],
            "state": team_data['State']
        },
    ]
    return jsonify({
        "data": information
    })


@app.route('/index')
def index():
    return jsonify({
        "/": "/",
        "/index": "/index",
        "/league": "/league",
        "/upcoming": "/upcoming",
        "/key": "/key",
        "/user": "/user",
        "/planet": "/planet",
        "/planets": "/planets",
        "/jokes": "/jokes",
        "/memepics": "/memepics",
        "/marketing": "/marketing",
        "/math": "/math",
        "/date": "/date",
        "/year": "/year",
        "/trivia": "/trivia",
        "/endpoint": "/endpoint",  # TODO: ADD MORE STUFF
        "HIDDEN": "MANY HIDDEN STUFF ARE THERE FOR YOU TO EXPLORE",
    })


########################################


@app.route('/league', methods=['GET', 'POST'])
def league_get():
    teams_collection = db.collection('Teams')
    teams_data = teams_collection.document('Team1')
    team_data = teams_data.get().to_dict()
    events_collection = db.collection('Events')
    events_data = events_collection.document('Event1')
    event_data = events_data.get().to_dict()
    upcoming_collection = db.collection('Upcoming')
    upcoming_data = upcoming_collection.document('Features')
    upcoming_data = upcoming_data.get().to_dict()
    league_data = []

    if event_data['EventPresent'] == False:
        league_data = [
            {
                "present": event_data['EventPresent'],
            }
        ]
    else:
        league_data = [
            {
                "present": event_data['EventPresent'],
                event_data['name1']: event_data['Team1'],
                event_data['name2']: event_data['Team2'],
                event_data['name3']: event_data['Team3'],
                event_data['name4']: event_data['Team4'],
                event_data['name5']: event_data['Team5'],
            }
        ]
    return jsonify({
        "data": league_data
    })


########################################


@app.route('/upcoming', methods=['GET', 'POST'])
def upcoming():
    teams_collection = db.collection('Teams')
    teams_data = teams_collection.document('Team1')
    team_data = teams_data.get().to_dict()
    events_collection = db.collection('Events')
    events_data = events_collection.document('Event1')
    event_data = events_data.get().to_dict()
    upcoming_collection = db.collection('Upcoming')
    upcoming_data = upcoming_collection.document('Features')
    upcoming_data = upcoming_data.get().to_dict()
    upcoming_array = [{
        "features": upcoming_data['messages'],
    }]
    return jsonify({
        "data": upcoming_array
    })
########################################
# KEY GEN PAGE


@app.route('/key', methods=['GET', 'POST'])
def key():
    try:
        data = request.json
        data = json.loads(data)
        num = data['length']
        res = ''.join(secrets.choice(string.ascii_letters + string.digits)
                      for x in range(num))
        return jsonify({
            "key": res
        })
    except:
        num = 10
        res = ''.join(secrets.choice(string.ascii_letters + string.digits)
                      for x in range(num))
        return jsonify({
            "key": res
        })
#################################################

# USER GEN PAGE


@app.route('/user', methods=['GET', 'POST'])
def usergive():
    URL = "https://randomuser.me/api"
    response = requests.get(url=URL)
    data = response.json()
    return jsonify({
        "user": data
    })


@app.route('/jokes')
def jokesgive():
    URL = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url=URL)
    data = response.json()
    return jsonify({
        "data": data
    })
    

@app.route('/memepics')
def memepicsgive():
    URL = "https://api.imgflip.com/get_memes"
    response = requests.get(url=URL)
    data = response.json()
    return jsonify({
        "data": data
    })
    

@app.route('/marketing')
def marketing():
    URL = "https://api2.binance.com/api/v3/ticker/24hr"
    response = requests.get(url=URL)
    data = response.json()
    return jsonify({
        "data": data
    })
    
@app.route('/math')
def math():
    URL = "http://numbersapi.com/random/math"
    response = requests.get(url=URL)
    data = response.text
    return jsonify({
        "fact": data
    })
    

@app.route('/date')
def date():
    URL = "http://numbersapi.com/random/date"
    response = requests.get(url=URL)
    data = response.text
    return jsonify({
        "fact": data
    })
    
@app.route('/year')
def year():
    URL = "http://numbersapi.com/random/year"
    response = requests.get(url=URL)
    data = response.text
    return jsonify({
        "fact": data
    })
    
@app.route('/trivia')
def trivia():
    URL = "http://numbersapi.com/random/trivia"
    response = requests.get(url=URL)
    data = response.text
    return jsonify({
        "fact": data
    })

@app.route("/planets")
def planets():
    return jsonify({
        "earth_like_planets": data,
        "message": "SUCCESS"
    }, 200)


@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "SUCCESS"
    }, 200)


@app.route("/endpoint")
def endpoint():
    URL = "https://api.ipify.org/?format=json"
    response = requests.get(url=URL)
    data = response.json()

    temp = "https://api.ipify.org/"
    temper = requests.get(url=temp)
    tempest = temper.text

    URL2 = "https://ipinfo.io/" + tempest + "/geo"
    response2 = requests.get(url=URL2)
    text = response2.text
    data2 = json.loads(text)
    
    country = data2["country"].lower()
    postal = data2["postal"]
    
    URL3 = "https://api.zippopotam.us/" + country + "/" + postal
    response3 = requests.get(url=URL3)
    data3 = response3.json()

    return jsonify({
        "ip_address": data,
        "info": {
            "ip": data2["ip"],
            "city": data2["city"],
            "region": data2["region"],
            "country": data2["country"],
            "loc": data2["loc"],
            "org": data2["org"],
            "postal": data2["postal"],
            "timezone": data2["timezone"],
        },
        "postal_info": data3,
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
