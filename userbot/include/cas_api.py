import json
import datetime
import requests


VERSION = "1.4.0"
CAS_QUERY_URL = "https://api.cas.chat/check?user_id="
DL_DIR = "./csvExports"

def get_user_data(user_id):
    with requests.request('GET', CAS_QUERY_URL + str(user_id)) as userdata_raw:
        userdata = json.loads(userdata_raw.text)
        return userdata

def isbanned(userdata):
    return userdata['ok']

def banchecker(userdata):
    return isbanned(userdata)

def vercheck() -> str:
    return str(VERSION)

def offenses(userdata):
    try:
        offenses = userdata['result']['offenses']
        return str(offenses) 
    except:
        return None
    
def timeadded(userdata):
    try:
        timeEp = userdata['result']['time_added']
        timeHuman = datetime.datetime.utcfromtimestamp(timeEp).strftime('%H:%M:%S, %d-%m-%Y')
        return timeHuman
    except:
        return None
