from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup as bs
import xlsxwriter
from io import BytesIO


class CarBrand:
    """品牌车"""

    def __init__(self, initials, brand, img):
        self._initials = initials
        self._brand = brand
        self._img = img

    @property
    def initials(self):
        return self._initials

    @property
    def brand(self):
        return self._brand

    @property
    def img(self):
        return self._img


def crawl_car_brand():
    r = requests.get("https://www.autohome.com.cn/car/#pvareaid=3311275")
    r.encoding = r.apparent_encoding

    soup = bs(r.text, "html.parser")
    html = soup.find(id="contentSeries")
    car_html_list = html.find_all("dl", attrs={"class": "clearfix brand-series__item"})
    list_all = []
    for car_html in car_html_list:
        for car in car_html.find_all("dd"):
            print(car)
            car_a = car.find('a')
            print(car_a)
            car_img = car.find('img')
            print(car_img)
            list_all.append(CarBrand(car_a.get('eng'), car_a.get('cname'), "https:" + car_img.get('src')))
    generate_table(list_all)


def generate_table(car_list=None):
    """生成xls表格文件"""
    if car_list is None:
        car_list = []
    wb = xlsxwriter.Workbook('轿车品牌.xls')
    ws = wb.add_worksheet('轿车品牌')
    ws.write(0, 0, '首字母')
    ws.write(0, 1, '品牌名称')
    ws.write(0, 2, '品牌图片')

    for i, card_bard in enumerate(car_list):
        ws.set_row(i + 1, 50)
        ws.write(i + 1, 0, card_bard.initials)
        ws.write(i + 1, 1, card_bard.brand)
        # 从远程读取文件
        image_data = BytesIO(urlopen(card_bard.img).read())
        ws.insert_image(i + 1, 2, card_bard.img, {'image_data': image_data, 'x_scale': 0.5, 'y_scale': 0.5})

    wb.close()


if __name__ == '__main__':
    crawl_car_brand()
