# -*- coding:utf-8 -*-

import time
from testcase import *

#添加物业公司

login('15707256976', '1234567')
time.sleep(5)
browser.find_element_by_xpath('//div/div/nav/ul/li[1]/ul/li[2]/a').click()
browser.find_element_by_xpath('//div[3]/div[2]/div/div[3]/div/div[2]/div[2]/button').click()
#公司名称
browser.find_element_by_xpath('//div/div[2]/div/form/div[1]/div/input').send_keys('company')
#公司简称
browser.find_element_by_xpath('//div/div[2]/div/form/div[2]/div/input').send_keys('COM')

browser.find_element_by_xpath('//div/div[2]/div/form/div[9]/div[2]/div/input').send_keys('username')
browser.find_element_by_xpath('//div/div[2]/div/form/div[9]/div[4]/div/input').send_keys('password')
browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]').click()
print('kkkk')