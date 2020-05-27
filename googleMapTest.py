import requests
r = requests.get('http://apis.vworld.kr/new2coord.do?q=서울특별시 서초구 서초동 서초대로74길 23&apiKey=DF50E610-13D3-392C-99C6-D4A1E1DE8512'
                 '&domain=http://map.vworld.kr/&output=json')
print(r.json())