# module import
import requests
import json

def pprand():
  from random import random
  return int(random()*1000%6)

def wCondition(c):
  okayFli = {'Sunny':0,'Clear':0,'Partly cloudy':0,'Cloudy':0,'Patchy rain possible':0,'Patchy light drizzle':0,'Light rain shower':0,'Light drizzle':0}
  delayFli = {'Overcast':30,'Fog':40,'Patchy light rain with thunder':60,'Blowing snow':70,'Patchy snow possible':10,'Patchy light snow':10,'Moderate rain':50}
  cancelFli = {'Heavy rain':40,'Heavy snow':60,'Thundery outbreaks possible':40,'Moderate or heavy rain shower':30,'Moderate or heavy rain with thunder':50}
  if c in okayFli.keys():
    return  okayFli[c], 'delay'
  elif c in delayFli.keys():
    return delayFli[c], 'delay'
  elif c in cancelFli.keys():
    return cancelFli[c], 'cancel'
  else:
    return 0,'delay'


def getweather(inputOrigin, inputDate):
    url = "https://api.m3o.com/v1/weather/Weather/Forecast"
    # inputOrigin = "DFW" # input
    # inputDate = '2021-11-17' # input

    payload = json.dumps({
        "days": "10",
        "location": inputOrigin
        })
    headers = {
        'Micro-Namespace': 'micro',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer NjJjMGRjNmEtN2JjYS00MWEzLTk4NjEtMTlkOTg2MmUyZGRk'
        }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    for i in range(len(response['forecast'])):
        if response['forecast'][i]['date'] == inputDate:
            temp = response['forecast'][i]['condition']
            prob, status = wCondition(temp)
            prob += pprand()
            print(inputOrigin,'date',response['forecast'][i]['date'],end=' ')
            print(prob,"%",status)
            return prob, status






