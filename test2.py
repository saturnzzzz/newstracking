import requests, json, traceback
import random, pywebio, csv
from datetime import datetime, timedelta
from hashlib import md5
import zhconv
import socket
from bs4 import BeautifulSoup
from time import sleep

newslisttempt = []


def time_transfer(time):
    timeafter = time.split('.')[0].split('Z')[0]
    input_time = datetime.strptime(timeafter, "%Y-%m-%dT%H:%M:%S")
    beijing_time = input_time + timedelta(hours=8)
    beijing_time_str = beijing_time.strftime("%m-%d %H:%M")
    return beijing_time_str


def translate(sentence):
    return ""


def timestampnow():
    current_time = datetime.now()
    return int(current_time.timestamp())


def timestampten(timestamp):
    return datetime.fromtimestamp(timestamp)


def timestamp_to_datetime(timestamp):
    timestamp = int(timestamp) / 1000  # 将毫秒转换为秒
    datetime_obj = datetime.fromtimestamp(timestamp)
    return datetime_obj


def timediff(timestr):
    now = str(datetime.now())[5:16]
    mindiff = int(now[6:8]) * 60 + int(now[9:]) - int(timestr[6:8]) * 60 - int(timestr[9:11])
    daydiff = int(now[4:6]) - int(timestr[4:6])
    if now[:6] != timestr[:6]:
        mindiff = 1440 * daydiff + mindiff
    if 0 <= mindiff < 60:
        return f"{mindiff}分"
    else:
        if 60 <= mindiff < 1440:
            for i in range(1, 25):
                if mindiff in range(60 * i, 60 * (i + 1)):
                    return f"{i}~{i + 1}小时"
        else:
            return f"{daydiff}天"


