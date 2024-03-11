import requests, json, traceback
import random, pywebio, csv
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

newslisttempt = []
MOUNT = 0

def UDN():
    for i in range(1, 3):
        cookies = {
            '_fbp': 'fb.1.1705550573517.19494459',
            '_gid': 'GA1.2.1147267168.1705550574',
            'dable_uid': '29769332.1705540641918',
            '_cc_id': 'e125a6f346e82b118fd689e6b19ef377',
            '_pbjs_userid_consent_data': '3524755945110770',
            '_pubcid': '25227352-2c30-496c-ad5c-11ab40d3e119',
            '__qca': 'P0-768388839-1705550576675',
            'trc_cookie_storage': 'taboola%2520global%253Auser-id%3D319855e9-38cf-4a14-b91f-df63ed741db8-tuctca180f9',
            '_im_vid': '01HMDBS2Y71VV1Q056D506D5HY',
            'pbjs-unifiedid': '%7B%22TDID%22%3A%22e1a0a26d-5fa5-47f4-b53a-54979b5c4f85%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-12-18T04%3A03%3A01%22%7D',
            '_rtbpbjs_userid_consent_data': '3524755945110770',
            '_sharedID': 'a08e5e8c-96ae-4e47-ad06-3f34ef65f34f',
            '_au_1d': 'AU1D-0100-001705633544-F2K6SFLB-6TZE',
            'truvid_protected': '{"val":"c","level":2,"geo":"HK","timestamp":1705633556}',
            'ucf_uid': 'f317e774-7b85-4a42-9747-ae3dd1c77c2d',
            'OX_plg': 'wmp|pm',
            '_gcl_au': '1.1.296702941.1705723913',
            'last_view_story': '/vip/story/122365/7722012',
            'last_view_tag': '%E6%8A%96%E9%9F%B3,%E6%B0%91%E9%80%B2%E9%BB%A8,%E5%81%87%E8%A8%8A%E6%81%AF,%E5%B0%88%E8%AB%96,%E6%94%BF%E6%B2%BB',
            'last_view_parameter': 'undefined',
            'last_view_cate': '122364,%E8%A9%95%E8%AB%96',
            '__gsas': 'ID=2eb3e717db92b58c:T=1705723917:RT=1705723917:S=ALNI_Ma4gmQHRDuv43L4SHk7WcGkpTHnEg',
            '_ga_7MZR1WNFGY': 'GS1.1.1705723914.1.1.1705723929.45.0.0',
            '_ga_XJKH64P6N7': 'GS1.1.1705723914.1.1.1705723929.45.0.0',
            'panoramaId': '400237e71fa49790215edd01fb49a9fb927a425a3c4d8c2ef525d7d61a86bddb',
            'panoramaIdType': 'panoDevice',
            'panoramaId_expiry': '1705885852367',
            '_au_last_seen_pixels': 'eyJhcG4iOjE3MDU3OTk0NTYsInR0ZCI6MTcwNTc5OTQ1NiwicHViIjoxNzA1Nzk5NDU2LCJydWIiOjE3MDU3OTk0NTYsInRhcGFkIjoxNzA1Nzk5NDU2LCJhZHgiOjE3MDU3OTk0NTYsImdvbyI6MTcwNTc5OTQ1NiwiY29sb3NzdXMiOjE3MDU3OTk5NTAsImltcHIiOjE3MDU3OTk5NTAsImFtbyI6MTcwNTgwMDAwMywicHBudCI6MTcwNTc5OTk1MCwiaW5kZXgiOjE3MDU3OTk5NTAsIm9wZW54IjoxNzA1Nzk5OTUwLCJiZWVzIjoxNzA1Nzk5NDU2LCJ1bnJ1bHkiOjE3MDU3OTk5NTAsInRhYm9vbGEiOjE3MDU3OTk5NTAsInNtYXJ0IjoxNzA1Nzk5OTUwLCJzb24iOjE3MDU3OTk0NTYsImFkbyI6MTcwNTc5OTk1MH0%3D',
            '_ga_TPXF8L10NG': 'GS1.1.1705800312.1.0.1705800371.1.0.0',
            '_ga_E3TLKYMMWW': 'GS1.1.1705800312.1.0.1705800371.1.0.0',
            'cto_bidid': 'lfrN5F9PZTVoY0JLdVVUcmM3R3dDNzZhRlpVWFlpdGw4Z3daeDJ4VnVZNmtoRkRVUDMxSzVEJTJCekRDeFV4N1prVlZicTJpWCUyQlR1cjdwTjh6bkJIc01OYnFwZTA0Y1lxVVJkUkJsZTROY0Rua29ZWER0RUszczlJN2NjRTFxSFVwOTRIZXcwOSUyRnZRRXFzUnBOUk5XV0tnbXZXdnclM0QlM0Q',
            'AMP_TOKEN': '%24NOT_FOUND',
            '__eoi': 'ID=124eb18beb3df141:T=1705712731:RT=1705807388:S=AA-AfjaRtafWn5kWVk6juUuxDLvj',
            '__AP_SESSION__': '949c289a-a17c-4bde-8ce3-851638610cca',
            '__gads': 'ID=cad3044fb287b1da:T=1705550574:RT=1705807409:S=ALNI_MabYLXmYFjvgeULP-AHAwAZCoje2w',
            '__gpi': 'UID=00000ce9d38f398b:T=1705550574:RT=1705807409:S=ALNI_Mb8PEVkEh5rZV58S2Z_3J0tNDIp_Q',
            '_ga_7THXRBK2CK': 'GS1.1.1705807384.9.1.1705807427.17.0.0',
            '_ga': 'GA1.1.102305793.1705550574',
            '_ga_NEBRGBLTFZ': 'GS1.1.1705807384.9.1.1705807427.17.0.0',
            'FCNEC': '%5B%5B%22AKsRol9gOsXpHVZN743ETSdup7EdZKes4szA3loe9ODfqAPwTICKK7Apm7fEmVpsIgxscCgkF2gjkUGzCUOMhwMc75PjvFPgt8xsb27xLJIQN1J-d2VDxCpECwaPJ9UOKWF3P9e9mftCl2lETZR_tFHLfwEoUCB26A%3D%3D%22%5D%5D',
            'cto_bundle': 'i5Whf18waG9qRTlTQ09jd1ZGYWpXZ28zTmJmc3pDNFgxOWdWU01jNjJmMHFYN3daSnlzTHRFM0VYd1o4b2dYcTVuYVJ4WE5uSiUyQnNJYjB0OXBoSlFkbzAlMkJHbWpkcmlEcEIwRzc5aG82T016dGdBMDJkNHlOMDdSY213TExnNzdociUyQnpMbVZCZHh2YlA3cEx4TlU2JTJGVEclMkZvWGNlNyUyRlBXJTJGY2x2dlg0a25rdDlSNWJNaG5LWnZEbVA3STlPMGVoRTFaQ3RkVA',
        }

        headers = {
            'authority': 'udn.com',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            # 'cookie': '_fbp=fb.1.1705550573517.19494459; _gid=GA1.2.1147267168.1705550574; dable_uid=29769332.1705540641918; _cc_id=e125a6f346e82b118fd689e6b19ef377; _pbjs_userid_consent_data=3524755945110770; _pubcid=25227352-2c30-496c-ad5c-11ab40d3e119; __qca=P0-768388839-1705550576675; trc_cookie_storage=taboola%2520global%253Auser-id%3D319855e9-38cf-4a14-b91f-df63ed741db8-tuctca180f9; _im_vid=01HMDBS2Y71VV1Q056D506D5HY; pbjs-unifiedid=%7B%22TDID%22%3A%22e1a0a26d-5fa5-47f4-b53a-54979b5c4f85%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-12-18T04%3A03%3A01%22%7D; _rtbpbjs_userid_consent_data=3524755945110770; _sharedID=a08e5e8c-96ae-4e47-ad06-3f34ef65f34f; _au_1d=AU1D-0100-001705633544-F2K6SFLB-6TZE; truvid_protected={"val":"c","level":2,"geo":"HK","timestamp":1705633556}; ucf_uid=f317e774-7b85-4a42-9747-ae3dd1c77c2d; OX_plg=wmp|pm; _gcl_au=1.1.296702941.1705723913; last_view_story=/vip/story/122365/7722012; last_view_tag=%E6%8A%96%E9%9F%B3,%E6%B0%91%E9%80%B2%E9%BB%A8,%E5%81%87%E8%A8%8A%E6%81%AF,%E5%B0%88%E8%AB%96,%E6%94%BF%E6%B2%BB; last_view_parameter=undefined; last_view_cate=122364,%E8%A9%95%E8%AB%96; __gsas=ID=2eb3e717db92b58c:T=1705723917:RT=1705723917:S=ALNI_Ma4gmQHRDuv43L4SHk7WcGkpTHnEg; _ga_7MZR1WNFGY=GS1.1.1705723914.1.1.1705723929.45.0.0; _ga_XJKH64P6N7=GS1.1.1705723914.1.1.1705723929.45.0.0; panoramaId=400237e71fa49790215edd01fb49a9fb927a425a3c4d8c2ef525d7d61a86bddb; panoramaIdType=panoDevice; panoramaId_expiry=1705885852367; _au_last_seen_pixels=eyJhcG4iOjE3MDU3OTk0NTYsInR0ZCI6MTcwNTc5OTQ1NiwicHViIjoxNzA1Nzk5NDU2LCJydWIiOjE3MDU3OTk0NTYsInRhcGFkIjoxNzA1Nzk5NDU2LCJhZHgiOjE3MDU3OTk0NTYsImdvbyI6MTcwNTc5OTQ1NiwiY29sb3NzdXMiOjE3MDU3OTk5NTAsImltcHIiOjE3MDU3OTk5NTAsImFtbyI6MTcwNTgwMDAwMywicHBudCI6MTcwNTc5OTk1MCwiaW5kZXgiOjE3MDU3OTk5NTAsIm9wZW54IjoxNzA1Nzk5OTUwLCJiZWVzIjoxNzA1Nzk5NDU2LCJ1bnJ1bHkiOjE3MDU3OTk5NTAsInRhYm9vbGEiOjE3MDU3OTk5NTAsInNtYXJ0IjoxNzA1Nzk5OTUwLCJzb24iOjE3MDU3OTk0NTYsImFkbyI6MTcwNTc5OTk1MH0%3D; _ga_TPXF8L10NG=GS1.1.1705800312.1.0.1705800371.1.0.0; _ga_E3TLKYMMWW=GS1.1.1705800312.1.0.1705800371.1.0.0; cto_bidid=lfrN5F9PZTVoY0JLdVVUcmM3R3dDNzZhRlpVWFlpdGw4Z3daeDJ4VnVZNmtoRkRVUDMxSzVEJTJCekRDeFV4N1prVlZicTJpWCUyQlR1cjdwTjh6bkJIc01OYnFwZTA0Y1lxVVJkUkJsZTROY0Rua29ZWER0RUszczlJN2NjRTFxSFVwOTRIZXcwOSUyRnZRRXFzUnBOUk5XV0tnbXZXdnclM0QlM0Q; AMP_TOKEN=%24NOT_FOUND; __eoi=ID=124eb18beb3df141:T=1705712731:RT=1705807388:S=AA-AfjaRtafWn5kWVk6juUuxDLvj; __AP_SESSION__=949c289a-a17c-4bde-8ce3-851638610cca; __gads=ID=cad3044fb287b1da:T=1705550574:RT=1705807409:S=ALNI_MabYLXmYFjvgeULP-AHAwAZCoje2w; __gpi=UID=00000ce9d38f398b:T=1705550574:RT=1705807409:S=ALNI_Mb8PEVkEh5rZV58S2Z_3J0tNDIp_Q; _ga_7THXRBK2CK=GS1.1.1705807384.9.1.1705807427.17.0.0; _ga=GA1.1.102305793.1705550574; _ga_NEBRGBLTFZ=GS1.1.1705807384.9.1.1705807427.17.0.0; FCNEC=%5B%5B%22AKsRol9gOsXpHVZN743ETSdup7EdZKes4szA3loe9ODfqAPwTICKK7Apm7fEmVpsIgxscCgkF2gjkUGzCUOMhwMc75PjvFPgt8xsb27xLJIQN1J-d2VDxCpECwaPJ9UOKWF3P9e9mftCl2lETZR_tFHLfwEoUCB26A%3D%3D%22%5D%5D; cto_bundle=i5Whf18waG9qRTlTQ09jd1ZGYWpXZ28zTmJmc3pDNFgxOWdWU01jNjJmMHFYN3daSnlzTHRFM0VYd1o4b2dYcTVuYVJ4WE5uSiUyQnNJYjB0OXBoSlFkbzAlMkJHbWpkcmlEcEIwRzc5aG82T016dGdBMDJkNHlOMDdSY213TExnNzdociUyQnpMbVZCZHh2YlA3cEx4TlU2JTJGVEclMkZvWGNlNyUyRlBXJTJGY2x2dlg0a25rdDlSNWJNaG5LWnZEbVA3STlPMGVoRTFaQ3RkVA',
            'referer': 'https://udn.com/news/breaknews/1/5',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }

        params = {
            'page': i,
            'id': '',
            'channelId': '1',
            'cate_id': '5',
            'type': 'breaknews',
            'totalRecNo': '102',
        }

        response = requests.get('https://udn.com/api/more', params=params, cookies=cookies, headers=headers)
        response.close()
        cleaned_text = response.text.replace('\/', '/')
        try:
            text = json.loads(
            rf'{cleaned_text}'.encode().decode('unicode_escape').encode('utf-8').decode('utf-8'))
        except:
            pass
        udnlist = text['lists']
        for news in udnlist:
            headline = news['title']
            body = news['paragraph']
            time = news['time']['date']
            url = f"https://udn.com{news['titleLink']}"
            newdict = {'headline': headline, 'body': body, 'time': time[5:], 'source': 'UDN',
                       'url': url}
            if newdict not in newslisttempt:
                newslisttempt.append(newdict)
        
        
