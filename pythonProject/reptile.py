import requests
from lxml import etree


def build_xpath(div_num):
    return "/html/body/div[@class ='bang_wrapper'] / div[@ class ='bang_content'] / div[@ class ='bang_list_box'] / " \
           "ul / li[" + str(div_num) + "] / div[@ class ='publisher_info'] // a[1] /text() "


def getinfo(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36'}  # 请求头
    resp = requests.get(url=url, headers=headers)  # 响应
    e = etree.HTML(resp.text)  # 解析
    bookname = e.xpath(
        '//html/body/div[@class="bang_wrapper"]//div[@class="bang_content"]//div[@class="bang_list_box"]//ul/li/div['
        '3]/a[1]/@title')  # 书名
    newbookname = [str(x) for x in bookname]
    new_name = []  # 用于存储name元素的列表

    for i in range(1, 21):
        rename = build_xpath(i)
        print(rename)
        name = e.xpath(rename)
        name = str(name)
        new_name.append(name)  # 将name元素添加到新数组中
    print(new_name)

    value = e.xpath(
        '//html/body/div[@class="bang_wrapper"]//div[@class="bang_content"]//div[@class="bang_list_box"]//ul/li/div['
        '8]/p[1]/span[1]/text()')  # 价格
    value = [str(x) for x in value]
    discoumt = e.xpath(
        '//html/body/div[@class="bang_wrapper"]//div[@class="bang_content"]//div[@class="bang_list_box"]//ul/li/div['
        '8]/p/span[3]/text()')  # 折扣
    discoumt = [str(x) for x in discoumt]
    original = e.xpath(
        '//html/body/div[@class="bang_wrapper"]//div[@class="bang_content"]//div[@class="bang_list_box"]//ul/li/div['
        '8]/p/span[2]/text()')  # 原价
    original = [str(x) for x in original]
    communt = e.xpath(
        '//html/body/div[@class="bang_wrapper"]//div[@class="bang_content"]//div[@class="bang_list_box"]//ul/li/div['
        '4]/a/text()')  # 评论数量
    communt = [str(x) for x in communt]

    with open('111.txt', 'a', encoding='utf-8') as f:
        for newbookname, new_name, value, discoumt, original, communt in zip(newbookname, new_name, value, discoumt, original, communt):
            column_widths = [100, 30, 30, 20, 20, 20, 20]
            alignment = '<'  # '>'表示右对齐，'<'表示左对齐
            formatted_string = f"{newbookname:{alignment}{column_widths[0]}}  {new_name:{alignment}{column_widths[1]}}   {value:{alignment}{column_widths[3]}}   {discoumt:{alignment}{column_widths[4]}}   {original:{alignment}{column_widths[5]}}   {communt:{alignment}{column_widths[6]}} "
            f.write(formatted_string + '\n')

if __name__ == "__main__":
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0118-0-1-'
    for i in range(1, 6):
        tmp = url + str(i)
        print(tmp)
        getinfo(tmp)