def Reuters():
    i = 0
    while i <= 3:
        try:
            cookies = {
                'cleared-onetrust-cookies': 'Thu, 17 Feb 2022 19:17:07 GMT',
                '_gcl_au': '1.1.949581699.1705734493',
                'usprivacy': '1---',
                '_sp_duid': 'd9cd5fed-4409-47ec-abd9-028fbc6330f1',
                '_cb': 'PzFYrDajo8rCcDi5q',
                'permutive-id': '180d412f-9344-45c4-8e00-2a4411ecd1a8',
                '_fbp': 'fb.1.1705734500985.860092731',
                'cookie': '9d130f9c-89f7-4637-95d6-a45cce46e9f6',
                'cookie_cst': 'zix7LPQsHA%3D%3D',
                '_lr_env_src_ats': 'false',
                'ajs_anonymous_id': '38d9d118-b22c-46f0-9c0a-56653e708c4e',
                '__qca': 'P0-205036969-1705734505909',
                '_cc_id': 'e125a6f346e82b118fd689e6b19ef377',
                'ajs_user_id': '10ae2677-7f1b-43c1-b73f-1082076e255d',
                'OneTrustWPCCPAGoogleOptOut': 'false',
                'cnx_userId': 'dc2dfa5c62184975a154392dcd2fd88e',
                '_gid': 'GA1.2.250088903.1706748234',
                '_lr_geo_location_state': '',
                '_lr_geo_location': 'HK',
                '_awl': '2.1706869329.5-e95c2a0b4ff9d3041b0f61daebc61383-6763652d617369612d6561737431-0',
                'ABTasty': 'uid=c4cqsea82t5khz6v&fst=1705740501946&pst=-1&cst=1705740501946&ns=1&pvt=1&pvis=1&th=',
                'sophiTagid.23dd': 'd9cd5fed-4409-47ec-abd9-028fbc6330f1.1705734494.23.1706869408.1706837991.08730edd-954b-4323-a57c-b51341b6eba8',
                '_ga': 'GA1.1.1230985263.1705734503',
                'datadome': 'XUW1e3Bi0SVt1MCJjKMztzVZCxP_I4GT2cgcNoo55H7EU65qnyJ8QV0rtcHyfB8g9AI~0~baf8CYTO~xJFLsNyGJAx9RtqcNEZ2Lcfvz3Mm7vMTV2ACBq4~6JM7KkOgP',
                'cto_bidid': 'HEQZAV9zbDhLJTJGTVJmM2hXTmgzZ3lHY3E1QnhMVVREY0hFZUZqWDFCOGtWV1BUR01VMnNpdzJxWjloMkFQTU5VdVBmSE82b3NpYmQlMkYyTGFGeWVwM2xkR0RCb3FWbnBXSGVjVDl2UlZwMkFRTkQlMkJONXRZQ2N0RFFnV3hZZkE5VEdBVmJTd3lndjBSaWwwNnpSbjA3TFNLTmtKc2clM0QlM0Q',
                'cto_bundle': 'zmGHC19xa0FXWiUyRkZ0dmt2dXZQM2JpdUJWZkF0Wm8lMkJncDROR2Nma2hwUnElMkZhbkVVSFFab0d6ellnZjdTcXMwWHYxT2ZJck4zdWxUOXlmaTF2T25aNWhUVm5aUkV3TWNwUlp1WTR5TUE1SiUyRmY4U0hhbmFpWUhQdkNQMjNwTUMwaW8xMDd0cVBmaVdORVNJQTFvSUxVT3ZyZXg3bkdyTUFFQW5FUnZjNG03aWhHNmV2WnU4bWJ1WUN2WmhNOWpEeGg0cE1DOWlGNlcxWFVDQXFhd0FZZ0htZE1sJTJCQSUzRCUzRA',
                '__gads': 'ID=ad6420261630ade0:T=1705734503:RT=1706875208:S=ALNI_MaURQujgmTqA3da2wAIWqZ74Y4hLA',
                '__gpi': 'UID=00000cebab530e37:T=1705734503:RT=1706875208:S=ALNI_MZ9zRGTzphUEZ-xSxN-xOcAd-FFVw',
                '__eoi': 'ID=19c301312f12993b:T=1705734503:RT=1706875208:S=AA-AfjYA-yZKzMBQmrsBS3uVAz_I',
                '_ga_WBSR7WLTGD': 'GS1.1.1706875159.25.0.1706875219.60.0.0',
                'RT': '"z=1&dm=reuters.com&si=oev64ski0mf&ss=ls4hxa0i&sl=0&tt=0"',
                'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Feb+02+2024+20%3A00%3A27+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=636401b8-659c-4532-8eef-65531b09241d&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2CSPD_BG%3A1%2C2%3A1%2C4%3A1&AwaitingReconsent=false&geolocation=HK%3B',
                'OptanonAlertBoxClosed': '2024-02-02T12:00:27.138Z',
                'reuters-geo': '{"country":"HK", "region":"-"}',
                '_chartbeat2': '.1705734497230.1706875231247.11010011100011.B7paZ1CtWnPbC9JSyJCPV434CldNPS.1',
                '_cb_svref': 'https%3A%2F%2Fwww.reuters.com%2Fworld%2F',
                '_dd_s': 'rum=0&expire=1706876131287',
            }

            headers = {
                'authority': 'www.reuters.com',
                'accept': '*/*',
                'accept-language': 'zh-CN,zh;q=0.9',
                # 'cookie': 'cleared-onetrust-cookies=Thu, 17 Feb 2022 19:17:07 GMT; _gcl_au=1.1.949581699.1705734493; usprivacy=1---; _sp_duid=d9cd5fed-4409-47ec-abd9-028fbc6330f1; _cb=PzFYrDajo8rCcDi5q; permutive-id=180d412f-9344-45c4-8e00-2a4411ecd1a8; _fbp=fb.1.1705734500985.860092731; cookie=9d130f9c-89f7-4637-95d6-a45cce46e9f6; cookie_cst=zix7LPQsHA%3D%3D; _lr_env_src_ats=false; ajs_anonymous_id=38d9d118-b22c-46f0-9c0a-56653e708c4e; __qca=P0-205036969-1705734505909; _cc_id=e125a6f346e82b118fd689e6b19ef377; ajs_user_id=10ae2677-7f1b-43c1-b73f-1082076e255d; OneTrustWPCCPAGoogleOptOut=false; cnx_userId=dc2dfa5c62184975a154392dcd2fd88e; _gid=GA1.2.250088903.1706748234; _lr_geo_location_state=; _lr_geo_location=HK; _awl=2.1706869329.5-e95c2a0b4ff9d3041b0f61daebc61383-6763652d617369612d6561737431-0; ABTasty=uid=c4cqsea82t5khz6v&fst=1705740501946&pst=-1&cst=1705740501946&ns=1&pvt=1&pvis=1&th=; sophiTagid.23dd=d9cd5fed-4409-47ec-abd9-028fbc6330f1.1705734494.23.1706869408.1706837991.08730edd-954b-4323-a57c-b51341b6eba8; _ga=GA1.1.1230985263.1705734503; datadome=XUW1e3Bi0SVt1MCJjKMztzVZCxP_I4GT2cgcNoo55H7EU65qnyJ8QV0rtcHyfB8g9AI~0~baf8CYTO~xJFLsNyGJAx9RtqcNEZ2Lcfvz3Mm7vMTV2ACBq4~6JM7KkOgP; cto_bidid=HEQZAV9zbDhLJTJGTVJmM2hXTmgzZ3lHY3E1QnhMVVREY0hFZUZqWDFCOGtWV1BUR01VMnNpdzJxWjloMkFQTU5VdVBmSE82b3NpYmQlMkYyTGFGeWVwM2xkR0RCb3FWbnBXSGVjVDl2UlZwMkFRTkQlMkJONXRZQ2N0RFFnV3hZZkE5VEdBVmJTd3lndjBSaWwwNnpSbjA3TFNLTmtKc2clM0QlM0Q; cto_bundle=zmGHC19xa0FXWiUyRkZ0dmt2dXZQM2JpdUJWZkF0Wm8lMkJncDROR2Nma2hwUnElMkZhbkVVSFFab0d6ellnZjdTcXMwWHYxT2ZJck4zdWxUOXlmaTF2T25aNWhUVm5aUkV3TWNwUlp1WTR5TUE1SiUyRmY4U0hhbmFpWUhQdkNQMjNwTUMwaW8xMDd0cVBmaVdORVNJQTFvSUxVT3ZyZXg3bkdyTUFFQW5FUnZjNG03aWhHNmV2WnU4bWJ1WUN2WmhNOWpEeGg0cE1DOWlGNlcxWFVDQXFhd0FZZ0htZE1sJTJCQSUzRCUzRA; __gads=ID=ad6420261630ade0:T=1705734503:RT=1706875208:S=ALNI_MaURQujgmTqA3da2wAIWqZ74Y4hLA; __gpi=UID=00000cebab530e37:T=1705734503:RT=1706875208:S=ALNI_MZ9zRGTzphUEZ-xSxN-xOcAd-FFVw; __eoi=ID=19c301312f12993b:T=1705734503:RT=1706875208:S=AA-AfjYA-yZKzMBQmrsBS3uVAz_I; _ga_WBSR7WLTGD=GS1.1.1706875159.25.0.1706875219.60.0.0; RT="z=1&dm=reuters.com&si=oev64ski0mf&ss=ls4hxa0i&sl=0&tt=0"; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+02+2024+20%3A00%3A27+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=636401b8-659c-4532-8eef-65531b09241d&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2CSPD_BG%3A1%2C2%3A1%2C4%3A1&AwaitingReconsent=false&geolocation=HK%3B; OptanonAlertBoxClosed=2024-02-02T12:00:27.138Z; reuters-geo={"country":"HK", "region":"-"}; _chartbeat2=.1705734497230.1706875231247.11010011100011.B7paZ1CtWnPbC9JSyJCPV434CldNPS.1; _cb_svref=https%3A%2F%2Fwww.reuters.com%2Fworld%2F; _dd_s=rum=0&expire=1706876131287',
                'referer': 'https://www.reuters.com/world/',
                'sec-ch-device-memory': '8',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-arch': '"arm"',
                'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.85", "Chromium";v="121.0.6167.85"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            }

            params = {
                'query': '{"arc-site":"reuters","called_from_a_component":true,"fetch_type":"sophi","offset":0,"section_id":"/world/","size":50,"sophi_page":"world","sophi_widget":"topic","website":"reuters"}',
                'd': '175',
                '_website': 'reuters',
            }

            response = requests.get(
                'https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22sophi%22%2C%22offset%22%3A0%2C%22section_id%22%3A%22%2Fworld%2F%22%2C%22size%22%3A50%2C%22sophi_page%22%3A%22world%22%2C%22sophi_widget%22%3A%22topic%22%2C%22website%22%3A%22reuters%22%7D&d=179&_website=reuters'
            )
            response.close()
            reuterslist = json.loads(response.text)['result']['articles']
            i = 4
        except:
            i = i + 1
            random_num = random.uniform(0.5, 3)
            random_num = float(str(random_num)[:3])
            sleep(random_num)


    for news in reuterslist:
        headline = news['title']
        body = news['description']
        time = news['updated_time']
        url = f"https://www.reuters.com{news['canonical_url']}"
        date_object = datetime.strptime(time[:10], "%Y-%m-%d")
        current_date = datetime.now()
        time_difference = current_date - date_object
        if int(str(time_difference.days)) <= 2:
            newdict = {'headline': headline, 'body': body, 'time': time_transfer(time), 'source': 'Reuters', 'url': url}
            if newdict not in newslisttempt:
                newslisttempt.append(newdict)
        else:
            continue


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
        text = json.loads(
            rf'{response.text}'.encode().decode('unicode_escape').encode('utf-8').decode('utf-8').replace('\/', '/'))
        udnlist = text['lists']
        for news in udnlist:
            headline = news['title']
            body = news['paragraph']
            time = news['time']['date']
            url = f"https://udn.com{news['titleLink']}"
            date_object = datetime.strptime(time[:10], "%Y-%m-%d")
            current_date = datetime.now()
            time_difference = current_date - date_object
            if int(str(time_difference.days)) <= 2:
                newdict = {'headline': headline, 'body': body, 'time': time[5:], 'source': 'UDN',
                           'url': url}
                if newdict not in newslisttempt:
                    newslisttempt.append(newdict)
            else:
                continue


def huanqiu():
    cookies = {
        'Hm_lvt_1fc983b4c305d209e7e05d96e713939f': '1705634057,1705710660',
        'Hm_lpvt_1fc983b4c305d209e7e05d96e713939f': '1705809125',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'Hm_lvt_1fc983b4c305d209e7e05d96e713939f=1705634057,1705710660; Hm_lpvt_1fc983b4c305d209e7e05d96e713939f=1705809125',
        'If-Modified-Since': 'Sun, 21 Jan 2024 02:51:16 GMT',
        'Referer': 'https://world.huanqiu.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.get(
        'https://world.huanqiu.com/api/list?node=%22/e3pmh22ph/e3pmh2398%22,%22/e3pmh22ph/e3pmh26vv%22,%22/e3pmh22ph/e3pn6efsl%22,%22/e3pmh22ph/efp8fqe21%22&offset=0&limit=24',
        cookies=cookies,
        headers=headers,
    )
    response.close()
    huanqiulist = json.loads(response.text)['list']

    for news in huanqiulist:
        try:
            headline = news['title']
            body = news['summary']
            time = str(timestamp_to_datetime(news['xtime']))[:19]
            url = f"https://world.huanqiu.com/article/{news['aid']}"
            date_object = datetime.strptime(time[:10], "%Y-%m-%d")
            current_date = datetime.now()
            time_difference = current_date - date_object
            if int(str(time_difference.days)) <= 2:
                newdict = {'headline': headline, 'body': body, 'time': time[5:], 'source': '环球网',
                           'url': url}
                if newdict not in newslisttempt:
                    newslisttempt.append(newdict)
            else:
                continue
        except:
            pass


def hk():
    headers = {
        'authority': 'web-data.api.hk01.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://www.hk01.com',
        'referer': 'https://www.hk01.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    params = {
        'limit': '50',
        'bucketId': '00000',
    }

    response = requests.get('https://web-data.api.hk01.com/v2/feed/category/19', params=params, headers=headers)
    # text = json.loads(rf'{response.text}'.encode().decode('unicode_escape').encode('utf-8').decode('utf-8'))
    response.close()
    hklist = json.loads(response.text.replace(r'\u3000', ' '))['items']

    for news in hklist:
        headline = news['data']['title']
        body = news['data']['description']
        time = str(timestampten(news['data']['publishTime']))
        url = news['data']['publishUrl']
        date_object = datetime.strptime(time[:10], "%Y-%m-%d")
        current_date = datetime.now()
        time_difference = current_date - date_object
        if int(str(time_difference.days)) <= 2:
            newdict = {'headline': headline, 'body': body, 'time': time[5:], 'source': 'HK01', 'url': url}
            if newdict not in newslisttempt:
                newslisttempt.append(newdict)
        else:
            continue


def cna():
    import requests, json

    cookies = {
        '_gid': 'GA1.3.1378951023.1705817773',
        '_gat_UA-6826760-1': '1',
        'CnaCloseLanguage': '1',
        '_fbp': 'fb.2.1705817773888.1415441624',
        '_cc_id': 'e125a6f346e82b118fd689e6b19ef377',
        'panoramaId_expiry': '1705904174539',
        'panoramaId': '400237e71fa49790215edd01fb49a9fb927a425a3c4d8c2ef525d7d61a86bddb',
        'panoramaIdType': 'panoDevice',
        '__gads': 'ID=b9094778582a224b:T=1705817774:RT=1705817774:S=ALNI_MYk8z8rtow6KHzDrIlST9gvKqbRHw',
        '__gpi': 'UID=00000cec3c0c601d:T=1705817774:RT=1705817774:S=ALNI_Ma7Wik9nChj1krGzOXZMXeF4u5cvQ',
        '__eoi': 'ID=b1aecc1a0b8d1f01:T=1705817774:RT=1705817774:S=AA-AfjaU_SQ3suydjHgxqwgDl3i1',
        '_ga': 'GA1.3.1200241492.1705817773',
        '_ga_M3FRFG0581': 'GS1.1.1705817772.1.1.1705817813.19.0.0',
        'FCNEC': '%5B%5B%22AKsRol-266rBQcjNPOii5Vf7xj9iTxzPtvuonu1MY2MD_mM95je7RtCujuS8S2yjCQ0wop5M7rsASRMIAin1QFEltI65GNvT_aexkX6Hm2tQm4zCbcEAdkspxfyh47w_d6AXGe7JUSeXbKzdAirvoHW7Ro9VkNCPjQ%3D%3D%22%5D%5D',
    }

    headers = {
        'authority': 'www.cna.com.tw',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.3.1378951023.1705817773; _gat_UA-6826760-1=1; CnaCloseLanguage=1; _fbp=fb.2.1705817773888.1415441624; _cc_id=e125a6f346e82b118fd689e6b19ef377; panoramaId_expiry=1705904174539; panoramaId=400237e71fa49790215edd01fb49a9fb927a425a3c4d8c2ef525d7d61a86bddb; panoramaIdType=panoDevice; __gads=ID=b9094778582a224b:T=1705817774:RT=1705817774:S=ALNI_MYk8z8rtow6KHzDrIlST9gvKqbRHw; __gpi=UID=00000cec3c0c601d:T=1705817774:RT=1705817774:S=ALNI_Ma7Wik9nChj1krGzOXZMXeF4u5cvQ; __eoi=ID=b1aecc1a0b8d1f01:T=1705817774:RT=1705817774:S=AA-AfjaU_SQ3suydjHgxqwgDl3i1; _ga=GA1.3.1200241492.1705817773; _ga_M3FRFG0581=GS1.1.1705817772.1.1.1705817813.19.0.0; FCNEC=%5B%5B%22AKsRol-266rBQcjNPOii5Vf7xj9iTxzPtvuonu1MY2MD_mM95je7RtCujuS8S2yjCQ0wop5M7rsASRMIAin1QFEltI65GNvT_aexkX6Hm2tQm4zCbcEAdkspxfyh47w_d6AXGe7JUSeXbKzdAirvoHW7Ro9VkNCPjQ%3D%3D%22%5D%5D',
        'origin': 'https://www.cna.com.tw',
        'referer': 'https://www.cna.com.tw/list/aopl.aspx',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'action': '0',
        'category': 'aopl',
        'pagesize': '50',
        'pageidx': 1,
    }

    response = requests.post('https://www.cna.com.tw/cna2018api/api/WNewsList', cookies=cookies, headers=headers,
                             json=json_data)
    response.close()
    cnalist = json.loads(response.text)['ResultData']['Items']
    for news in cnalist:
        headline = news['HeadLine']
        time = news["CreateTime"].replace("/", "-")
        url = news['PageUrl']
        body = ''
        date_object = datetime.strptime(time[:10], "%Y-%m-%d")
        current_date = datetime.now()
        time_difference = current_date - date_object
        if int(str(time_difference.days)) <= 2:
            newdict = {'headline': headline, 'body': body, 'time': time[5:], 'source': '中央社', 'url': url}
            if newdict not in newslisttempt:
                newslisttempt.append(newdict)
        else:
            continue


def xinhua():
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://www.news.cn/world/jsxw/index.html',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    response = requests.get('http://www.news.cn/world/jsxw/ds_29089f6bdec84f03b12804d9fe4897be.json', headers=headers,
                            verify=False)
    response.close()
    response.encoding = 'utf-8'  # 或 response.encoding = 'gbk'
    source_code = json.loads(response.text)
    xinhualist = source_code['datasource']
    for news in xinhualist:
        headline = news['title']
        body = news['summary']
        time = news['publishTime']
        url = f"https://www.news.cn{news['publishUrl']}"
        date_object = datetime.strptime(time[:10], "%Y-%m-%d")
        current_date = datetime.now()
        time_difference = current_date - date_object
        if int(str(time_difference.days)) <= 2:
            newdict = {'headline': headline, 'body': body, 'time': time[5:], 'source': '新华网',
                       'url': url}
            if newdict not in newslisttempt:
                newslisttempt.append(newdict)
        else:
            continue


