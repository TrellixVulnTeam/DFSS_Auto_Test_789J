# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

from selenium import webdriver
import csv

url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
driver = webdriver.PhantomJS()
#csv_file = open(r'F:\TestSpider\SongList.csv','w',newline='',encoding='gbk')
csv_file = open('F:\TestSpider\SongList.csv','w',newline='')
writer = csv.writer(csv_file)
writer.writerow(['标题','播放数','链接'])

while url != 'javascript:void(0)':
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    data = driver.find_element_by_id('m-pl-container').find_elements_by_tag_name('li')

    for i in range(len(data)):
        nb = data[i].find_element_by_class_name('nb').text
        if '万'in nb and int(nb.split("万")[0]) > 200:
            msk = data[i].find_element_by_css_selector('a.msk')
            writer.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])
    #定位下一页
    url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')
csv_file.close()



















