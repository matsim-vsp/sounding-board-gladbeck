import os
from os.path import exists
import sys,tempfile,random,shutil
from datetime import datetime, timedelta

from flask import Flask, request, g, jsonify, send_file
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


def convertTuple(tup):
    st = ''.join(map(str, tup))
    return st

# ---------- Set up Database -------------------------

# DB table - votes
con = sqlite3.connect("test.db", check_same_thread=False)
cur = con.cursor()
cur.execute("DROP TABLE votes")
cur.execute("DROP TABLE sessions")
cur.execute("CREATE TABLE votes(oepnv, kiezbloecke, fahrrad, parkraum, fahrenderAutoVerkehr, drt, ipAddr, cookie, sessionID)")
cur.execute("CREATE TABLE sessions(sessionActive, sessionID, startTime, EndTime)")

# ---------- Set up Flask ----------------------------
# Flask API

app = Flask(__name__)
CORS(app, support_credentials=True)

# global sessionStatus
# global sessionID

valid_api_keys = setup_auth_keys(authfile)

@app.route('/sessionOn', methods=["POST"])
def turn_session_on():
    if not is_valid_api_key():
        return "Invalid API Key", 403

    data = request.get_data().decode("utf-8")

    con = sqlite3.connect("test.db", check_same_thread=False)
    cur = con.cursor()

    db_session_insert = "INSERT INTO sessions (sessionActive, sessionID, startTime, endTime) VALUES (?, ?, ?, ?)"
    db_session_end_insert = "UPDATE sessions SET endTime = ? WHERE sessionActive = 1"
    db_session_active_off_insert = "UPDATE sessions SET SessionActive = 0 WHERE sessionActive = 1"

    start_time = ""
    end_time = ""
    session_active = None
    sessionID = None

    c = datetime.now().replace(second=0, microsecond=0)
    current_time = c.strftime("%Y-%m-%d %H:%M:%S")

    if data == "true":
        start_time = current_time
        session_active = 1

        # Get the current maximum sessionID from the table
        cur.execute("SELECT MAX(sessionID) FROM sessions")
        result = cur.fetchone()
        max_sessionID = result[0] if result[0] is not None else 0

        # Calculate the next sessionID
        sessionID = max_sessionID + 1

        cur.execute(db_session_insert, (session_active, sessionID, start_time, end_time))

    elif data == "false":
        end_time = current_time
        cur.execute(db_session_end_insert, (end_time,))
        cur.execute(db_session_active_off_insert)

    # Print the content of the 'sessions' table for debugging purposes
    table_list = [a for a in cur.execute("SELECT * FROM sessions ORDER BY ROWID ASC LIMIT 5")]
    print(table_list)

    con.commit()
    con.close()

    return jsonify({"message": "instruction received successfully"}), 200, {"Access-Control-Allow-Origin": "*"}

@app.route('/votes', methods=["POST"])
def post_vote_to_db():
    # if not is_valid_api_key(): return "Invalid API Key", 403
    data = request.get_json()

    con = sqlite3.connect("test.db", check_same_thread=False)
    cur = con.cursor()

    cur.execute("SELECT sessionID FROM sessions WHERE EXISTS (SELECT sessionID FROM sessions WHERE sessionActive = 1)")
    result = cur.fetchone()
    if (result == None):
        print(" no active session")
        sessionID = 0
    else:
        print("Active session")
        cur.execute("SELECT sessionID FROM sessions WHERE sessionActive = 1")
        sessionID = int(convertTuple(cur.fetchone()))

    check_if_voter_exists = "SELECT * FROM votes WHERE cookie = ? AND  ipAddr = ?"
    cur.execute(check_if_voter_exists, (1, data['ipAddr']))
    voter_exists = cur.fetchone()
    # if (voter_exists != None):
    #     update_vote = """Update votes
    #                 SET oepnv = ?, kiezBloecke = ?, fahrrad = ?,
    #                 parkraum = ?, fahrenderAutoVerkehr = ?, drt= ?, sessionID = ?
    #                 WHERE cookie = ? AND  ipAddr = ?"""
    #     cur.execute(update_vote, (
    #         data['oepnv'],
    #         data['kiezBloecke'],
    #         data['fahrrad'],
    #         data['parkraum'],
    #         data['fahrenderAutoVerkehr'],
    #         data['drt'],
    #         sessionID,
    #         1,
    #         data['ipAddr']))

    #     table_list = [a for a in cur.execute("SELECT * FROM votes ORDER BY ROWID ASC LIMIT 37")]
    #     print(table_list)

    #     con.commit()
    #     con.close()

    #     return jsonify({"message": "Vote received successfully"}), 200, {"Access-Control-Allow-Origin": "*"}

    # else:
    db_vote_insert = """INSERT INTO votes (oepnv, kiezBloecke, fahrrad, parkraum, fahrenderAutoVerkehr, drt, ipAddr, cookie, sessionID)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

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

    table_list = [a for a in cur.execute("SELECT * FROM votes ORDER BY ROWID ASC LIMIT 37")]
    print(table_list)

    con.commit()
    con.close()

    return jsonify({"message": "Vote received successfully"}), 200, {"Access-Control-Allow-Origin": "*"}

@app.route('/getVotes/<session_id>', methods=["GET"])
def get_votes_from_db(session_id):
    if not is_valid_api_key(): return "Invalid API Key", 403

    con = sqlite3.connect("test.db", check_same_thread=False)
    cur = con.cursor()
    cur.execute("SELECT * FROM votes WHERE sessionID = " + session_id)
    results = cur.fetchall()
    votes = [{'oepnv': row[0], 'kiezBloecke': row[1], 'fahrrad': row[2], 'parkraum': row[3], 'fahrenderAutoVerkehr': row[4], 'drt': row[5], 'ipAddr': row[6], 'cookie': row[7], 'session_id': row[8]} for row in results]
    print(votes)

    return json.dumps(votes)

@app.route('/getLastSession/', methods=["GET"])
def get_last_session():
    if not is_valid_api_key(): return "Invalid API Key", 403

    con = sqlite3.connect("test.db", check_same_thread=False)
    cur = con.cursor()
    cur.execute("SELECT MAX(sessionID) FROM sessions")
    result = convertTuple(cur.fetchone())
    if (result == "None"):
        return "0"
    else:
        return result

if __name__ == "__main__":
    app.run(port=4999, debug=True)
