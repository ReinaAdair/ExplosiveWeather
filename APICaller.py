import json
import requests

##### Prebuilt API call that requires no input from the program/user
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


##### API call that substitutes API variables with user/program input
def API_Call(loc, un):
    location = loc
    apikey = "9xi9ZXm6xNUKDVQDS6DQKsiwtuJMJb61"
    units = un
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

API_Call("47421", "imperial")
#Prebuilt_API_Call()

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