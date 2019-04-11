# import requests,re
# session = requests.session()
#
# login_page_url = "https://github.com/login"
# resp = session.get(login_page_url)
# token = re.search('authenticity_token" value="(.*?)" /> ',resp.text).group(1) # 获取token 在请求体拿
#
# login_url = "https://github.com/session"    #这里要点击登录请求才能看到
# resp2= session.post(login_url,
#                     headers={
#                         "Referer": "https://github.com/login",
#                         "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Mobile Safari/537.36"
#
#                     },
#                     data={"commit": "Sign in",
#                           "utf8": "✓",
#                           "authenticity_token": token,
#                           "login": "oldboyedujerry",
#                           "password": "123654asdAsd",
#                           "webauthn-support": "supported"},)
#
# print(resp2.status_code)
# with open("github_home.html", "wb") as f:
#     f.write(resp2.content)
# print("oldboyedujerry/testProject" in resp2.text)
"""
1.获取token
地址:https://github.com/login
token放在了响应体中


"""
import requests,re
# 1.获取token
login_page_url = "https://github.com/login"
resp = requests.get(login_page_url) # 请求首页
# 获取返回的cookie
cookie = resp.cookies.get_dict()
token = re.search('authenticity_token" value="(.*?)" /> ',resp.text).group(1) # 获取token




# 2.请求登录接口
login_url = "https://github.com/session"
resp2 = requests.post(login_url,
              headers={
                  "Referer": "https://github.com/login",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
              },
              data={"commit": "Sign in",
                    "utf8": "✓",
                    "authenticity_token": token,
                    "login": "oldboyedujerry",
                    "password": "123654asdAsd",
                    "webauthn-support": "supported"},
              cookies = cookie)

print(resp2.status_code)
with open("github_home.html","wb") as f:
    f.write(resp2.content)
print("oldboyedujerry/testProject" in resp2.text)




