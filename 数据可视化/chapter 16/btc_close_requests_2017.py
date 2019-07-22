from urllib.request import *

json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
req = request.get(json_url)

# 将数据写入文件
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)
    
file_requests = req.json()
