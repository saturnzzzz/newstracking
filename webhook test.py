import csv
from datetime import datetime
from pywebio.input import *
from pywebio.output import *
import pywebio

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

def checkword(wordlist):
    list = wordlist.split("；")
    for word in list:
        if word in content_list:
            return f'关键词{word}已存在'


while 1 + 1 == 2:
    with open('wordlist.txt', 'r') as check:
        lines = check.readlines()
        content_list = [line.strip() for line in lines]
    content_list = list(set(content_list))
    put_markdown(rf"""## 关键词更新
        #### 当前关键词
        {content_list}
        """)
    words = input('增删关键词')
    put_markdown('> 1. 输入多个请按中文符号"；"分割'
                 '> 2. 直接点击"提交"可查看当前筛选新闻')
    wordlist = words.split("；")
    for word in wordlist:
        if word not in content_list:
            with open('wordlist.txt', 'a', encoding='utf-8') as file:
                for item in wordlist:
                    file.write(item + "\n")
        else:
            with open('wordlist.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
            with open('wordlist.txt', 'w', encoding='utf-8') as file:
                for line in lines:
                    if line.strip() not in wordlist:
                        file.write(line)

    with open('lasttime.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        lasttime = list(reader)

    newslist = []

    for item in lasttime:
        desc = item['headline'] + item['body']
        if any(word in desc for word in content_list):
            newslist.append(item)
        else:
            print('no')

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