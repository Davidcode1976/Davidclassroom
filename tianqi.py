# -*- coding:utf-8 -*-

import requests

while True:
    city_name=input('请输入查询天气的城市名称:\n')
    url='http://wthrcdn.etouch.cn/weather_mini?city=%s'%city_name
    req=requests.get(url)
    #print(req.text)
    req_data=req.json()
    #print(req_data)
    result=req_data.get('data')
    #print(result)
    if result:
        print('城市名称:',result.get('city'))
        print('目前温度:',result.get('wendu'),'摄氏度')
        print('感冒指数:',result.get('ganmao'))
        print('今日及未来四天天气预报:')
        forecast_result=result.get('forecast')
        #print(forecast_result)
        #print(type(forecast_result))
        for fr in forecast_result:
            print('日期:%s,天气:%s,最高温度:%s,最低温度:%s,风向:%s,风力:%s\n'% (fr.get('date'),fr.get('type'),fr.get('high'),fr.get('low'),fr.get('fengxiang'),fr.get('fengli')))
    else:
        print('很遗憾!没有该城市信息')

    quit=input('退出请按"q",按其他键继续查询')
    if quit=='q' or quit=='Q':
        break


