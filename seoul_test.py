import requests
import pandas as pd

SEOUL_API_AUTH_KEY = '63486e74646c6174383278774f7359'

def seoul_open_api_data(url,service):
    data_list = list
    try:
        result_dict = requests.get(url).json()
        result_data = result_dict[service]
        code = result_data['RESULT']['CODE']
        if code == 'INFO-000':
            data_list = result_data['row']
    except:
        pass
    return data_list

# 서울시 행정구역 시군구 정보(좌표계: WGS1984)
sgg_url = 'http://openapi.seoul.go.kr:8088/{}/json/SdeTlSccoSigW/1/25'.format(SEOUL_API_AUTH_KEY)
sgg_data_list = seoul_open_api_data(sgg_url, 'SdeTlSccoSigW')

columns = ['SIG_CD','SIG_KOR_NM','LAT','LNG']
sgg_df = pd.DataFrame(data = sgg_data_list, columns=columns)
sgg_df.columns = ['시군구코드','시군구명','위도','경도']
print(sgg_df)


# 서울시 주민등록인구 (구별) 통계
people_url = 'http://openapi.seoul.go.kr:8088/{}/json/octastatapi419/2/26/2019.3-4'.format(SEOUL_API_AUTH_KEY)
people_data_list = seoul_open_api_data(people_url, 'octastatapi419')

columns = ['GIGAN','JACHIGU','SEDAE','GYE_1']
people_df = pd.DataFrame(data=people_data_list, columns = columns)
people_df.columns = ['기간','자치구','세대수','인구 합']
print(people_df)


# https://data.seoul.go.kr/dataList/104/A/2/datasetView.do
# 서울시 사업체현황 (산업대분류별/동별) 통계
company_url = 'http://openapi.seoul.go.kr:8088/{}/json/octastatapi104/1/500'.format(SEOUL_API_AUTH_KEY)
company_data_list = seoul_open_api_data(company_url, 'octastatapi104')
print(company_data_list[1])

columns = ['GIGAN', 'JACHIGU','DONG', 'SAEOPCHESU_1']
company_df = pd.DataFrame(data=  company_data_list, columns=columns)
company_df.columns = ['기간', '자치구','동', '사업체 수']
comp_df = company_df[company_df['동']=='소계']
print(comp_df)