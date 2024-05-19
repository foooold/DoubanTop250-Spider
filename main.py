# 爬取豆瓣Top250电影名称及其评分然后储存在'./Top250.txt'中
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "User""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}


# 将爬取的字典中不含'/'的数据加入新字典，主要是把爬到的所有title里以'/'开头的数据剔除
def scrape(tag):
    datas = []
    all_datas = soup.findAll("span", {"class": tag})
    for i in range(0, len(all_datas)):
        if '/' not in all_datas[i].string:
            datas.append(all_datas[i].string)    # 这一步感觉复杂了，不知道可不可以直接删除含有'/'的数据
    return datas


row = 1  # 定义行计数
with open('Top250.txt', 'w', encoding='UTF-8') as f:
    for num in range(0, 226, 25):    # 豆瓣Top250网页共10page，page1的网址以'?start=0'结尾，page10的网址以'?start=225'结尾
        content = requests.get(f"https://movie.douban.com/top250?start={num}", headers=headers).text
        soup = BeautifulSoup(content, "html.parser")
        title = scrape('title')
        rating_num = scrape('rating_num')
        for i in range(0, len(title)):
            res = str(f'{row}.{title[i]} {rating_num[i]}')
            print(res)
            f.write(f'{res}\n')
            row = row + 1