def aljazeera():
    cookies = {
        '_cb': 'R6hx0DkiQAnRvl4V',
        '_fbp': 'fb.1.1706750933838.1467210190',
        '__qca': 'P0-340311878-1706750930629',
        '_gid': 'GA1.2.1883952847.1706922633',
        'cookie': 'd9dbad7b-aace-4deb-a9e4-2cdb7e90a574',
        'cookie_cst': 'zix7LPQsHA%3D%3D',
        '_au_1d': 'AU1D-0100-001706923493-HRX47Q0Z-JBDZ',
        'cnx_userId': '8152b379a395432aa591422fd0326f5a',
        '_au_last_seen_pixels': 'eyJhcG4iOjE3MDY5MjM0OTMsInR0ZCI6MTcwNjkyMzQ5MywicHViIjoxNzA2OTIzNDkzLCJydWIiOjE3MDY5MjM0OTMsInRhcGFkIjoxNzA2OTIzNDkzLCJhZHgiOjE3MDY5MjM0OTMsImdvbyI6MTcwNjkyMzQ5MywidGFib29sYSI6MTcwNjkyMzQ5MywiaW5kZXgiOjE3MDY5MjM0OTMsInVucnVseSI6MTcwNjkyMzQ5MywiYWRvIjoxNzA2OTIzNTU0LCJpbXByIjoxNzA2OTIzNTU0LCJiZWVzIjoxNzA2OTIzNTU0LCJwcG50IjoxNzA2OTIzNTU0LCJzbWFydCI6MTcwNjkyMzU1NCwib3BlbngiOjE3MDY5MjM1NTQsInNvbiI6MTcwNjkyMzU1NCwiYW1vIjoxNzA2OTIzNTU0LCJjb2xvc3N1cyI6MTcwNjkyMzU1NH0%3D',
        '_splunk_rum_sid': '%7B%22id%22%3A%2234687cfd1c6acf4b2475690f6dae0cd4%22%2C%22startTime%22%3A1706968591114%7D',
        '_cb_svref': 'external',
        '_ga_XN9JB9Q0M1': 'GS1.1.1706968592.8.1.1706968593.0.0.0',
        '_chartbeat2': '.1706750925987.1706968593254.101.-skZfDDWKa4BiMi16DLbicIBIXpqw.2',
        'AMP_9e2bdeb55f': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI4YWIxZTcyMC00ZjM4LTQ3NjAtOGM2Yy0wZGUxZGJjZWJjMDMlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzA2OTY4NTkxNzAyJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwNjk2ODU5MzI2MSUyQyUyMmxhc3RFdmVudElkJTIyJTNBNDglN0Q=',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Feb+03+2024+21%3A56%3A33+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=67a96fd9-dd27-4a32-9917-a37b5fba2ff4&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0007%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&AwaitingReconsent=false',
        '_ga': 'GA1.2.1801407487.1706750928',
        '__gads': 'ID=8291cf8189a1a20e:T=1706923553:RT=1706968607:S=ALNI_MbrZkLZX9vgIaUGewYrROTmqHKeLg',
        '__gpi': 'UID=00000cf72efb6be6:T=1706923553:RT=1706968607:S=ALNI_MZuaze_PqHW-SRNzXO3jE0TPQPJUg',
        '__eoi': 'ID=892c77cf4d8c06ee:T=1706923553:RT=1706968607:S=AA-AfjbmE0rMkU5QjN0pyQS0L4hi',
        'cto_bundle': 'GDaab19WWGtKRld0UXRLQ2slMkJpVWExcyUyRktuTjI1R1hRcXhwMm05SDEza3AlMkZueFF2d0N2c3d0UVRETUJTY3N6cGZRbU4yeGkzQ05HJTJCWFdWSEE0SVc0QjYySWxPbmdWek1BaiUyQmx3U0VieU13V0hNU1VnVEhoMjRqamphNWdPb1FZNFcyY0JWV0NEa3YzaXBPR21iaFdNZUZSN2dPeDVYQjZxVmozRFlvYTh2VjAxNVp0VSUyRnRQYXZPRzdaQ2gxWmxnMlhlZ0MwZUhIeHh6S0dCWHJWNllkd0plZ3VnJTNEJTNE',
        'cto_bidid': 'oSEFBV9VMnZDenlTZVlOYlQ5Z3lvQmJiR05HTmdKT2tramlyJTJCaVVKazV1d2dZNWE2aDR4WDQlMkZUNXc2MkxRTm5Jc3poWlVDY0NLbjhETzQ0b2NyOHFyRXlONjYlMkZTaGpqVUZtQko3ZnA3N0dZaGxPJTJGRGYxNmRsTzZBdHFWdEJHbGpoaHpHMmlBZHE1VVl5Q0N6VkRqNDU2Zkc1ZyUzRCUzRA',
    }

    headers = {
        'authority': 'www.aljazeera.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_cb=R6hx0DkiQAnRvl4V; _fbp=fb.1.1706750933838.1467210190; __qca=P0-340311878-1706750930629; _gid=GA1.2.1883952847.1706922633; cookie=d9dbad7b-aace-4deb-a9e4-2cdb7e90a574; cookie_cst=zix7LPQsHA%3D%3D; _au_1d=AU1D-0100-001706923493-HRX47Q0Z-JBDZ; cnx_userId=8152b379a395432aa591422fd0326f5a; _au_last_seen_pixels=eyJhcG4iOjE3MDY5MjM0OTMsInR0ZCI6MTcwNjkyMzQ5MywicHViIjoxNzA2OTIzNDkzLCJydWIiOjE3MDY5MjM0OTMsInRhcGFkIjoxNzA2OTIzNDkzLCJhZHgiOjE3MDY5MjM0OTMsImdvbyI6MTcwNjkyMzQ5MywidGFib29sYSI6MTcwNjkyMzQ5MywiaW5kZXgiOjE3MDY5MjM0OTMsInVucnVseSI6MTcwNjkyMzQ5MywiYWRvIjoxNzA2OTIzNTU0LCJpbXByIjoxNzA2OTIzNTU0LCJiZWVzIjoxNzA2OTIzNTU0LCJwcG50IjoxNzA2OTIzNTU0LCJzbWFydCI6MTcwNjkyMzU1NCwib3BlbngiOjE3MDY5MjM1NTQsInNvbiI6MTcwNjkyMzU1NCwiYW1vIjoxNzA2OTIzNTU0LCJjb2xvc3N1cyI6MTcwNjkyMzU1NH0%3D; _splunk_rum_sid=%7B%22id%22%3A%2234687cfd1c6acf4b2475690f6dae0cd4%22%2C%22startTime%22%3A1706968591114%7D; _cb_svref=external; _ga_XN9JB9Q0M1=GS1.1.1706968592.8.1.1706968593.0.0.0; _chartbeat2=.1706750925987.1706968593254.101.-skZfDDWKa4BiMi16DLbicIBIXpqw.2; AMP_9e2bdeb55f=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI4YWIxZTcyMC00ZjM4LTQ3NjAtOGM2Yy0wZGUxZGJjZWJjMDMlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzA2OTY4NTkxNzAyJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwNjk2ODU5MzI2MSUyQyUyMmxhc3RFdmVudElkJTIyJTNBNDglN0Q=; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+03+2024+21%3A56%3A33+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=67a96fd9-dd27-4a32-9917-a37b5fba2ff4&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0007%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&AwaitingReconsent=false; _ga=GA1.2.1801407487.1706750928; __gads=ID=8291cf8189a1a20e:T=1706923553:RT=1706968607:S=ALNI_MbrZkLZX9vgIaUGewYrROTmqHKeLg; __gpi=UID=00000cf72efb6be6:T=1706923553:RT=1706968607:S=ALNI_MZuaze_PqHW-SRNzXO3jE0TPQPJUg; __eoi=ID=892c77cf4d8c06ee:T=1706923553:RT=1706968607:S=AA-AfjbmE0rMkU5QjN0pyQS0L4hi; cto_bundle=GDaab19WWGtKRld0UXRLQ2slMkJpVWExcyUyRktuTjI1R1hRcXhwMm05SDEza3AlMkZueFF2d0N2c3d0UVRETUJTY3N6cGZRbU4yeGkzQ05HJTJCWFdWSEE0SVc0QjYySWxPbmdWek1BaiUyQmx3U0VieU13V0hNU1VnVEhoMjRqamphNWdPb1FZNFcyY0JWV0NEa3YzaXBPR21iaFdNZUZSN2dPeDVYQjZxVmozRFlvYTh2VjAxNVp0VSUyRnRQYXZPRzdaQ2gxWmxnMlhlZ0MwZUhIeHh6S0dCWHJWNllkd0plZ3VnJTNEJTNE; cto_bidid=oSEFBV9VMnZDenlTZVlOYlQ5Z3lvQmJiR05HTmdKT2tramlyJTJCaVVKazV1d2dZNWE2aDR4WDQlMkZUNXc2MkxRTm5Jc3poWlVDY0NLbjhETzQ0b2NyOHFyRXlONjYlMkZTaGpqVUZtQko3ZnA3N0dZaGxPJTJGRGYxNmRsTzZBdHFWdEJHbGpoaHpHMmlBZHE1VVl5Q0N6VkRqNDU2Zkc1ZyUzRCUzRA',
        'original-domain': 'www.aljazeera.com',
        'referer': 'https://www.aljazeera.com/news/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'wp-site': 'aje',
    }

    params = {
        'wp-site': 'aje',
        'operationName': 'ArchipelagoAjeSectionPostsQuery',
        'variables': '{"category":"news","categoryType":"categories","postTypes":["blog","episode","opinion","post","video","external-article","gallery","podcast","longform","liveblog"],"quantity":30,"offset":0}',
        'extensions': '{}',
    }

    response = requests.get('https://www.aljazeera.com/graphql', params=params, cookies=cookies, headers=headers)
    aljazeeralist = json.loads(response.text)['data']['articles']
    response.close()

    for news in aljazeeralist:
        headline = news['title']
        body = news['excerpt']
        time = news['date']
        url = f"https://www.aljazeera.com/{news['link']}"
        date_object = datetime.strptime(time[:10], "%Y-%m-%d")
        current_date = datetime.now()
        time_difference = current_date - date_object
        if int(str(time_difference.days)) <= 2:
            newdict = {'headline': headline, 'body': body, 'time': time_transfer(time), 'source': 'AlJazeera',
                       'url': url}
            if newdict not in newslisttempt:
                newslisttempt.append(newdict)
        else:
            continue


