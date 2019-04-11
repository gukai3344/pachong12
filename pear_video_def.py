# import requests
# import re
# import json
# import os
# from concurrent.futures import ThreadPoolExecutor
#
# datas = []
#
# page_num = 1
#
#
# def get_datails(resp):
#     res =re.findall('<a href="(video_.*?)"',resp.text )
#     base_url = "https://www.pearvideo.com/"
#     for i in res:
#         detail_url = base_url + i
#         detail_resp = requests.get(detail_url)
#         title = re.search('<h1 class="video-tt">(.*?)</h1>',detail_resp.text).group(1)
#         video_url = re.search('srcUrl="(.*?)"',detail_resp.text).group(1)
#         dic = {"title":title,"video_url":video_url}
#         pool.submit(download_video,video_url,title)
#         datas.append(dic)
#
#
#
# def get_page_data(categoryId):
#     url = "https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=%s&start=" % categoryId
#
#     for i in range(page_num):
#         url1 = url + str(i*12)
#         resp = requests.get(url1)
#         if requests.status_codes == 200:
#             print('请求成功!')
#             get_datails(resp)
#
#
# def download_video(video_url,video_name):
#     print('开始下载', video_name)
#     resp = requests.get(video_url)
#     dir = os.path.dirname(__file__)
#
#     file_path = os.path.join(dir,"videos", video_name+".mp4")
#
#     if os.path.exists(file_path):
#         print(video_name, "+++++++++已经下载过了!")
#         return
#     with open(file_path, "wb") as f:
#         f.write(resp.content)
#
# def write_json():
#     with open("datas.json","wt") as f:
#         json.dump(datas,f)
#
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor()
#
#     get_page_data(31)
#     write_json()

import requests
import re
import json
import os
from concurrent.futures import ThreadPoolExecutor   #线程池模块




# 存储解析完成的数据
datas = []

# 要爬取的页数
page_num = 1
# 要爬取的分类


def get_details(resp):
    res = re.findall('<a href="(video_\d+)"', resp.text)
    base_url = "https://www.pearvideo.com/"
    for i in res:
        # 拼接详情页面的地址
        detail_url = base_url + i
        detail_resp = requests.get(detail_url)
        # 解析标题
        title = re.search('<h1 class="video-tt">(.*?)</h1>', detail_resp.text).group(1)
        # 时间
        subdate = re.search('<div class="date">(.*?)</div>', detail_resp.text).group(1)
        # 点赞数
        f_count = re.search('<div class="fav" data-id="\d+">(\d+)</div>', detail_resp.text).group(1)
        author = re.search('</i>(.*?)</div>', detail_resp.text).group(1)
        # 详情
        content = re.search('<div class="summary">(.*?)</div>', detail_resp.text).group(1)
        # 视频地址
        video_url = re.search('srcUrl="(.*?)"',detail_resp.text).group(1)
        dic = {"title": title, "subdate": subdate, "f_count": f_count, "author": author, "content": content,"video_url":video_url}
        # 开始下载视频文件
        # download_video(video_url,title)
        pool.submit(download_video,video_url,title) # 异步提交任务到线程池
        datas.append(dic)


# 请求首页列表
def get_page_data(categoryId):
    url = "https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=%s&start=" % categoryId

    for i in range(page_num):
        url1 = url + str(i * 12)
        #一页显示12 显示多页就是多页*12
        resp = requests.get(url1)
        if resp.status_code == 200:
            print("请求成功返回！")
            get_details(resp)



def download_video(video_url,video_name):
    print("开始下载",video_name)
    resp = requests.get(video_url)
    dir = os.path.dirname(__file__)
    video_name = video_name.replace('"',"")     #当标题出现特殊字符,转义下
    video_name = video_name.replace('?', "")
    file_path = os.path.join(dir,"videos",video_name+".mp4")    #文件名拼接下

    if os.path.exists(file_path):
        print(video_name,"+++++++++++++++++++++已经下载过了!")
        return

    with open(file_path,"wb") as f:
        f.write(resp.content)   #注意resp.content 是显示二进制形式,用于图片,视频
        #如果是resp.test 是显示文本形式的 字符串

    pass



# 将数据写入json文件
def write_json():
    with open("datas.json", "wt") as f:
        json.dump(datas, f)




if __name__ == '__main__':
    # 开启线程池
    pool = ThreadPoolExecutor()


    get_page_data(31)
    # 写入
    write_json()



