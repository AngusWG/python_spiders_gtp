# -*- coding:utf-8 -*-
import urllib.request

import os
from pip._vendor import requests
from selenium.webdriver.common.keys import Keys


def gethtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('utf-8')


def get_singer_name(driver, list1):
    html = "http://music.163.com/#/my/m/music/artist"
    driver.get(html)
    driver.switch_to_frame("g_iframe")
    element = driver.find_element_by_link_text("下一页")
    while True:
        try:
            for each in driver.find_elements_by_css_selector('a[href^=\/artist]'):
                if each.text != "":
                    list1.append(each.text + "\n")
            if "disabled" in element.get_attribute("class"):
                break
            element.send_keys(Keys.ENTER)
        except Exception as e:
            print(e)
            break

    return list1


def get_singer_num(driver, singer_name):
    html = "http://www.jitashe.org/search.php?mod=group"
    driver.get(html)
    element = driver.find_element_by_id("scform_srchtxt")
    element.send_keys(singer_name)
    element.send_keys(Keys.ENTER)


def get_GTP_url(driver, url, sing_name):
    print("已进入 " + sing_name + " 的歌手页面")
    js = 'window.open(" ' + url + "t2/" + ' ");'
    driver.execute_script(js)
    handles = driver.window_handles
    driver.switch_to_window(handles[-1])
    # 获得当页歌手的所以谱子地址
    # driver.get(url + "t2/")

    while True:
        try:
            for each in driver.find_elements_by_css_selector('a[href^=\/tab]'):
                print(each.text)
                get_pic_url(driver, "" + each.get_attribute("href"), sing_name, ""+each.text)
            element = driver.find_element_by_link_text("下一页")
            if not driver.find_element_by_link_text("下一页"):
                break
            else:
                element.click()
        except Exception as e:
            print(e)
            break
    driver.close()
    driver.switch_to_window(handles)


def get_pic_url(driver, url, sing_name, song_name):
    print("正在获得 " + song_name + " 的图片连接")
    js = 'window.open(" ' + url + ' ");'
    driver.execute_script(js)
    # driver.get(url)
    handles = driver.window_handles
    driver.switch_to_window(handles[-1])
    i = 1
    element = driver.find_element_by_class_name("imgtab").find_elements_by_css_selector('img')
    try:
        for each in element:
            print(each.get_attribute("file").strip("@!tab_thumb"))
            save_pic(each.get_attribute("file").strip("@!tab_thumb").replace("//att", "http://www"), sing_name,
                     song_name.replace(":", "-") + str(i))
            i = i + 1
    except Exception as e:
        pass
    driver.close()
    driver.switch_to_window(handles)


def save_pic(url, sing_name, song_name):
    print("正在保存 " + song_name + " 的图片")
    # 保存图片
    file_name = "GTP/" + sing_name + "/" + song_name + "." + url[-3:]
    path = "GTP/" + sing_name
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)

    # r = requests.get(url, stream=True)
    # with open(file_name, 'wb') as fd:
    #     for chunk in r.iter_content():
    #         fd.write(chunk)

    img = requests.get(url)
    print(file_name)
    f = open(file_name, 'ab')  # 存储图片，多媒体文件需要参数b（二进制文件）
    f.write(img.content)  # 多媒体存储content
    f.close()