def sputnik():
    cookies = {
        'ab_emoji_test': 'c',
        'ab_subscriber': 'a',
        'sputnik_cn': '65acbbacb7c8b81c64080333',
        'Hm_lvt_a194ecb55641188e5cbf02d633e406cb': '1705819056',
        '_ym_uid': '170581905852188968',
        '_ym_d': '1705819058',
        '_gid': 'GA1.2.2136934168.1705819058',
        '_pk_ref.sputnik_cn.8417': '%5B%22%22%2C%22%22%2C1705904858%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_ym_isad': '2',
        '_pk_ses.sputnik_cn.8417': '%7B%22depth%22%3A1%7D',
        'Hm_lpvt_a194ecb55641188e5cbf02d633e406cb': '1705904916',
        '_ga': 'GA1.1.845180709.1705819058',
        '_pk_id.sputnik_cn.8417': '4c1eed8f28e52d7d.1705819057.2.1705904916.1705819081.',
        '_ga_LZMMXB5WL7': 'GS1.2.1705904859.2.1.1705904916.0.0.0',
        '_ga_3CRMDN5S1H': 'GS1.1.1705904858.2.1.1705904939.60.0.0',
    }
    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'ab_emoji_test=c; ab_subscriber=a; sputnik_cn=65acbbacb7c8b81c64080333; Hm_lvt_a194ecb55641188e5cbf02d633e406cb=1705819056; _ym_uid=170581905852188968; _ym_d=1705819058; _gid=GA1.2.2136934168.1705819058; _pk_ref.sputnik_cn.8417=%5B%22%22%2C%22%22%2C1705904858%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _ym_isad=2; _pk_ses.sputnik_cn.8417=%7B%22depth%22%3A1%7D; Hm_lpvt_a194ecb55641188e5cbf02d633e406cb=1705904916; _ga=GA1.1.845180709.1705819058; _pk_id.sputnik_cn.8417=4c1eed8f28e52d7d.1705819057.2.1705904916.1705819081.; _ga_LZMMXB5WL7=GS1.2.1705904859.2.1.1705904916.0.0.0; _ga_3CRMDN5S1H=GS1.1.1705904858.2.1.1705904939.60.0.0',
        'Referer': 'https://sputniknews.cn/category_guoji/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    params = {
        'date_start': '20240121',
        'date': datetime.now().strftime('%Y%m%d'),
        'tags[]': 'category_guoji',
    }
    response = requests.get('https://sputniknews.cn/services/tagsearch/', params=params, cookies=cookies,
                            headers=headers)
    response.close()
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extracting news titles, publish time, and links
    news_items = soup.find_all('div', class_='list__item')
    for item in news_items:
        title = item.find('a', class_='list__title').text
        publish_time = item.find('span', class_='date').text
        if publish_time[0:1] == '昨':
            publish_time = publish_time.replace('昨天, ', '')
            publish_time = f"{(datetime.now() - timedelta(days=1)).strftime('%m-%d')} {publish_time}"
        else:
            publish_time = f"{datetime.now().strftime('%m-%d')} {publish_time}"
        link = item.find('a', class_='list__title')['href']
        newdict = {'headline': title, 'body': '', 'time': publish_time,
                   'source': '俄罗斯卫星通讯社',
                   'url': f"https://sputniknews.cn{link}"}
        if newdict not in newslisttempt:
            newslisttempt.append(newdict)

