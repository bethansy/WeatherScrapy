#!/usr/local/Python3.6.4/bin/python
import datetime


def process(city_list):
    date_str = (datetime.datetime.now() - datetime.timedelta(days=1)).__format__('%Y%m%d')
    date_str2 = (datetime.datetime.now() - datetime.timedelta(days=1)).__format__('%Y-%m-%d')
    row_list = []
    for i in city_list:
        for j in city_list[i]:
            for k in city_list[i][j]:
                for l in range(0, 24):
                    row = {
                        'province': i,
                        'stationcode': k['StationCode'],
                        'city': j,
                        'positionname': k['PositionName'],
                        'latitude': k['Latitude'],
                        'longitude': k['Longitude'],
                        'timepoint': date_str + (str(l) if l > 9 else '0' + str(l)) + '0000',
                        'timepoint2': date_str2 + ' ' + (str(l) if l > 9 else '0' + str(l)) + ':00:00'
                    }
                    row_list.append(row)
    return row_list
