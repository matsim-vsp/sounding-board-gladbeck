import os
from os.path import exists
import sys,tempfile,random,shutil
from datetime import datetime, timedelta

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import sqlite3
import json
from datetime import datetime


# Set up API keys
authfile = 'auth-keys.csv'
valid_api_keys = {}


def setup_auth_keys(authfile):
    print('-- SETTING UP API AUTH KEYS')

    lookup = {}
        # keys from API_KEYS env variable
    if 'API_KEYS' in os.environ:
        env_api_keys = [key.strip() for key in os.environ['API_KEYS'].split(',')]
        for key in env_api_keys:
            split = key.split('-')
            lookup[key] = len(split) > 1 and split[0] or 'user'

    # keys from auth_keys.csv
    try:
        with open(authfile,'r') as keys:
            for line in keys:
                line = line.strip()
                if line.startswith('#'): continue
                items = line.split(',')
                if len(items) >= 2: lookup[items[1]] = items[0]
    except:
        print("\n**\nAuth keyfile not found: ", authfile)

    # No keys? Abort
    if len(lookup.keys()) == 0:
        raise RuntimeError("\n***\nNo valid API keys. Provide keyfile or set API_KEYS env variable.")
        sys.exit(1)

    print("\n*** SoundBoard API SERVER")
    print("*** Valid API users:", ", ".join(lookup.values()), '\n')
    return lookup

valid_api_keys = setup_auth_keys(authfile)

def is_valid_api_key():
    apikey = request.headers.get('Authorization')
    if apikey in valid_api_keys: 
        print("-------VALID KEY---------")
        return True
    return False




# ---------- Set up Database -------------------------



# DB table - votes
# con = sqlite3.connect("test.db")
# cur = con.cursor()
# cur.execute("DROP TABLE votes")
# cur.execute("CREATE TABLE votes(oepnv, kiezbloecke, fahrrad, parkraum, fahrenderAutoVerkehr, drt, ipAddr, cookie, sessionID)")

# ---------- Set up Flask ----------------------------
# Flask API

app = Flask(__name__)
CORS(app, support_credentials=True)

sessionStatus = False
sessionID = 0

valid_api_keys = setup_auth_keys(authfile)

@app.route('/data')
def data():
    if not is_valid_api_key(): return "Invalid API Key", 403
    data = {
        'name': 'Bing',
        'age': 10,
        'hobbies': ['searching', 'chatting', 'learning']
    }
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')

    # Return a JSON response
    return response

@app.route('/sessionOn', methods=["POST"])
def turn_session_on():
    if not is_valid_api_key(): return "Invalid API Key", 403
    data = request.get_data()
    console.log(data)
    return jsonify({"message": "instrcution received successfully"}), 200, {"Access-Control-Allow-Origin": "*"}


@app.route('/votes', methods=["POST"])
def post_vote_to_db():
    if not is_valid_api_key(): return "Invalid API Key", 403
    data = request.get_json()
    db_vote_insert = """INSERT INTO votes (oepnv, kiezBloecke, fahrrad, parkraum, fahrenderAutoVerkehr, drt, ipAddr, cookie, sessionID) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                    
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    
    # if sessionStatus is False:
    #     cur.execute("SELECT MAX(sessionID) FROM votes")
    #     sessionID = cur.fetchone()
    #     print(sessionID)
        
    cur.execute(db_vote_insert, (
    data['oepnv'],
    data['kiezBloecke'],
    data['fahrrad'],
    data['parkraum'],
    data['fahrenderAutoVerkehr'],
    data['drt'],
    data['ipAddr'],
    data['cookie'],
    sessionID
    ))
    
    # table_list = [a for a in cur.execute("SELECT MAX(sessionID) FROM votes ORDER BY ROWID ASC LIMIT 37")]
    # print(table_list) 
    # print(sessionID)

    con.commit()
    con.close()

    return jsonify({"message": "Vote received successfully"}), 200, {"Access-Control-Allow-Origin": "*"}

if __name__ == "__main__":
    app.run(port=4999, debug=True)












