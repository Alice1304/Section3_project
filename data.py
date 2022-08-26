# $ pip install requests
# $ pip3 install xmltodict
# $ pip install pandas

import requests, xmltodict, json
import pandas as pd
import sqlite3


#df_1 = 전립선암
df_1 = pd.DataFrame()
key_1 = '4Tn8%2FfrQZgV3pa%2F8YDMfW3qiYs%2BXYqQJ6zneFUw2v2WUOTZSBrSjaUAxrXGXc77hmrK2mk7wbz6owNw34daYUw%3D%3D'

for page_num in range(1,8):
    url = 'http://apis.data.go.kr/B551172/Prostate03/prJobByType?numOfRows=100&pageNo=' + str(page_num) + '&type=xml&fromYear=2010&toYear=2019&serviceKey={}'.format(key_1)
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    jsonString = json.dumps(dict['response'], ensure_ascii=False)
    jsonObj = json.loads(jsonString)
    df_11 = pd.DataFrame(jsonObj['items']['item'])
    df_1 = pd.concat([df_1,df_11])

df_1['type'] = '전립선암'


## 
#df_2 = 대장암

df_2 = pd.DataFrame()
key_2 = '4Tn8%2FfrQZgV3pa%2F8YDMfW3qiYs%2BXYqQJ6zneFUw2v2WUOTZSBrSjaUAxrXGXc77hmrK2mk7wbz6owNw34daYUw%3D%3D'

for page_num in range(1,39):
    url = 'http://apis.data.go.kr/B551172/Colon03/voJobByType?&numOfRows=100&pageNo=' + str(page_num) + '&fromYear=2010&toYear=2019&type=xml&serviceKey={}'.format(key_2)
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    jsonString = json.dumps(dict['response'], ensure_ascii=False)
    jsonObj = json.loads(jsonString)
    df_22 = pd.DataFrame(jsonObj['items']['item'])
    df_2 = pd.concat([df_2,df_22])

df_2['type'] = '대장암'

## 
#df_3 = 췌장암

df_3 = pd.DataFrame()
key_3 = '4Tn8%2FfrQZgV3pa%2F8YDMfW3qiYs%2BXYqQJ6zneFUw2v2WUOTZSBrSjaUAxrXGXc77hmrK2mk7wbz6owNw34daYUw%3D%3D'

for page_num in range(1,8):
    url = 'http://apis.data.go.kr/B551172/Pancreatic03/pnJobByType?numOfRows=100&pageNo=' + str(page_num) + '&type=xml&fromYear=2010&toYear=2019&serviceKey={}'.format(key_3)
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    jsonString = json.dumps(dict['response'], ensure_ascii=False)
    jsonObj = json.loads(jsonString)
    df_33 = pd.DataFrame(jsonObj['items']['item'])
    df_3 = pd.concat([df_3,df_33]) 

df_3['type'] = '췌장암'


## 
#df_4 = 담도암

df_4 = pd.DataFrame()
key_4 = '4Tn8%2FfrQZgV3pa%2F8YDMfW3qiYs%2BXYqQJ6zneFUw2v2WUOTZSBrSjaUAxrXGXc77hmrK2mk7wbz6owNw34daYUw%3D%3D'

for page_num in range(1,9):
    url = 'http://apis.data.go.kr/B551172/Cholan03/chJobByType?numOfRows=100&pageNo=' + str(page_num) + '&type=xml&fromYear=2010&toYear=2019&serviceKey={}'.format(key_4)
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    jsonString = json.dumps(dict['response'], ensure_ascii=False)
    jsonObj = json.loads(jsonString)
    df_44 = pd.DataFrame(jsonObj['items']['item'])
    df_4 = pd.concat([df_4,df_44])


df_4['type'] = '담도암'

## 
#df_5 = 폐암

df_5 = pd.DataFrame()
key_5 = '4Tn8%2FfrQZgV3pa%2F8YDMfW3qiYs%2BXYqQJ6zneFUw2v2WUOTZSBrSjaUAxrXGXc77hmrK2mk7wbz6owNw34daYUw%3D%3D'


for page_num in range(1,179):
    url = 'http://apis.data.go.kr/B551172/Lung03/luJobByType?fromYear=2010&toYear=2020&type=xml&numOfRows=100&pageNo=' + str(page_num) + '&serviceKey={}'.format(key_5)
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    jsonString = json.dumps(dict['response'], ensure_ascii=False)
    jsonObj = json.loads(jsonString)
    df_55 = pd.DataFrame(jsonObj['items']['item'])
    df_5 = pd.concat([df_5,df_55])


df_5['type'] = '폐암'


## 
#df_6 = 신장암

df_6 = pd.DataFrame()
key_6 = '4Tn8%2FfrQZgV3pa%2F8YDMfW3qiYs%2BXYqQJ6zneFUw2v2WUOTZSBrSjaUAxrXGXc77hmrK2mk7wbz6owNw34daYUw%3D%3D'

for page_num in range(1,8):
    url = 'http://apis.data.go.kr/B551172/Kidney03/kiJobByType?numOfRows=100&fromYear=2010&toYear=2019&type=xml&pageNo=' + str(page_num) + '&serviceKey={}'.format(key_6)
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    jsonString = json.dumps(dict['response'], ensure_ascii=False)
    jsonObj = json.loads(jsonString)
    df_66 = pd.DataFrame(jsonObj['items']['item'])
    df_6 = pd.concat([df_6,df_66])

df_6['type'] = '신장암'


## 
#df_7 = 위암

df_7 = pd.DataFrame()
key_7 = '4Tn8%2FfrQZgV3pa%2F8YDMfW3qiYs%2BXYqQJ6zneFUw2v2WUOTZSBrSjaUAxrXGXc77hmrK2mk7wbz6owNw34daYUw%3D%3D'

for page_num in range(1,122):
    url = 'http://apis.data.go.kr/B551172/Gastric03/gsJobByType?type=xml&numOfRows=100&fromYear=2010&toYear=2019&pageNo=' + str(page_num) + '&serviceKey={}'.format(key_7)
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    jsonString = json.dumps(dict['response'], ensure_ascii=False)
    jsonObj = json.loads(jsonString)
    df_77 = pd.DataFrame(jsonObj['items']['item'])
    df_7 = pd.concat([df_7,df_77])

df_7['type'] = '위암'


## 
#df_8 = 간암

df_8 = pd.DataFrame()
key_8 = '4Tn8%2FfrQZgV3pa%2F8YDMfW3qiYs%2BXYqQJ6zneFUw2v2WUOTZSBrSjaUAxrXGXc77hmrK2mk7wbz6owNw34daYUw%3D%3D'

for page_num in range(1,109):
    url = 'http://apis.data.go.kr/B551172/Liver03/lvJobByType?type=xml&numOfRows=100&fromYear=2010&toYear=2019&pageNo=' + str(page_num) + '&serviceKey={}'.format(key_8)
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    jsonString = json.dumps(dict['response'], ensure_ascii=False)
    jsonObj = json.loads(jsonString)
    df_88 = pd.DataFrame(jsonObj['items']['item'])
    df_8 = pd.concat([df_8,df_88])

df_8['type'] = '간암'

df = pd.concat([df_1,df_2,df_3,df_4,df_5,df_6,df_7,df_8])