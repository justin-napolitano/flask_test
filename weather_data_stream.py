import requests, json
from pprint import pprint
from pandas import json_normalize
from flatten_json import flatten_json
from datetime import datetime
import os
import time
from ratelimit import limits, RateLimitException, sleep_and_retry
from concurrent.futures import ThreadPoolExecutor as PoolExecutor

def get_key(key_path):
    with open(key_path, "r") as f:
        key = f.read()
        key = key.rstrip('\n')
        pprint(key)
    return key



def make_query_string(base_url,lat,long,key):
    lat_string = "lat={}".format(lat)
    long_string = "lon={}".format(long)
    appid_string = "appid={}".format(key)
    query_string = "&".join([lat_string,long_string,appid_string])
    query_string = "?".join([base_url,query_string])
    return query_string

def make_request(query_string):
    response = requests.get(query_string)
    return response
 
def make_dict_from_response(response):
    try: 
        return response.json()
    except:
        raise
    
def add_date_stamp(response_dict):
    response_dict['timestamp'] = stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
    pprint(stamp)
    return response_dict
    
def make_update_string(response_dict):
    #pprint(response_dict)

    latitude = response_dict['coord']['lat']
    longitude = response_dict['coord']['lon']
    temp = response_dict['main']['temp']
    temp_max = response_dict['main']['temp_max']
    temp_min = response_dict['main']['temp_min']
    humidity = response_dict['main']['humidity']
    pressure = response_dict['main']['pressure']
    feels_like = response_dict['main']['feels_like']
    sunrise = response_dict['sys']['sunrise']
    sunset =  response_dict['sys']['sunset']
    datetime = response_dict['timestamp']
    timezone = response_dict['timezone']
    city_name = response_dict['name']
    city_name = city_name.replace(" ", "")
    city_name = city_name.replace(",", "-")


    base_url = "http://10.132.66.195:8080/weather?"
    lat_str = "lat={}".format(str(latitude))
    long_str = "long={}".format(str(longitude))
    temp_str = "temp={}".format(str(temp))
    temp_max_str = "temp_max={}".format(str(temp_max))
    temp_min_str = "temp_min={}".format(str(temp_min))
    feels_like_str = "feels_like={}".format(str(feels_like))
    humidity_str = "humidity={}".format(str(humidity))
    pressure_str = "pressure={}".format(str(pressure))
    sunrise_str = "sunrise={}".format(str(sunrise))
    sunset_str = "sunset={}".format(str(sunset))
    datetime_str = "datetime={}".format(str(datetime))
    timezone_str = "timezone={}".format(str(timezone))
    city_name_str = "city={}".format(str(city_name))
    
    query_str = "&".join([lat_str,long_str,temp_str, temp_max_str, temp_min_str, feels_like_str, humidity_str, pressure_str,sunrise_str, sunset_str, datetime_str, timezone_str, city_name_str])
    query_str = base_url + query_str
    return query_str
    
    


ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 30

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def update_pipeline(count = 0):
    #outpath = os.getcwd()
    key_path = "/Users/jnapolitano/Projects/pmc-submission/jupyter-book/notebooks/weather_key.txt"
    lat = 34.047470
    long = -118.445950
    key = get_key(key_path)
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    query_string = make_query_string(base_url,lat,long,key)
    #pprint(query_string)
    response = make_request(query_string=query_string)
    response_dict = make_dict_from_response(response=response)
    response_dict = add_date_stamp(response_dict)
    update_str = make_update_string(response_dict)
    big_query_response = make_request(update_str)
    pprint(big_query_response)
    pprint(update_str)
    pprint(count)

    with PoolExecutor(max_workers=3) as executor:
        for _ in executor.map(update_pipeline, range(60)):
            pass 

    
def main():
    update_pipeline()

if __name__ == "__main__":
    main()