def zaobao():
    headers = {
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.zaobao.com/',
        'x-auth': '07b20a9df7f3c4aafea2a4a647f87111',
        'x-amz-date': '2024-01-26T11:57:11Z',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'pageNo': '1',
        'pageSize': '15',
    }

    response = requests.get('https://www.zaobao.com/more/realtime', params=params, headers=headers)
    zaobaolist = json.loads(response.text)["result"]['4']

    for news in zaobaolist:
        headline = news['title']
        body = news['contentPreview']
        time = news['publicationDate']
        url = f"https://www.zaobao.com/realtime/world{news['url']}"
        date_object = datetime.strptime(time[:10], "%Y-%m-%d")
        current_date = datetime.now()
        time_difference = current_date - date_object
        if int(str(time_difference.days)) <= 2:
            newdict = {'headline': headline, 'body': body, 'time': time[5:], 'source': '联合早报',
                       'url': url}
            if newdict not in newslisttempt:
                newslisttempt.append(newdict)
        else:
            continue

def logourl(source):
    logodict = {
        "UDN": "https://cdn2.downdetector.com/static/uploads/logo/udn.png",
        "Reuters": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Reuters_Logo.svg/2560px-Reuters_Logo.svg.png",
        "HK01": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/HK01_Logo.svg/1200px-HK01_Logo.svg.png",
        "环球网": "https://qc-website.sh1a.qingstor.com/files/2019/08/ed9715bdbbc03761688a3d50513e91fb.jpg",
        "中央社": "https://secure-res.craft.do/v2/DruVuSrkuz3w8PtpCtmXVTjJiEURyBF75LJVHeUXHhqzSoFxd8RPTy2oKqLDLgwJNTj4HRxiqvmgaE9EN53nAruySdM3aTUgLht5c5rvkWu2V1q212Qyn846bn3qonE95daitYawsokETnWgs8KBTx5oXSY25T5RAkwuPzBkcjzeGfgCJvAq49vogmak5pjpFjyUg8mSFrVuq3p7b7aEVYpAxnEeQhAC5D2c6Tn6GaJ1s2wdKDZKYKtCCu2MbZ1behoQpkWm1dCfLPYYd1Qw2JgYiRBk5fFsNyKWwEuC7HGS5KqPz/Image.jpg",
        "新华网": "http://www.news.cn/2023homepro/images/logo.png",
        "AlJazeera": "https://secure-res.craft.do/v2/DruVuSrkuz3w8PtpCtmXVTjJiEURyBF75LJVHeUXHhqzSoFxd8RPTy2oKqLDLgwJNTj4HRxiqvmgaE9EN53nAruySdM3aTUgLht5c5rvkWu2V1q212Qyn846bn3qonE95daitYawsokETnWgs8KBTx5om64HiMU847JscfvB6uL69XrkFYV9UKGD3wDs1ri3xKUjRfMSXSHFQA4VGhcSrc1eoLMrWo6nweWedAX1xEYmRwHDzZfKPNsJRtJPuCA5w9kPAevgJhY1EyhtLcAGir9w9U26LZQhc17RhuUQLWvnsfRDq/Image.jpg",
        "俄罗斯卫星通讯社": "https://user-images.githubusercontent.com/1645233/160103720-7cbc3c8c-6991-452a-a886-2f0869b48a7a.png",
        "联合早报": "https://static.zaobao.com/s3fs-public/2023-09/nlogo.png"
    }
    return logodict[source]

