import json
import requests
from bs4 import BeautifulSoup
import cloudscraper
#目标网站含有cloudflare反爬机制
scraper=cloudscraper.create_scraper()
header={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control':'no-cache',
    'Cookie':'benefit=264CBB89ED4B5B752363C1AAF409FF; csi=21f27c3e-079a-498e-8680-44cf759fdbe9; optimizelyEndUserId=oeu1718170342403r0.25347446125382134; _gid=GA1.2.459780963.1718170343; tms_VisitorID=1te4ge9deo; _gcl_au=1.1.356407513.1718170344; rskxRunCookie=0; rCookie=4e0r04yaoh8nj7jthzvxplxbe9e9a; _fbp=fb.1.1718170344310.450200997983906822; _tt_enable_cookie=1; _ttp=40j6T3NpPEIjieGjOVUxqcojEnD; _pin_unauth=dWlkPU1USTRObU5oWkRNdFl6YzFNQzAwTjJJNUxXRmxabUV0TXpVMU5EY3dPVGcxT1RnNQ; _hjSessionUser_1781677=eyJpZCI6ImE5NDVkMGQ0LWJjN2ItNTFiOS1hMjZkLTIxMDJiZTM2ODdhNyIsImNyZWF0ZWQiOjE3MTgxNzAzNDQzMjksImV4aXN0aW5nIjp0cnVlfQ==; ftr_ncd=6; __cfruid=bcd062705e524147ce4fdaacb5d6d9bd52994a38-1718240616; cf_clearance=e5o8zaDFUMSoLJWHK_YBtcFC5TisatreufBOqGqZHhE-1718240617-1.0.1.1-k4u_tiH0WLg09MFkM9in_m32uZ0s9V6_.aKbS2XBV6Prrt6.CefU9CA8X6CoUlAEI_enouSLlXfUAzVZI5fQIQ; ftr_blst_1h=1718240618520; tms_wsip=1; _hjSession_1781677=eyJpZCI6IjJiOWQ1YzlmLTJiZDgtNDNkZC1iNjE3LTU4OTcxZTI1OWNhNCIsImMiOjE3MTgyNDA2MTg3ODgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; ctx=%7b%22u%22%3a370701918%2c%22g%22%3a0%7d; __Secure-sc=XuC5J3yUpXpuvKKoRLabjcz4Dn2iAYhH1K11ciFOl9SljyHtaax2VZB2vDohTD%2F4Sl34OOCO%2FPVk1kpYdrv9vcfHvbaX8Bg86Y10p6fxbfxf%2BEZrlPf8zhlG%2FlaAY0glyLlVx944%2F0yoqt2aeG%2BiGYYBwZvEhqG%2BLpf%2FcwFwIzZP3CneFST2ETuDv%2FVhaXA4y0OOiCroFGGdjbDtipM7bI79fLvORM4GYu59V8setQ%2B1aNfUt9QfgUJww2DSdFDsFxi0tFZNBkg2eStcGADC%2BU9YA6bKWdKEo7VSjFVKNkNVYvDMLh%2FnbH1pmAq0djS8KUpt5zyaxJO%2Blt%2FzJbfWVA%3D%3D; _gat_UA-699627-7=1; _gat_gtag_UA_699627_7=1; _ga_6EXGM6SE3V=GS1.1.1718240618.4.1.1718241126.0.0.0; @farfetch/blackout-react__gcm_shared_consent_mode=[["consent","default",{"ad_personalization":"denied","ad_storage":"denied","ad_user_data":"denied","analytics_storage":"denied"}],["consent","update",{"ad_personalization":"granted","ad_storage":"granted","ad_user_data":"granted","analytics_storage":"granted"}],["consent","update",{"ad_personalization":"granted","ad_storage":"granted","ad_user_data":"granted","analytics_storage":"granted"}]]; __cuid=fd5a44af382444308eb8bbcd2f1220e0; _uetsid=25d86170287d11ef9f53810847e597c3; _uetvid=25d88a00287d11ef852df1b0a7b77904; lastRskxRun=1718241127270; _ga_30N061DRTP=GS1.1.1718240618.4.1.1718241127.57.0.0; _ga=GA1.2.1248676149.1718170343; forterToken=86c4e8953e9341b4bc7826af55169e65_1718241126550__UDF43-m4_15ck_',
    'Pragma':'no-cache',
    'Priority':'u=0,i',
    'Referer':'https://www.brownsfashion.com/hk/account/login?returnurl=/hk/shopping/y-project-blue-evergreen-maxi-cowboy-straight-leg-jeans-23387182',
    'Sec-Ch-Ua':'"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':"Windows",
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    # 'Sec-Fetch-Site':'none',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
   # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
}
# /hk/shopping/woman-clothing?pageindex=1
url='https://www.brownsfashion.com/hk/shopping/woman-clothing?pageindex=1'
def get_one_page(url):
    url_list=[]
    res=scraper.get(url).text
    # print(res.text)
    bs=BeautifulSoup(res,'html.parser')
    data=bs.find_all('script',{'type':'application/ld+json'})
    json_data=json.loads(data[0].text)
    clothes_data=json_data['itemListElement']
    for data in clothes_data:
        clothes_url=data['url']
        print(clothes_url)
        url_list.append(clothes_url)
    return url_list


all_urls=[]
for i in range(25):
    url = f'https://www.brownsfashion.com/hk/shopping/man-clothing?pageindex={i+1}'
    print(url)
    page_urllist=get_one_page(url)
    all_urls.extend(page_urllist)


with open('all_men_urls.json','w') as f:
    json.dump(all_urls,f)

