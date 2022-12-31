import requests
import time
import json

url = "https://api.divar.ir/v8/web-search/1/residential-sell"
json1 ={"json_schema":{"category": {"value": "residential-sell"}, "cities": ["1"]},
"last-post-date": 1672154996735027}
headers = {
    "Content_Type": "application/json"}

tokens_list=[]
res =requests.post(url, json=json1,headers=headers)

data=res.json()

last_post_date=data['last_post_date']


count=0
while True:
    
    url = "https://api.divar.ir/v8/web-search/1/residential-sell"
    json2 ={"json_schema":{"category": {"value": "residential-sell"}, "cities": ["1"]},
    "last-post-date": last_post_date}
    headers = {
        "Content_Type": "application/json"}
    
    res=requests.post(url,json=json2, headers=headers)
    
    try:
        data= res.json()
        
        last_post_date=last_post_date-800000
        
     
        
        
        
        last_post_date=data['last_post_date']
    

    
        for item in data['web_widgets']['post_list']:
            token=item['data']['token']
            tokens_list.append(token)
        
        
            count+=1
        
        if count>=7000:
            break
    except:
        print (last_post_date,count)
        txt_file=open ('token15.txt','w',encoding='utf8')
        txt_file.write(','.join(tokens_list))
        txt_file.close()
        break

   
    else:

        txt_file=open ('token15.txt','w',encoding='utf8')
        txt_file.write(','.join(tokens_list))
        txt_file.close()



    