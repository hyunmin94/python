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
## http://data.seoul.go.kr/dataList/OA-11677/S/1/datasetView.do


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
## http://data.seoul.go.kr/dataList/419/S/2/datasetView.do
## 2015년 4분기 데이터


# 공통 함수를 이용해 서울시 주민등록인구수 OPEN API 호출, 리스트 생성
people_url = 'http://openapi.seoul.go.kr:8088/{}/json/octastatapi419/1/26/2015.4-4'.format(SEOUL_API_AUTH_KEY)
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
## http://data.seoul.go.kr/dataList/104/S/2/datasetView.do
## 2015년 데이터


# 공통 함수를 이용해 서울시 주민등록인구수 OPEN API 호출, 리스트 생성
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



############################################################################################################

# 4. 서울시 생활인구 수 ( 유동인구 )
## https://data.seoul.go.kr/dataList/OA-15379/S/1/datasetView.do
## 일별로 집계됨. 5/30 기준 5/25 데이터가 가장 최신


# 공통 함수를 이용해 서울시 주민등록인구수 OPEN API 호출, 리스트 생성
day_people_url = 'http://openapi.seoul.go.kr:8088/{}/json/SPOP_DAILYSUM_JACHI/1/26/20200525'.format(SEOUL_API_AUTH_KEY)
day_people_data_list = seoul_open_api_data(day_people_url, 'SPOP_DAILYSUM_JACHI')
day_people_data_list[0]


# SIGNGU_NM = '서울시' 제거
day_people_list = []
for i in day_people_data_list :
    if i['SIGNGU_NM'] != '서울시':
        day_people_list.append(i)



# 결과 데이터를 pandas의 df로 변환
columns = ['SIGNGU_NM', 'DAY_LVPOP_CO', 'NIGHT_LVPOP_CO', 'DAIL_MXMM_MVMN_LVPOP_CO']
day_people_df = pd.DataFrame(data=day_people_list, columns = columns)
print(day_people_df.head())


# df의 컬럼명 변경
day_people_df.columns = ['자치구', '주간인구수(09~18)', '야간인구수(19~08)']
print(day_people_df.head())


#df 요약 정보 확인
print(day_people_df.info())


