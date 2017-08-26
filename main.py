# -*- coding:utf-8 -*-
from selenium import webdriver
from 存取工具 import webUtils
from 存取工具.DataUtils import DataUtils


def get_singer():
    singer_list1 = []
    driver = webdriver.Ie("IEDriverServer.exe")
    # 从网易云中获得歌手名称 因为Chrome没找到保存登录的方式 所以用很慢很慢的IE
    webUtils.get_singer_name(driver, singer_list1)
    driver.quit()
    singerTXT = DataUtils(DataUtils.singer_name)
    singerTXT.set_data(singer_list1)
    return singer_list1


def get_song_url(driver, singer):
    print("正在获得 " + singer + " 的谱子URL")
    webUtils.get_singer_num(driver, singer)
    try:
        for each in driver.find_elements_by_css_selector('a[href^=\/artist]')[1:]:
            webUtils.get_GTP_url(driver, "" + each.get_attribute("href"), singer)
    except Exception as e:
        pass


# get_singer()
# singerTXT = DataUtils(DataUtils.singer_name)
# singer_name_list = singerTXT.get_data()
driver = webdriver.Chrome("chromedriver.exe")
# for each in singer_name_list:
#     get_song_url(driver, each.rstrip("\n"))
get_song_url(driver, "好妹妹")

print("finish")
