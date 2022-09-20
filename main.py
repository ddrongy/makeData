import streamlit as st
import pandas as pd
import requests
import json

if 'num' not in st.session_state:
    st.session_state.num = 1
    st.session_state.strIdx = 1
    st.session_state.endIdx = 10
if 'data' not in st.session_state:
    st.session_state.data = []

# class NewStudent:
#     def __init__(self, page_id):
#         st.title(f"Student N°{page_id}")
#         self.name = st.text_input("Name")
#         self.age = st.text_input("Age")


def main():
    placeholder = st.empty()
    placeholder2 = st.empty()


    while True:    
        num = st.session_state.num
        url = 'http://openapi.foodsafetykorea.go.kr/api/d5930f67722c49129a56/COOKRCP01/json/' + str(st.session_state.strIdx) + '/' + str(st.session_state.endIdx)        
        response = requests.get(url)
        contents = response.text
        json_ob = json.loads(contents)
        body = json_ob['COOKRCP01']['row']
        # st.title('레시피 조사를 위한 ~')
        # st.write('이중에서 내가 만들었어봤거나 만들 수 있을거라고 생각하는 음식고르기')
        receipt_name = [ e["RCP_NM"] for e in body ]
        receipt_img = [ e["ATT_FILE_NO_MK"] for e in body]
        # print(len(receipt_name))
        # print(len(receipt_img))
        if placeholder2.button('그만!', key=num):
            placeholder2.empty()
            df = pd.DataFrame(st.session_state.data)
            st.dataframe(df)
            break
        else:
            with placeholder.form(key=str(num)):
                st.title('레시피 조사를 위한 ~')
                st.write('이중에서 내가 만들었어봤거나 만들 수 있을거라고 생각하는 음식고르기')
                # new_student = NewStudent(page_id=num)        
                for i in range(10):
                    # print(i)
                    locals()['option_'+str(i)] = st.checkbox(receipt_name[i])
                    st.image(receipt_img[i], width = 200)
                if st.form_submit_button('더 하기 ..'):                
                    # st.session_state.data.append({
                    #     'id': num, 'name': new_student.name, 'age': new_student.age})
                    for i in range(10):
                        if locals()['option_'+str(i)]:
                            st.session_state.data.append({'foodname' : receipt_name[i]})
                    st.session_state.num += 1
                    st.session_state.strIdx += 10
                    st.session_state.endIdx += 10
                    placeholder.empty()
                    placeholder2.empty()
                else:
                    st.stop()

main()
