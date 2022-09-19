import streamlit as st
import pandas as pd
import requests
import json

if 'num' not in st.session_state:
    st.session_state.num = 1
    st.session_state.strIdx = 0
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

        receipt_name = [ e["RCP_NM"] for e in body ]
        receipt_img = [e["ATT_FILE_NO_MK"] for e in body]
        if placeholder2.button('end', key=num):
            placeholder2.empty()
            df = pd.DataFrame(st.session_state.data)
            st.dataframe(df)
            break
        else:
            with placeholder.form(key=str(num)):
                # new_student = NewStudent(page_id=num)        
                for i in range(10):
                    locals()['option_'+str(i)] = st.checkbox(receipt_name[i])
                    st.image(receipt_img[i], width = 200)
                if st.form_submit_button('register'):                
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
