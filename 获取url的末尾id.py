#由于获取的url的id不太稳定，遂开发此文档

import json

base_url='https://www.brownsfashion.com/hk/shopping/arcteryx-black-rush-insulated-jacket-'
with open('all_men_urls.json','r') as f:
    data = json.load(f)
new_data=[]
for d in data:
    new_d=d.split('-')[-1]
    print(new_d)
    new_url=base_url+str(new_d)
    new_data.append(new_url)

with open('all_men_urlsnew.json','w') as f:
    json.dump(new_data,f)
