from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# html 형식의 문자열에서 원하는 데이터만 가공처리 함수
def cut_unness(data):
    return data[data.index('>') + 1:data.index('<', 1)].strip()

browser = webdriver.Chrome('C:/DBExam/chromedriver.exe')

# 지점별로 [지점명, 주소, 전화번호]의 리스트형태로 저장할 변수
total = []

# 총 16개 이삭토스트 지점페이지 웹 크롤링
for i in range(1, 17):

    url = 'http://www.isaac-toast.co.kr/bbs/board.php?bo_table=branches&sca=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&page='+str(i)
    browser.implicitly_wait(3)

    browser.get(url)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    list = soup.select('tr')
    list1 = list[1:]

    # 지정명 리스트 변수
    names = []
    # 주소 리스트 변수
    address = []
    # 전화번호 리스트 변수
    tel = []

    for row in list1:
        cut_str = str(row.select('td.td_date')[1])
        names.append(cut_unness(cut_str))
        cut_str = str(row.select('td.td_subject')[0])
        address.append(cut_unness(cut_str))
        cut_str = str(row.select('td.td_date')[2])
        tel.append(cut_unness(cut_str))

    total.extend([[name,address,tel] for name,address,tel in zip(names, address, tel)])

# DataFrame 형식으로 데이터 변환
df = pd.DataFrame(total, columns=["지정명","주소","연락처"])

# csv 파일 형태로 데이터 저장
df.to_csv('C:\\myPyCode\issac_data.csv', index = False, encoding = 'cp949')

# xlsx 파일 형태로 데이터 저장
excel_writer = pd.ExcelWriter('C:\\myPyCode\issac_data.xlsx', engine ='xlsxwriter')
df.to_excel(excel_writer, index=False, sheet_name='이삭토스트')
excel_writer.save()