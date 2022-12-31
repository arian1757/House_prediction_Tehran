from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

my_tokens=open('token7.txt','r')
my_tokens=my_tokens.read().split(',')
tokens_not=[]
dataset=[]
urls=list(map (lambda x:'https://api.divar.ir/v8/posts-v2/web/%s' %(x),my_tokens))





for url in urls:
    try:
        res=requests.get(url)

        data=res.json()
    except:
        tokens_not.append(url)
        continue
    try:
        district=data['sections'][1]['widgets'][0]['data']['subtitle'].split('،')[1].split('|')[0]
        area=data['sections'][8]['widgets'][0]['data']['items'][0]['value']
        year=data['sections'][8]['widgets'][0]['data']['items'][1]['value']
        rooms=data['sections'][8]['widgets'][0]['data']['items'][2]['value']
        value=data['sections'][8]['widgets'][1]['data']['value'].split()[0]
        floor=data['sections'][8]['widgets'][4]['data']['value']
    except:
        continue
    try:
            elevator=data['sections'][8]['widgets'][6]['data']['items'][0]['available'],
    except:
            elevator=False

    try:
            parking=data['sections'][8]['widgets'][6]['data']['items'][1]['available'],
    except:
            parking=False
    try:
            warehouse=data['sections'][8]['widgets'][6]['data']['items'][1]['available']
    except:
            warehouse=False
    
    house={
        'district':district,
        'area':area,
        'year':year,
        'rooms':rooms,
        'value':value,
        'floor':floor,
        'elevator':elevator,
        'parking':parking,
        'warehouse':warehouse
        
        }
    
    dataset.append(house)

x=pd.DataFrame(dataset)
x.to_csv('dataset2.csv')
txt_file=open ('noturls.txt','w',encoding='utf8')
txt_file.write(','.join(tokens_not))
txt_file.close()




