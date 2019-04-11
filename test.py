# import  requests
# headers={
#     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
#
# }
# response = requests.get('http://www.jianshu.com',
#                         headers=headers)
# # print(response.text)
# # print(response.content)
# print(response.status_code)
# print(response.headers)
# print(response.cookies)
# print(response.cookies.get_dict())
# print(response.cookies.items)
# print(response.url)
# print(response.history)
# print(response.encoding)
#
# from contextlib import  closing
# with closing(requests.get("http://www.jianshu.com",stream=True)) as response:
#     for line in response.iter_content():
#         pass

# import requests
# response = requests.get("http://www.autohome.com/news")
# response.encoding="GBK" #页面如果是GBK 不设置就会出现乱码现象
# print(response.text)

# import requests
# #
# # response=requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1509868306530&di=712e4ef3ab258b36e9f4b48e85a81c9d&imgtype=0&src=http%3A%2F%2Fc.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F11385343fbf2b211e1fb58a1c08065380dd78e0c.jpg')
# #
# # with open('a.jpg','wb') as f:
# #     f.write(response.content)

# import requests
# proxies={
#     'http':'http://egon:123@localhost:9743',#带用户名密码的代理,@符号前是用户名与密码
#     'http':'http://localhost:9743',
#     'https':'https://localhost:9743',
# }
# respone=requests.get('https://www.12306.cn',
#                      proxies=proxies)
#
# print(respone.status_code)
import requests
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}
respone=requests.get('https://www.12306.cn',
                     proxies=proxies)

print(respone.status_code)