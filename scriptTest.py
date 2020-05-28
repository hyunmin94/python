from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# chromedriver 버전과 Chrome 버전을 일치
# 다운로드 URL : https://sites.google.com/a/chromium.org/chromedriver/home
browser = webdriver.Chrome('C:/myPyCode/chromedriver.exe')
url = 'https://www.starbucks.co.kr/store/store_map.do?disp=locale'

# 브라우저에서 사용되는 엔진 자체의 파싱되는 시간을 기다려 주는 메소드 3초
browser.implicitly_wait(3)
# url에 해당하는 브라우져 오픈
browser.get(url)

# 서울 버튼 code selector 내용
seoul_btn = '#container > div > form > fieldset > div > section > article.find_store_cont ' \
            '> article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'

# 서울 버튼을 통한 브라우져 이동
browser.find_element_by_css_selector(seoul_btn).click()

# 전체 버튼 code selector 내용
all_btn = '#mCSB_2_container > ul > li:nth-child(1) > a'

# 전체 버튼을 통한 브라우져 이동
browser.find_element_by_css_selector(all_btn).click()

# 5초 시간 여유 주기
time.sleep(5)

# html 소스 get
html = browser.page_source
# html 내용 줄맞춤
soup = BeautifulSoup(html, 'html.parser')

# li 태그의 class = quickResultLstCon 데이터 호출
starbucks_soup_list = soup.select('li.quickResultLstCon')
starbucks_list = []

# 데이터 전처리 (예시 데이터)
# =============================================================================================================================================================================================================================
# <li class="quickResultLstCon" data-code="3762" data-hlytag="null" data-index="0" data-lat="37.501087" data-long="127.043069" data-name="역삼아레나빌딩" data-storecd="1509" style="background:#fff">
# 	<strong>역삼아레나빌딩
# 		<img alt="" class="setStoreFavBtn mCS_img_loaded" data-my_siren_order_store_yn="N" data-name="역삼아레나빌딩" data-store="1509" data-yn="N" 			src="//image.istarbucks.co.kr/common/img/store/icon_fav_off.png"/>
# 	</strong>
# 	<p class="result_details">서울특별시 강남구 언주로 425 (역삼동)<br/>1522-3232</p>
# 	<i class="pin_general">리저브 매장 2번</i>
# </li>
# =============================================================================================================================================================================================================================

for item in starbucks_soup_list:
    name = item.select('strong')[0].text.strip()
    lat = item['data-lat'].strip()
    lng = item['data-long'].strip()
    store_type = item.select('i')[0]['class'][0][4:]
    address = str(item.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
    tel = str(item.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]
    starbucks_list.append([name,lat,lng,store_type,address,tel])

columns = ['매장형', '위도', '경도', '매장타입', '주소', '전화번호']
df = pd.DataFrame(starbucks_list,columns=columns)
print(df)
