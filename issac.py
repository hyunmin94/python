from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# chromedriver 버전과 Chrome 버전을 일치
# 다운로드 URL : https://sites.google.com/a/chromium.org/chromedriver/home
browser = webdriver.Chrome('C:\\Users\\acorn\\Downloads\\chromedriver.exe')
url = 'http://www.isaac-toast.co.kr/bbs/board.php?bo_table=branches'

# 브라우저에서 사용되는 엔진 자체의 파싱되는 시간을 기다려 주는 메소드 3초
browser.implicitly_wait(3)
# url에 해당하는 브라우져 오픈
browser.get(url)

# 서울 버튼 code selector 내용
seoul_btn = '#container > #bo_list > div:nth-child(1) > div > ul > li:nth-child(2) > div > #bo_cate > #bo_cate_ul > li:nth-child(2) > a'

# 서울 버튼을 통한 브라우져 이동
browser.find_element_by_css_selector(seoul_btn).click()

# 전체 버튼 code selector 내용
all_btn = '#bo_cate_ul.bo_cate2 > li:nth-child(1) > a'

# 전체 버튼을 통한 브라우져 이동
browser.find_element_by_css_selector(all_btn).click()

# 5초 시간 여유 주기
time.sleep(5)

# html 소스 get
html = browser.page_source
# html 내용 줄맞춤
soup = BeautifulSoup(html, 'html.parser')

issac_soup_list = soup.select('tr')

issac_store = issac_soup_list[0]

issac_list = []

for i in range(1, 10):
    address = str(issac_soup_list[i].select("td.td_subject")[0]).split('</td>')[0].split('">')[1]
    store = str(issac_soup_list[i].select("td.td_date")[1]).split('</td>')[0].split('">')[1]
    tel = str(issac_soup_list[i].select("td.td_date")[2]).split('</td>')[0].split('">')[1]

    issac_list.append([address, store, tel])

df = pd.DataFrame(issac_list, columns=['address', 'store', 'tel'])

print(df)