def printnews(item):
    pywebio.output.put_markdown(f'<img src={logourl(item["source"])} height="30">')
    pywebio.output.put_markdown(
        f"<b><font size=5>[{item['headline']}<br>{translate(item['headline'])}]({item['url']})</font></b>")
    pywebio.output.put_markdown(f'''> 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}''')
    pywebio.output.put_text(item['body'])
    pywebio.output.put_text(translate(item['body']))
    pywebio.output.put_markdown("""---""").show()

def lasttime():
    with open('lasttime.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        lasttime = list(reader)

    head = open("head.png", 'rb').read()
    pywebio.output.put_image(head).show()
    pywebio.output.put_markdown("""### 以下展示上次更新""").show()
    pywebio.output.put_buttons(['加载最新'], onclick=[load]).show()

    pywebio.output.put_tabs([
        {'title': '全部', 'content':[pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

<b><font size=5>[{item['headline']}]({item['url']})</font></b>

> 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

{item['body']}

---''') for item in lasttime]},
        {'title': '环球网', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

<b><font size=5>[{item['headline']}]({item['url']})</font></b>

> 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

{item['body']}

---''') for item in lasttime if item['source'] == '环球网']},
        {'title': 'Reuters', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

<b><font size=5>[{item['headline']}]({item['url']})</font></b>

> 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

{item['body']}

---''') for item in lasttime if item['source'] == 'Reuters']},
        {'title': '香港01', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

<b><font size=5>[{item['headline']}]({item['url']})</font></b>

> 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

{item['body']}

---''') for item in lasttime if item['source'] == 'HK01']},
        {'title': '新华网', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

<b><font size=5>[{item['headline']}]({item['url']})</font></b>

> 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

{item['body']}

---''') for item in lasttime if item['source'] == '新华网']},
        {'title': '中央社', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

<b><font size=5>[{item['headline']}]({item['url']})</font></b>

> 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

{item['body']}

---''') for item in lasttime if item['source'] == '中央社']},
        {'title': 'UDN', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

<b><font size=5>[{item['headline']}]({item['url']})</font></b>

> 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

{item['body']}

---''') for item in lasttime if item['source'] == 'UDN']},
        {'title': '俄罗斯卫星通讯社', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

<b><font size=5>[{item['headline']}]({item['url']})</font></b>

> 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

{item['body']}

---''') for item in lasttime if item['source'] == '俄罗斯卫星通讯社']},
        {'title': '半岛电视台', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

<b><font size=5>[{item['headline']}]({item['url']})</font></b>

> 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

{item['body']}

---''') for item in lasttime if item['source'] == 'AlJazeera']},
]).show()

def load():
    pywebio.output.clear()
    head = open("head.png", 'rb').read()
    pywebio.output.put_image(head).show()
    pywebio.output.put_processbar('bar', auto_close=True)
    i = 0
    try:
        UDN()
        i = i + 1
    except:
        print(traceback.print_exc())
        pywebio.output.toast("Error: UDN 加载失败", position='center', color='#2188ff', duration=3)
    pywebio.output.set_processbar('bar', i / 8)
    try:
        Reuters()
        i = i + 1
    except:
        print(traceback.print_exc())
        pywebio.output.toast("Error: Reuters 加载失败", position='center', color='#2188ff', duration=3)
    pywebio.output.set_processbar('bar', i / 8)
    try:
        huanqiu()
        i = i + 1
    except:
        print(traceback.print_exc())
        pywebio.output.toast("Error: 环球网 加载失败", position='center', color='#2188ff', duration=3)
    pywebio.output.set_processbar('bar', i / 8)
    try:
        hk()
        i = i + 1
    except:
        print(traceback.print_exc())
        pywebio.output.toast("Error: HK01 加载失败", position='center', color='#2188ff', duration=3)
    pywebio.output.set_processbar('bar', i / 8)
    try:
        cna()
        i = i + 1
    except:
        print(traceback.print_exc())
        pywebio.output.toast("Error: 中央社 加载失败", position='center', color='#2188ff', duration=3)
    pywebio.output.set_processbar('bar', i / 8)
    try:
        xinhua()
        i = i + 1
    except:
        print(traceback.print_exc())
        pywebio.output.toast("Error: 新华网 加载失败", position='center', color='#2188ff', duration=3)
    pywebio.output.set_processbar('bar', i / 8)
    try:
        sputnik()
        i = i + 1
    except:
        print(traceback.print_exc())
        pywebio.output.toast("Error: 俄罗斯卫星通讯社 加载失败", position='center', color='#2188ff', duration=3)
    pywebio.output.set_processbar('bar', i / 8)
    try:
        aljazeera()
        i = i + 1
    except:
        print(traceback.print_exc())
        pywebio.output.toast("Error: 半岛电视台 加载失败", position='center', color='#2188ff', duration=3)
    pywebio.output.set_processbar('bar', i / 8)
    newslists = sorted(newslisttempt, key=lambda x: x["time"], reverse=True)


    # 創建一個空的set來存儲已經出現過的title
    titles = set()
    # 創建一個新的列表來存儲去重後的字典
    newslist = []
    for d in newslists:
        title = d["headline"]
        if title not in titles:
            # 若title還沒出現過，將其加入set和新的列表中
            titles.add(title)
            newslist.append(d)

    fields = ['headline', 'body','time','source','url']

    with open('lasttime.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newslist)

    pywebio.output.put_tabs([
        {'title': '全部', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

    <b><font size=5>[{item['headline']}]({item['url']})</font></b>

    > 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

    {item['body']}

    ---''') for item in newslist]},
        {'title': '环球网', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

    <b><font size=5>[{item['headline']}]({item['url']})</font></b>

    > 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

    {item['body']}

    ---''') for item in newslist if item['source'] == '环球网']},
        {'title': 'Reuters', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

    <b><font size=5>[{item['headline']}]({item['url']})</font></b>

    > 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

    {item['body']}

    ---''') for item in newslist if item['source'] == 'Reuters']},
        {'title': '香港01', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

    <b><font size=5>[{item['headline']}]({item['url']})</font></b>

    > 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

    {item['body']}

    ---''') for item in newslist if item['source'] == 'HK01']},
        {'title': '新华网', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

    <b><font size=5>[{item['headline']}]({item['url']})</font></b>

    > 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

    {item['body']}

    ---''') for item in newslist if item['source'] == '新华网']},
        {'title': '中央社', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

    <b><font size=5>[{item['headline']}]({item['url']})</font></b>

    > 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

    {item['body']}

    ---''') for item in newslist if item['source'] == '中央社']},
        {'title': 'UDN', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

    <b><font size=5>[{item['headline']}]({item['url']})</font></b>

    > 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

    {item['body']}

    ---''') for item in newslist if item['source'] == 'UDN']},
        {'title': '俄罗斯卫星通讯社', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

    <b><font size=5>[{item['headline']}]({item['url']})</font></b>

    > 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

    {item['body']}

    ---''') for item in newslist if item['source'] == '俄罗斯卫星通讯社']},
        {'title': '半岛电视台', 'content': [pywebio.output.put_markdown(f'''<img src={logourl(item["source"])} height="30">

    <b><font size=5>[{item['headline']}]({item['url']})</font></b>

    > 最后更新时间：{timediff(item['time'])}前，UTC+8 {item['time']}

    {item['body']}

    ---''') for item in newslist if item['source'] == 'AlJazeera']},
    ]).show()

def main():
    try:
        lasttime()
    except:
        load()

pywebio.start_server(main, port=8080)