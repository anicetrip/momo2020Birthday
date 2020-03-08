import requests
import json
import datetime
from collections import OrderedDict

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}


def getRequest():
    num = 1
    json_urls = ["https://api.bilibili.com/x/space/arc/search?mid=431537245&ps=30&tid=0&pn={}&keyword=&order=pubdate&jsonp=jsonp".format(str(i)) for i in range(1, 4)]
    with open("data.json", "w") as f:
        for url in json_urls:
            response = requests.get(url, headers=headers)
            dict_str = json.loads(response.text)
            dic_list = dict_str["data"]["list"]["vlist"]
            for content in dic_list:
                x = OrderedDict()
                x["av"] = "av" + str(content["aid"])
                x["avurl"] = "https://www.bilibili.com/video/" + x["av"]
                x["title"] = content["title"]
                utime = content["created"]
                x["time"] = datetime.datetime.fromtimestamp(utime).strftime("%Y-%m-%d %H:%M:%S")
                x["description"] = content["description"]
                x["play"] = content["play"]
                json_dic = {str(num): x}
                num += 1
                json_str = json.dumps(json_dic, indent=4)
                f.write(json_str)


if __name__ == "__main__":
    getRequest()