#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" ANA机票价格爬虫 """

__author__ = 'Shu Xu'

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import pandas as pd
import datetime


def search_price(start_date, end_date, flag):
    try:
        # 进入多航段搜索
        mix = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="module-ticket"]/div/div[2]/div[1]/a[3]'))
        )
        mix.click()

        # 第一航段
        date1cho = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#requestedSegment1 > dl.departDate > dd > span.paxFormIcon.paxFormIconCal > img'))
        )
        date1cho.click()
        next3mon = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="requestedSegment:0:departureDate:field_pctext_view"]/div/div/ul/li[2]/a'))
        )
        next3mon.click()
        xpath = '//*[@id="calsec' + str(encode.loc[start_date, 0]) + '"]/table/tbody/tr[' + str(
            encode.loc[start_date, 1]) + ']/td[' + str(encode.loc[start_date, 2]) + ']/a'
        date1 = wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        # date1 = wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//*[@id="calsec4"]/table/tbody/tr[5]/td[1]/a'))
        # )
        date1.click()
        fr1 = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '#requestedSegment1 > dl:nth-child(3) > dd > a.paxFormIconAirport.paxFormIconSelect > img'))
        )
        fr1.click()
        area = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="requestedSegment:0:departureAirportCode:field_region_20"]'))
        )
        area.click()
        if flag == 0:
            city_xpath = '//*[@id="PEK"]'
        else:
            city_xpath = '//*[@id="SHA"]'
        city = wait.until(
            EC.presence_of_element_located((By.XPATH, city_xpath))
        )
        city.click()
        to1 = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '#requestedSegment1 > dl:nth-child(4) > dd > a.paxFormIconAirport.paxFormIconSelect > img'))
        )
        to1.click()
        area = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="requestedSegment:0:arrivalAirportCode:field_region_01"]'))
        )
        area.click()
        city = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="HKD"]'))
        )
        city.click()

        # 第二航段
        date2cho = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#requestedSegment2 > dl.departDate > dd > span.paxFormIcon.paxFormIconCal > img'))
        )
        date2cho.click()
        xpath = '//*[@id="calsec' + str(encode.loc[end_date, 0]) + '"]/table/tbody/tr[' + str(
            encode.loc[end_date, 1]) + ']/td[' + str(encode.loc[end_date, 2]) + ']/a'
        date2 = wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        # date2 = wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//*[@id="calsec5"]/table/tbody/tr[2]/td[2]/a'))
        # )
        date2.click()
        fr2 = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '#requestedSegment2 > dl:nth-child(3) > dd > a.paxFormIconAirport.paxFormIconSelect > img'))
        )
        fr2.click()
        area = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="requestedSegment:1:departureAirportCode:field_region_01"]'))
        )
        area.click()
        city = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="TYO"]'))
        )
        city.click()
        to2 = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '#requestedSegment2 > dl:nth-child(4) > dd > a.paxFormIconAirport.paxFormIconSelect > img'))
        )
        to2.click()
        area = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="requestedSegment:1:arrivalAirportCode:field_region_20"]'))
        )
        area.click()
        if flag == 1:
            city_xpath = '//*[@id="PEK"]'
        else:
            city_xpath = '//*[@id="SHA"]'
        city = wait.until(
            EC.presence_of_element_located((By.XPATH, city_xpath))
        )
        city.click()

        # 设置人数并搜索
        add = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="searchForm"]/div[1]/div[2]/dl/dd/ul/li[1]/dl/div/ul/li[3]/a'))
        )
        add.click()
        search = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#searchForm > div.areaSeparate > p > input'))
        )
        search.click()

        # 等待输入验证码直到出现票价
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#searchContentsForm > div:nth-child(7)'))
        )
        time.sleep(1)

        # 获取最低价
        if exist('//*[@id="j_idt369:0:cmnErrorMessageWindow:j_idt377"]/div'):
            browser.find_element_by_xpath('//*[@id="j_idt369:0:cmnErrorMessageWindow:j_idt377"]/p/input').click()

        price = browser.find_element_by_xpath('//*[@id="searchContentsForm"]/div[1]/div/table/tbody/tr[1]/td[1]').text
        price = int(re.findall(r"\d+", price.replace(',', ''))[0])

        # 回到首页
        back = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cmnHeader"]/div[1]/div/p/a/img'))
        )
        back.click()
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="module-ticket"]/div/div[2]/div[1]/a[3]'))
        )

        return price

    except TimeoutException:
        browser.get(url)
        if flag == 0:
            return search_price(sd, ed, 0)
        else:
            return search_price(sd, ed, 1)


