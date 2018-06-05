#!/usr/local/Python3.6.4/bin/python
# coding=utf-8
# -*- coding: utf-8 -*-
import datetime
import json
from multiprocessing import Pool
import pandas as pd
import data_aliyun
import weatherApi
import weatherCityListProcessor
import config
import logger,os

params = {'wind': 'CLDAS-WIND',
          'sun': 'CLDAS-SSRA',
          'temp': 'CLDAS-TEMP',
          'rain': 'CMPA-PREP',
          'wet': 'CLDAS-SHU',
          'prs': 'CLDAS-PRS'}


def row_processor(row):
    for param in params:
        unfinish = True
        while (unfinish):
            try:
                value = weatherApi.get(
                    row['timepoint'],
                    params[param],
                    row['latitude'],
                    row['longitude']
                )
                row[param] = value
                unfinish = False
            except:
                #print('connection error')
                pass
    # print(row)
    return row


if __name__ == '__main__':
    city_list = json.loads(data_aliyun.stationList_json)
    date_str = (datetime.datetime.now() - datetime.timedelta(days=1)).__format__('%Y%m%d')
    date_str1 = (datetime.datetime.now() - datetime.timedelta(days=1)).__format__('%Y-%m-%d')
    pool = Pool(80)
    results = []
    row_lists = weatherCityListProcessor.process(city_list)
    time = datetime.datetime.now()
    results = pool.map(row_processor, row_lists)
    pool.close()
    pool.join()
    logger = logger.getLogger(os.path.splitext(os.path.basename(__file__))[0])
    logger.info('craw data success!')
    results = pd.DataFrame(results)
    # results.columns = ('prs', 'rain', 'sun', 'temp', 'wet', 'wind', 'timepoint',
    #                    'city', 'latitude', 'longitude', 'stationname', 'province',
    #                    'stationcode', 'timepoint2')
    results = results[['timepoint2','province', 'city', 'positionname', 'stationcode',
                      'sun', 'rain', 'prs', 'temp', 'wet', 'wind', 'latitude', 'longitude']]
    results.to_csv(config.dataFilePath+date_str1+'.csv')
    logger.info('write data success!')
    # print(results)
    print(datetime.datetime.now() - time)
