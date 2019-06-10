from selenium import webdriver
import time
from lxml import etree
import random
#解析每个详情页面
def parse_detail_url(detail_url):
    driver = webdriver.Chrome()
    driver.get(detail_url)
    content = {}
    job_massage = {}
    html = etree.HTML(driver.page_source)
    career = html.xpath('//div[@class="job-name"]/span[1]/text()')[0]
    salary = html.xpath('//dd[@class="job_request"]/p[1]/span[1]/text()')
    job_massage['salary'] = salary
    era = html.xpath('//dd[@class="job_request"]/p[1]/span[2]/text()')
    job_massage['era'] = era
    experience = html.xpath('//dd[@class="job_request"]/p[1]/span[3]/text()')
    job_massage['experience'] = experience
    education = html.xpath('//dd[@class="job_request"]/p[1]/span[4]/text()')
    job_massage['education'] = education
    title = html.xpath('//dd[@class="job-advantage"]/span/text()')[0]
    advantage = html.xpath('//dd[@class="job-advantage"]/p/text()')
    job_massage[title] = advantage
    descripe = html.xpath('//dd[@class="job_bt"]/h3/text()')[0]
    job_content = html.xpath('//dd[@class="job_bt"]/div/p/text()')
    job_massage[descripe] = job_content
    content[career] = job_massage
    print( content)
    driver.close()
def spider():
    driver = webdriver.Chrome()
    driver.get('https://www.lagou.com/')
    driver.implicitly_wait(10)
    submitBtn0 = driver.find_element_by_id('cboxClose')
    submitBtn0.click()
    time.sleep(5)
    inputTag = driver.find_element_by_id('search_input')
    inputTag.send_keys('python')
    submitBtn = driver.find_element_by_id('search_button')
    submitBtn.click()
    i=1
    while i <5:
        #翻页操作，总共5页
        submitBtn1 = driver.find_element_by_class_name('pager_next ')
        submitBtn1.click()
        html = etree.HTML(driver.page_source)
        hrefs = html.xpath('//div[@class="p_top"]//a[1]/@href')
        for detail_url in hrefs:
            parse_detail_url(detail_url)
            time.sleep(random.randint(1, 10))
            print('=' * 50)
        i +=1
if __name__ == '__main__':
    spider()
