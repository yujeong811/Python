import jwt
import requests
import json
from time import time
  
  
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app)

@app.route('/')
def zoom():
    return render_template('zoom_test.html')

    
# Enter your API key and your API secret
API_KEY = 'os92P7NyT86_Rk9ihtPHeg'
API_SEC = 'RTWHkNFiJRxwXMkX29YvsGUD0mndoY5lW3J9'
  
# create a function to generate a token
# using the pyjwt library


  
def generateToken():
    token = jwt.encode(
        # Create a payload of the token containing
        # API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},
  
        # Secret used to generate token signature
        API_SEC,
  
        # Specify the hashing alg
        algorithm='HS256'
    )
    return token
  
  
# create json data for post requests
meetingdetails = {"topic": "python zoom meeting",
                  "type": 2,
                  "start_time": "2019-06-14T10: 21: 57",
                  "duration": "45",
                  "timezone": "Europe/Madrid",
                  "agenda": "test",
  
                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }
  
# send a request with headers including
# a token and meeting details
  
@app.route('/createZoom', methods = ['GET'])
def createMeeting():
    headers = {'authorization': 'Bearer ' + generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))
  
    print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]
  
    print(
        f'\n here is your zoom meeting link {join_URL} and your \
        password: "{meetingPassword}"\n')
    
    return y
  
# run the create meeting function
#createMeeting()


if __name__ == '__main__':
    socket_io.run(app, port=9999)