# 判断元素是否存在
def exist(xpath):
    flag = True
    try:
        browser.find_element_by_xpath(xpath)
        return flag
    except NoSuchElementException:
        flag = False
        return flag


# 初始化
def init():
    try:
        login = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-area > div > button > span > span'))
        )
        login.click()
        num = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-custno"]'))
        )
        num.clear()
        time.sleep(1)
        num.send_keys('**')
        # time.sleep(1)
        pas = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-password"]'))
        )
        pas.clear()
        time.sleep(1)
        pas.send_keys('**')
        time.sleep(1)
        browser.find_element_by_name('login').click()
        ctn = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="contents"]/div/div/form/div[3]/div/div[2]/p/a'))
        )
        ctn.click()
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-data"]/div/div[4]/a'))
        )
    except TimeoutException:
        browser.get(url)
        init()


if __name__ == '__main__':
    # 生成所有待查询往返日期
    # start = datetime.date(2019, 7, 28)
    # end = datetime.date(2019, 8, 22)
    # days_min = 5
    # days_max = 10
    # excel_path = 'ticket.xlsx'
    # encode = pd.read_excel(excel_path, sheet_name='Sheet1', index_col=0)
    # roundtime_all = []
    # for i in range(int((end - start).days) + 1):
    #     start_date = start + datetime.timedelta(days=i)
    #     for j in range(days_min, days_max):
    #         roundtime = []
    #         end_date = start_date + datetime.timedelta(days=j)
    #         roundtime.append(start_date)
    #         roundtime.append(end_date)
    #         roundtime_all.append(roundtime)
    # header = ['出发日期', '返回日期']
    # roundtime_all_df = pd.DataFrame(roundtime_all, columns=header)
    # write = pd.ExcelWriter(excel_path)
    # encode.to_excel(write, sheet_name='Sheet1', header=[0, 1, 2], index=True)
    # roundtime_all_df.to_excel(write, sheet_name='Sheet2', header=header, index=False)
    # roundtime_all_df.to_excel(write, sheet_name='Sheet3', header=header, index=False)
    # write.save()

    excel_path = 'ticket.xlsx'
    encode = pd.read_excel(excel_path, sheet_name='Sheet1', index_col=0)
    price_bs = pd.read_excel(excel_path, sheet_name='Sheet2')
    price_sb = pd.read_excel(excel_path, sheet_name='Sheet3')

    # 打开浏览器并登录ANA
    url = 'https://www.ana.co.jp/zh/cn/'
    browser = webdriver.Chrome()  # 打开浏览器
    browser.maximize_window()
    browser.get(url)  # 进入相关网站
    wait = WebDriverWait(browser, 30)
    init()
    # login = wait.until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-area > div > button > span > span'))
    # )
    # login.click()
    # num = wait.until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="login-custno"]'))
    # )
    # num.clear()
    # num.send_keys('4610699296')
    # pas = wait.until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="login-password"]'))
    # )
    # pas.clear()
    # pas.send_keys('336429226626xs')
    # rem = wait.until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, '//*[@id="toggle_39930318"]/div[1]/div/form/p[5]/span/label/span'))
    # )
    # rem.click()
    # con = wait.until(
    #     EC.presence_of_element_located(
    #         (By.CSS_SELECTOR, '#toggle_6f9ef726f > div.js-toggleInner > div > form > button.btn.submit.spt15'))
    # )
    # con.click()
    # browser.find_element_by_name('login').click()
    # ctn = wait.until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, '//*[@id="contents"]/div/div/form/div[3]/div/div[2]/p/a'))
    # )
    # ctn.click()

    # 检索票价
    price_bs_temp = []
    price_sb_temp = []
    for i in range(len(price_bs.index.values)):
        sd = price_bs.loc[i, '出发日期']
        ed = price_bs.loc[i, '返回日期']
        price_bs_temp.append(search_price(sd, ed, 0))
        price_sb_temp.append(search_price(sd, ed, 1))

    browser.close()

    today = datetime.datetime.now()
    date_search = str(today.month) + '月' + str(today.day) + '日' + str(today.hour) + '时' + str(today.minute) + '分'
    price_bs[date_search] = price_bs_temp
    price_sb[date_search] = price_sb_temp
    write = pd.ExcelWriter(excel_path)
    encode.to_excel(write, sheet_name='Sheet1', header=[0, 1, 2], index=True)
    price_bs.to_excel(write, sheet_name='Sheet2', header=list(price_bs.columns.values), index=False)
    price_sb.to_excel(write, sheet_name='Sheet3', header=list(price_sb.columns.values), index=False)
    write.save()
