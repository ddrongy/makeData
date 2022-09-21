import streamlit as st
import pandas as pd
import numpy as np
# 라이브러리 import
import requests
import pprint
import json


if 'num' not in st.session_state:
    st.session_state.num = 1
    st.session_state.strIdx = 10
    st.session_state.endIdx = 10

st.title('레시피 조사를 위한 ~')
st.write('이중에서 내가 만들었을거 같다라고 생각한 음식 고르기')

while True :

    placeholder = st.empty()
    placeholder2 = st.empty()

    num = st.session_state.num
    print(st.session_state.strIdx, st.session_state.endIdx)

    if placeholder2.button('end', key=num):
        placeholder2.empty()
        # df = pd.DataFrame(st.session_state.data)
        # st.dataframe(df)
        break
    else :
        url = 'http://openapi.foodsafetykorea.go.kr/api/d5930f67722c49129a56/COOKRCP01/json/' + str(st.session_state.strIdx) + '/' + str(st.session_state.endIdx)

        # url 불러오기
        response = requests.get(url)

        #데이터 값 출력해보기
        contents = response.text
        json_ob = json.loads(contents)
        body = json_ob['COOKRCP01']['row']

        receipt_name = [ e["RCP_NM"] for e in body ]
        receipt_img = [e["ATT_FILE_NO_MK"] for e in body]

        for i in range(10):
            locals()['option_'+str(i)] = st.checkbox(receipt_name[i])
            st.image(receipt_img[i], width = 200)

        st.session_state.strIdx += 10
        st.session_state.endIdx += 10

        known_variables = option_0 + option_1 + option_2 + option_3 + option_4 + option_5 + option_6 + option_7 + option_8 + option_9

        # if known_variables < 1:
        #     st.write('적어도 한개 이상은 골라주세요 ... ~')

        with placeholder.form(key=str(num)):
            if st.form_submit_button('next'): 
                st.session_state.strIdx += 10
                st.session_state.endIdx += 10
                st.session_state.num += 1
                placeholder.empty()
                placeholder2.empty()
            else :
                st.stop()