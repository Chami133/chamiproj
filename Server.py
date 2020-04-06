from symbol import parameters
from Corona import *
import requests
import json

def iost(countryTotal):
    parameters = {'countryTotal': countryTotal}
    response = requests.get("https://api.thevirustracker.com/free-api",params=parameters)
    print(response.status_code)

    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    pass_times = response.json()['countrydata']
    jprint(pass_times)

iost(countryTotal = Name)

