import  requests


key = input("请输入关键词:")  

url = "https://image.baidu.com/search/index?tn=baiduimage&word="    #百度图库 需要user_agent 才能爬取

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0"

resp = requests.get(url,
                    params={"word":key},
                    headers={"User-agent":user_agent})

with open("baidu.html","wb") as f:
    f.write(resp.content)


# key = input("请输入关键词")
# url = "https://www.baidu.com/s"     #这个是百度的页面搜索url
# user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0"
#
# resp = requests.get(url,
#                     params={"wd":key},  #这里是用wd
#                     headers = {"user-agent":user_agent})
#
# with open("test.html", "wb") as f:
#     f.write(resp.content)

