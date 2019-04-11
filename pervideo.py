import requests
import re
import json
url ="https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=31&start=0"

datas= []
resp = requests.get(url)
if resp.status_code == 200:
    print("请求成功")
    # print(resp.text)    #这个是字符串形式获取
    # print(resp.content) #这个是已bytes形式获取 ,拿图片,视频

    res=re.findall('<a href="(video_.*?)"',resp.text )  #re正则过滤
    # print(res)
    #拼接详情页面的地址
    base_url = "https://www.pearvideo.com/"
    for i in res:
        detail_url = base_url + i
        # print(detail_url)   #通过url + 匹配出来的信息,拼接想要的内容
        detail_resp = requests.get(detail_url)
        # print(detail_resp.text)
        # 验证是否与网页一致
        # with open('text.html', 'wb') as f:
        #     f.write(detail_resp.content)

        #解析标题
        title = re.search('<h1 class="video-tt">(.*?)</h1>',detail_resp.text).group(1)
        # print(title)
        #解析时间
        subdata = re.search('<div class="date">(.*?)</div>',detail_resp.text).group(1)
        # print(subdata)
        # 点赞
        up = re.search('<div class="fav" data-id="\d+">(\d+)</div>',detail_resp.text).group(1)
        # print(up)
        author = re.search('</i>(.*?)</div>', detail_resp.text).group(1)
        # print(author)
        # content = re.search('<div class="summary">(.*?)</div>', detail_resp.text).group(1)
        # print(content)
        video_url = re.search('srcUrl="(.*?)"', detail_resp.text).group(1)
        dic = {"title":title,"subdata":subdata,"up":up,"author":author,"video_url":video_url}
        # print(video_url)
        datas.append(dic)



# with open("datas.json", "wt") as f:
#     json.dump(datas,f)


# print(json.load(open("datas.json")))


#########面条版完成

