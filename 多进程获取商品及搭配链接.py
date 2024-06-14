import json

from 获取商品的商品图以及相关搭配 import get_all_pic
import multiprocessing
from multiprocessing import Pool

def main(url):
    print(f'《《{url}》》获取所有图片中！！！！！！！！！！')
    all_pic ,other= get_all_pic(url)
    if other !=[]:
        id=url.split('-')[-1]
        return {id:all_pic}
    else:
        return {}

if __name__ == '__main__':
    all_dic={}
    with open('all_men_urlsnew.json','r') as f:
        data=json.load(f)
    with Pool(6) as p:
        result=p.map(main,data)
    for i in result:
        all_dic.update(i)
    with open('all_men_picnew.txt','w') as f:
        json.dump(all_dic,f,indent=4)
