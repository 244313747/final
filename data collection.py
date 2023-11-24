#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Data collection 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：kai
@Date    ：2023/9/29 18:33 
'''
from lxml import  html
from lxml import  etree as eee
import  pandas as pd

import requests

target_url = "http://httpbin.org/ip"
proxy_host = 'http-dynamic.xiaoxiangdaili.com'
proxy_port = 10030
proxy_username = '1017390935040217088'
proxy_pwd = 'P13z2UQz'

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxy_host,
        "port": proxy_port,
        "user": proxy_username,
        "pass": proxy_pwd,
}
session = requests.session()
proxies = {
        'http' : proxyMeta,
        'https': proxyMeta,
}
headers = {
    "authority": "www.nosetime.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.nosetime.com/searchcolor.php",
    "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "Hm_lvt_bc9aac562f84656cc4182658d4ca76ba": "1695949329",
    "uid": "33654825",
    "Hm_lpvt_bc9aac562f84656cc4182658d4ca76ba": "1695978168"
}
data_list = []
data_yanse = [('I', 60), ('H', 98), ('G', 55), ('F', 36), ('E', 5), ('C', 100), ('B', 24), ('A', 100), ('R', 100), ('Q', 100), ('P', 100), ('O', 100), ('N', 100), ('M', 100), ('L', 100), ('K', 10), ('J', 89)]
for code, max_page in data_yanse:
    for page in range(1,max_page+1):
        try:
            url_search = 'https://www.nosetime.com/searchcolor.php?c={}&vx=1&zxx=1&nx=1&p={}'.format(str(code),str(page))
            print(url_search)
            try:

                response = session.get(url_search, headers=headers, cookies=cookies,proxies=proxies).text
                # print(response)
                etree_obj = html.fromstring(response)
                url_x = etree_obj.xpath('//a[contains(@href, "/xiangshui/")]/@href')
            # print(url_x)
            except Exception as e   :
                print('该页数为空')
                continue
            for ulr_s  in url_x:
                try:
                    detail_id =ulr_s.split('/xiangshui/')[1].split('-')[0]
                    # print(detail_id)
                    detail_url = "https://www.nosetime.com/app/item.php"
                    params = {
                        "id": str(detail_id)
                    }
                    response = session.get(detail_url, headers=headers, cookies=cookies, params=params,proxies=proxies).json()
                    # print(response)
                    ifullname = response['ifullname'] # 名字
                    brand = response['brand'] # 品牌

                    attrib = response.get('attrib','')
                    img_url = 'https://img.xssdcdn.com/perfume/{}.jpg'.format(detail_id) #图片链接

                    intro = response.get('intro','')# 简介


                    perfumer = response.get('perfumer','') # 调香师

                    fragrance = response.get('fragrance','')# 香调

                    data = response['mainodor']
                    # 使用列表推导取出'uoodor'
                    uoodor_list = [item['uoodor'] for item in data]
                    # 使用逗号连接'uoodor'
                    uoodor_string = ', '.join(uoodor_list)

                    data_list.append({
                        "名称": ifullname,
                        "品牌": brand,
                        "属性": attrib,
                        "图片链接": img_url,
                        "简介": intro,
                        "调香师": perfumer,
                        "香调": fragrance,
                        "主要香味": uoodor_string
                })
                except Exception as e:
                    print('详情页出现问题 无法保存 : {}'.format(e))
                    continue
            df = pd.DataFrame(data = data_list)

            # 保存DataFrame到Excel
            excel_path = "{}.xlsx".format(code)
            df.to_excel(excel_path, index=False)

            # print(f"数据已写入到 {excel_path}")
        except Exception as e:
            continue
