import json
import requests
from bs4 import BeautifulSoup
import cloudscraper
from pprint import pprint
#目标网站含有cloudflare反爬机制
scraper=cloudscraper.create_scraper()
#没有搭配的图片
#https://www.brownsfashion.com/hk/shopping/y-project-blue-evergreen-maxi-cowboy-straight-leg-jeans-23387182
#有搭配的图片
#

#获取搭配的链接
def get_other(url):
    maxretry=5
    other_url=[]
    base_url='https://www.brownsfashion.com/hk/shopping/arcteryx-black-rush-insulated-jacket-'
    id=url.split('-')[-1]
    header={
        'Referer':url,
        # 'X-Castle-Request-Token':'LyZ5FlZWYl8bXXdWGUcYV1xVYWlHZxpWdlhOVWh2emQbSGdg0nVrgBcLax-hl5TiAD0Pz16VLZLAx_pjX57ndFvvj00d2_kweRJnZGaR701GoOFeVNIHYBGXmj-XMrBlLAblaAGZ5x85lJotMe-ODDL0yFVwpcdICfyJBDHilEAQwcdRbrvXW37Cjg5oodxAJqPTSX7UlxAy8LAFPN6OFHGg1FdwptFAdt6vNBPZy0Ay_IwFftKCAzX6zkAd_ZUPM_DIUWygyVBwpclQfsaGBj_njk9rptBObaPHJTryyFFsoMlQcKXJUDKdhlBm8dJYPaaQY14e5_RW9tVWavTfBjoJsiEQ0qslfr2uDirwi0x-3IkUO_nPMne1sigataASP-WPCT3mx1ZtpcdIbu3XUG6l1CVnp85AGvyVBT3h1CRvpMcWLcrSP261lxMBoLhQcrWjUxqk1kn6hNZZaaXIUXGkx1Bmr9dQZKXXz1aVUkGbJRirXkbmvd1NAGC1lhAxI0g2paE3jeNdlettH-aOAXHGjwEw8o8BN4HzGja4pC5y8IlMO_vKJxy5gg5zwLQgXubnYF6V52BeledgXpXnYF6V52BeLL_ZBtXnIB6V52Be1acgHtWnCF795woMPU_-wNzn1STn7GBeledgXpTnn_E',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    retry1=0
    while retry1<maxretry:
        try:
            url=f'https://www.brownsfashion.com/api/commerce/v1/products/{id}/outfits'
            res=scraper.get(url,headers=header).text
            # print(res)
            if res !='[]':
                print('已在短链接中找到相关搭配')
                jsondata=json.loads(res)
                data=jsondata[0]['products']
                for d in data:
                    d_url=base_url+str(d['productId'])
                    other_url.append(d_url)
                return other_url
            else:
                break

        except Exception as e:
            print(f"{url}请求时发现错误{e}")
            print(f"请求失败,正在重试... ({retry1 + 1}/{maxretry})")
    # raise Exception(f"无法完成URL {url} 的请求,已达到最大重试次数")
    retry2 = 0
    while retry2 < maxretry:
        try:
            url=f'https://www.brownsfashion.com/api/marketing/v1/recommendations/outfits?productId={id}&strategyName=web_pdp_outfit&recommendedPageName=pdp&gender=0&countryCode=HK&userType=userId&userIdentifier=370701918'
            res=scraper.get(url,headers=header).text
            # print(res)
            jsondata=json.loads(res)
            if jsondata[0]['outfits']!=[]:
                print('已在长连接中找到相关链接！')
                data=jsondata[0]['outfits'][0]['products']
                for d in data[1:]:
                    # print(d)
                    d_url = base_url + str(d['id'])
                    other_url.append(d_url)
                return other_url
            else:
                break
        except Exception as e:
                print(f"{url}请求时发现错误{e}")
                print(f"请求失败,正在重试... ({retry2 + 1}/{maxretry})")
    # raise Exception(f"无法完成URL {url} 的请求,已达到最大重试次数")
    return []

#测试的url
# url='https://www.brownsfashion.com/hk/shopping/arcteryx-black-rush-insulated-jacket-22934025'#短字符的
url='https://www.brownsfashion.com/hk/shopping/y-project-blue-evergreen-maxi-cowboy-straight-leg-jeans-23387182'#没有搭配图片的
# url='https://www.brownsfashion.com/hk/shopping/y-project-white-checked-invisible-strap-top-22385494'
# url='https://www.brownsfashion.com/hk/shopping/alexander-wang-black-faux-fur-cuff-cropped-cardigan-22099358'#长字符的其他链接
# print(get_other(url))

# url='https://www.brownsfashion.com/hk/shopping/y-project-white-checked-invisible-strap-top-22385494'

def get_res(url):
    retry=0
    while retry<5:
        try:

            res=scraper.get(url,timeout=30).text
            return res
        except Exception as e:
            print(f"error get {url}: {e}")
            retry+=1
            continue
    print('已经达到最大次数')
    return None

#获取该页面的主要图片
def get_main_pic(url):
    try:
        print(f'正在下载{url}中的图片！！！')
        main_pic=[]
        nameid=url.split('-')[-1]
        res=get_res(url)
        # print(res)
        bs=BeautifulSoup(res,'html.parser')
        # print(bs)
        alldata=bs.find_all('script')

        for data in alldata:
            if 'window.__PRELOADED_STATE__' in data.text:
                data_text=data.text.split('window.__SITE_FEATURES__')[0].split('window.__PRELOADED_STATE__ =')[1].strip()
                json_data=json.loads(data_text)
                img_list=json_data['entities']['products'][nameid]['images']
                for img in img_list:
                    img_url=img['sources']['1920']
                    main_pic.append(img_url)
                    # print(img_url)
        return main_pic
    except:
        return []

def get_all_pic(url):
    all_pic=[]
    main_pic=get_main_pic(url)
    all_pic.extend(main_pic)
    others=get_other(url)
    for other in others:
        other_pic=get_main_pic(other)
        all_pic+=other_pic
    print(all_pic)
    return all_pic,others

if __name__=='__main__':
    url='https://www.brownsfashion.com/hk/shopping/arcteryx-black-rush-insulated-jacket-22138736'
    all_pic,panduan=get_all_pic(url)
    print(all_pic)
    print(panduan)

        # pprint(json_data)