import json
import requests
#import PySimpleGUI as sg

def Prebuilt_API_Call():
    location = "indianapolis"
    apikey = "9xi9ZXm6xNUKDVQDS6DQKsiwtuJMJb61"
    units = "imperial"
    calltype = "realtime"

    #URL used for calling the API
    url = f'https://api.tomorrow.io/v4/weather/{calltype}?location={location}&units={units}&apikey={apikey}'

    #Headers used for calling the API
    headers = {"accept": "application/json"}

    #Assigining API response to variable
    response = requests.get(url, headers=headers)

    r = json.loads(response.text)

    try:
        for val in r["data"]["values"]:
            print(val, ": ", r["data"]["values"][val])
    except:
        print("An error has occured parsing the JSON")
        print(r)
        return "error"

    for val in r["data"]["values"]:
        if val == "humidity":
            humidity = r["data"]["values"][val]
        elif val == "precipitationProbability":
            precipitationProbability = r["data"]["values"][val]
        elif val == "pressureSurfaceLevel":
            pressureSurfaceLevel = r["data"]["values"][val]
        elif val == "temperature":
            temperature = r["data"]["values"][val]
        elif val == "temperatureApparent":
            temperatureApparent = r["data"]["values"][val]
        elif val == "weatherCode":
            weatherCode = r["data"]["values"][val]
        elif val == "windSpeed":
            windSpeed = r["data"]["values"][val]

    return humidity, precipitationProbability, pressureSurfaceLevel, temperature, temperatureApparent, weatherCode, windSpeed

def API_Call(location, units, calltype):
    pass

Prebuilt_API_Call()

"""Add a try catch for the API call in case of exceeding call limit"""

"""
values returned in json format from the API

data:{
    time:
    values:{
        cloudBase:
        cloudCeiling:
        cloudCover:
        dewPoint:
        freezingRainIntensity:
        humidity: ###
        precipitationProbability: ###
        pressureSurfaceLevl: ###
        rainIntensity:
        sleetIntensity:
        snowIntensity:
        temperature: ###
        temeratureApparent: ###
        uvHealthConcern:
        uvIndex:
        visibility:
        weatherCode:
        windDirection:
        windGust:
        windSpeed: ###
    }
    location:{
        lat:
        lon:
        name:1,2,3,4
        type:
    }
}
"""