getlist = UDN()
print(getlist)
exit()
print("初数据获取成功")
oldlist = getlist
wordslist = ["China", "Beijing", "Chinese", "Taiwan", "Taiwanese", "US-China", "China-US", "Xi", "China’s",
             "Shanghai", "Hong Kong", "Macau"]

i = 1
while 1 + 1 == 2:
    random_num = random.uniform(60, 62)
    random_num = float(str(random_num)[:3])
    print(f"HK01第{i}次刷新完成，下次刷新将在{random_num}后进行。")
    sleep(random_num)
    getlist = UDN()
    i = i + 1
    difference = [item for item in getlist if item not in oldlist]
    oldlist = getlist
    if len(difference) != 0:
        for item in difference:
            hookheadline = item['headline']
            hookbody = item['body']
            hooktime = item['time']
            hooksource = item['source']
            hookurl = item['url']
            hookdesc = hookheadline + hookbody
            given_time = datetime.strptime(f"2024-{hooktime}", "%Y-%m-%d %H:%M")
            current_time = datetime.now()
            time_difference = current_time - given_time
            if abs(time_difference) <= timedelta(minutes=30):
                webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/e73c2152-d369-47ce-bed3-dc91122448b6'
                hookdata = {
                    "msg_type": "post",
                    "content": {
                        "post": {
                            "zh-CN": {
                                "title": hookheadline,
                                "content": [
                                    [
                                        {
                                            "tag": "text",
                                            "text": f"\n{hooktime}\n{hookbody}\n "
                                        },
                                        {
                                            "tag": "a",
                                            "text": "点击查看",
                                            "href": hookurl
                                        }
                                    ]
                                ]
                            }
                        }
                    }
                }

                response = requests.post(webhook_url, json=hookdata)
                if response.status_code == 200:
                    print('消息已成功发送至 webhook！')
                else:
                    print('发送消息至 webhook 时出错：', response.status_code)

