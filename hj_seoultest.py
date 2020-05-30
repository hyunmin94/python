# 0. 함수 생성 및 변수 입력

import requests
import pandas as pd

#서울열린데이터광장 API 코드
SEOUL_API_AUTH_KEY = '63486e74646c6174383278774f7359'


#서울열린데이터광장 OPEN API 호출 공통 함수
def seoul_open_api_data(url, service):
    data_list = None
    try :
        result_dict = requests.get(url).json()              #서울열린데이터광장 OPEN API 호출
        result_data = result_dict[service]                  #각 목록 결과 딕셔너리 데이터 값 가져오기
        code = result_data['RESULT']['CODE']
        if code == 'INFO-000' :
            data_list = result_data['row']
    except :
        pass
    return data_list


############################################################################################################

# 1. 서울시 행정구역 시군구

# 공통 함수를 이용해 서울시 행정구역 시군구 OPEN API 호출, 리스트 생성
sgg_url = 'http://openapi.seoul.go.kr:8088/{}/json/SdeTlSccoSigW/1/25'.format(SEOUL_API_AUTH_KEY)
sgg_data_list = seoul_open_api_data(sgg_url, 'SdeTlSccoSigW')
sgg_data_list[0]


# 결과 데이터를 pandas의 df로 변환
columns = ['SIG_CD', 'SIG_KOR_NM', 'LAT', 'LNG']
sgg_df = pd.DataFrame(data=sgg_data_list, columns = columns)
print(sgg_df.head())


# df의 컬럼명 변경
sgg_df.columns = ['시군구코드', '시군구명', '위도', '경도']
print(sgg_df.head())


#df 요약 정보 확인
print(sgg_df.info())



############################################################################################################

# 2. 서울시 주민등록인구수

# 공통 함수를 이용해 서울시 주민등록인구수 OPEN API 호출, 리스트 생성
## 가장 최근 데이터는 2020년 1/4분기이지만 open api로 받을 수 있는 최대치는 2019년 3/4분기임
people_url = 'http://openapi.seoul.go.kr:8088/{}/json/octastatapi419/1/26/2019.3-4'.format(SEOUL_API_AUTH_KEY)
people_data_list = seoul_open_api_data(people_url, 'octastatapi419')
people_data_list[0]


# 자치구 = '합계'인 행 제거
pp_data_list = people_data_list[1:]


# 결과 데이터를 pandas의 df로 변환
columns = ['JACHIGU', 'GYE_1', 'GYE_2', 'GYE_3']
people_df = pd.DataFrame(data=pp_data_list, columns = columns)
print(people_df.head())


# df의 컬럼명 변경
people_df.columns = ['자치구', '총 인구 수', '한국인', '외국인']
print(people_df.head())


#df 요약 정보 확인
print(people_df.info())



############################################################################################################

# 3. 서울시 사업체 및 종사자 수

# 공통 함수를 이용해 서울시 주민등록인구수 OPEN API 호출, 리스트 생성
## 가장 최근 데이터는 2018년지만 open api로 받을 수 있는 최대치는 2015년임
company_url = 'http://openapi.seoul.go.kr:8088/{}/json/octastatapi96/1/450/2015'.format(SEOUL_API_AUTH_KEY)
com_data_list = seoul_open_api_data(company_url, 'octastatapi96')
com_data_list[0:5]


# 구별 데이터로 변환
company_data_list = []
for i in com_data_list :
    if i['JACHIGU'] != '합계' and '소계' in i['DONG']:
        company_data_list.append(i)



# 결과 데이터를 pandas의 df로 변환
columns = ['JACHIGU', 'SAEOPCHESU', 'JONGSAJASU']
company_df = pd.DataFrame(data=company_data_list, columns = columns)
print(company_df.head())


# df의 컬럼명 변경
company_df.columns = ['자치구', '사업체 수', '종사자 수']
print(company_df.head())


#df 요약 정보 확인
print(company_df.info())

