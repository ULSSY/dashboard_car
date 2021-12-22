import streamlit as st
import pandas as pd
import numpy as np
import joblib 


def run_ml_app():
    st.subheader('Machine learning 예측')

    #1.유저한테,데이터를 입력받습니다.
    gender=st.radio('성별을 입력하세요',['남자','여자'])
    if gender == '남자':
        gender_number=1
    elif gender=='여자':
         gender_number=0

    age=st.number_input('나이 입력',min_value=1,max_value=120)
    
    salary=st.number_input('연봉입력',min_value=10000)
    
    debt=st.number_input('카드 빛 입력',min_value=0)
    worth=st.number_input('자산 입력',min_value=10000)
    
    print(gender_number,age,salary,debt,worth)
    