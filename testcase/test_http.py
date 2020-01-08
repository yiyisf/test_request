import json
import requests
from jsonschema import validate
from requests import request, get, Response
from jsonpath import jsonpath


class TestHTTP:
    def setup(self):
        # self.proxy={"http":"http://127.0.0.1:8090"}
        self.proxy=None
    def test_fxm5547(self):
        url= "https://fxm5547.baobaobooks.com/goodsapi/goods/newest"
        r = requests.get(url)
        self.inspect_response(r)


    def inspect_response(self, r: Response):
        print(r.json())
        print(r.cookies)
        print(r.text)
        print(r.encoding)
        print(r.headers)
        print(r.raw)
        print(r.request)
        print(r.status_code)
        # print(r.reason)



    def test_testerhome(self):
        # 使用json
        url = "https://testerhome.com/api/v3/topics.json?"
        params = {"limit": "3"}
        r = requests.get(url, params=params)
        print(r.json())
        print(r.json()['topics'][-1]['user']['login']=='liangqiangWang')

    def test_testerhome_jsonpath(self):
        # 使用jsonpath
        url = "https://testerhome.com/api/v3/topics.json?"
        params = {"limit": "2"}
        data = requests.get(url, params=params).json()
        l = jsonpath(data, "$.topics[?(@.user.login == 'xz-2018-05')].user.id")
        print(l)
        print(l[0] == 47182)
        print(jsonpath(data, "$.topics[?(@.user.login == 'xz-2018-05')].user.id")[0]== 47182 )
        # assert jsonpath(data, "$.topics[?(@.user.login == '944527839')].user.id")[0] == 21277

    def test_testerhome_jsonschema(self):
        # 使用jsonschema
        url = "https://testerhome.com/api/v3/topics.json?"
        params = {"limit": 2}
        data = requests.get(url, params=params).json()
        schema = json.load(open("topic.json"))
        validate(data, schema=schema)



    def test_xueqiu(self):
        url= "https://xueqiu.com/stock/search.json?"
        params = {"code": "sogo", "size": 3, "page": 1}
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
        cookies = {"xq_a_token": "d831cd39b53563679545656fba1f4efd8e48faa0",
                   "xq_r_token": "fd2f0f487c8298cad8e7519f1560abb7a18c589d"}
        r = requests.get(url, params=params, cookies=cookies, headers=headers, proxies=self.proxy)
        # print(r.json())
        # print(r.json()["stocks"][0]["name"] == "搜狗")
        print(r.json().stocks[0].name)
        # print(r.json()["stocks"][0]["name"]=="Electrameccanica汽车")

    def test_get_qyweixin(self):
        # 使用json
        url = " https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
        params = {"corpid": "wwad5d5cb999214373","corpsecret":"uF4eMYJdMZGgRjdvEv5fQUbnK5Kbg3EYs0dNCSoSPsc"}
        r = requests.get(url, params=params)
        print(r.json()["access_token"])

