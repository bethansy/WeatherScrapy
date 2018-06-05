#!/usr/local/Python3.6.4/bin/python
import json

import requests

url = "http://nature.data.aliyun.com/api"


def get(date_time_str, param, lat, lng):
    params = {'token': '1gCALvcR64',
              'action': 'data_value_by_date_name_geometry',
              'name': param,
              'date': date_time_str,
              'geometry': lng + ',' + lat}
    response = requests.get(url, params, timeout=3)
    data = json.loads(response.text)
    return data['data']['data_value_by_date_name_geometry']['value']


