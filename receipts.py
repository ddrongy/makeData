# 라이브러리 import
import requests
import pprint
import json

# url 입력
url = 'http://openapi.foodsafetykorea.go.kr/api/d5930f67722c49129a56/COOKRCP01/json/1/1063'

# url 불러오기
response = requests.get(url)

#데이터 값 출력해보기
contents = response.text
json_ob = json.loads(contents)
print(json_ob)

# body = json_ob['COOKRCP01']['row']

# receipt_name = [ e["RCP_NM"] for e in body ]

# receipt_img = [ e["ATT_FILE_NO_MK"] for e in body ]
#ATT_FILE_NO_MK
# print(receipt_name)
# print(receipt_img)