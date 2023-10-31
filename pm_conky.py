#!/usr/bin/python3
#coding=utf-8
# 抓取 iqair.cn 空气质量和天气
# ver.20230925  修改网址和伪装浏览器
# ver.20231017 配合conky显示

import urllib.request
import requests
import re
from bs4 import BeautifulSoup  
import os
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

linkurl = 'https://www.iqair.cn/cn/china/hebei/shijiazhuang/xinhua' #url对应空气监测站点
air_site = linkurl.split('/')[-1] #获取唯一的站点名称

res = requests.get(linkurl, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')


def PmOutput(): 
    air_aqi = soup.find("p", class_="aqi-value__value").string #aqi数值
    
    air_all = soup.find("table", class_="aqi-overview-detail__other-pollution-table") #空气质量table

    pm25 = air_all.find_all('tr')[1]  # 第二个tr
    pm25_num = pm25.find_all('td')[2].select('span')[0].string

    pm10 = air_all.find_all('tr')[2]
    pm10_num = pm10.find_all('td')[2].select('span')[0].string

    weather = soup.find("div", class_="weather") #天气部分
    temperature = weather.table.find_all('tr')[1].find_all('td')[1].string
    humidity = weather.table.find_all('tr')[2].find_all('td')[1].string

    air_output = 'AQI: ' + str(air_aqi) + ' | PM2.5: ' + str(pm25_num) + ' | PM10: ' + str(pm10_num)
    #  给输出命令行加颜色，\033[32;40m为褐底蓝色

    print(air_output)
    

PmOutput()


