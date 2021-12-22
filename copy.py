import streamlit as st
import pandas as pd
import numpy as np
import joblib 

    
def run_ml_app():
    st.subheader('Machine learning 예측')
    df=pd.read_csv('data/Car_Purchasing_Data.csv')
    #1.유저한테,데이터를 입력받습니다.
    gender=st.radio('성별을 입력하세요',['남자','여자'])
    if gender == '남자':
        gender_number=1
    elif gender=='여자':
         gender_number=0
    print(df.columns)
    age=st.number_input('나이 입력',min_value=df['Age'].min(),max_value=df['Age'].max())
    
    salary=st.number_input('연봉입력',min_value=df['Annual Salary'].min(),max_value=df['Annual Salary'].max())
    
    debt=st.number_input('카드 빛 입력',min_value= df['Credit Card Debt'].min(), max_value=df['Credit Card Debt'].max())
    worth=st.number_input('자산 입력',min_value=df['Net Worth'].min(), max_value=df['Net Worth'].max())
    
    print(gender_number,age,salary,debt,worth)
    
    
    #2.모델에 예측한다
    #2-1 신규데이터를 넘파이로 만든다
    
    new_data=np.array([gender_number,age,salary,debt,worth])
    new_data=new_data.reshape(1,5)
    #2-2스케일러와 인공지능을 변수로 불러온다
    scaler_X=joblib.load('data/scaler_X.pkl')
    scaler_y=joblib.load('data/scaler_Y.pkl')

    regressor=joblib.load('data/regressor.pkl')
    #2-3신규데이터를 피쳐스케일링 한다.
    new_data=scaler_X.transform(new_data)
    #2-4 인공지능에게 예측하게 한다
    y_pred=regressor.predict(new_data)
    #2-5예측한 결과는 다시 원래대로 복구해줘야 한다
    print(y_pred)
    
    y_pred=scaler_y.inverse_transform(y_pred.reshape(1,1))
    print(y_pred)
   
    #3.예측 결과를 웹 대시보드에 표시한다
    btn=st.button('예측결과보기')
    #결과가 소수점으로 나오는데 소수점 뒤 한자리까지만 나오도록
    #코드를 수정해라
    if btn:
        st.write('예측결과 {:,.1f}달러의 차를 살 수 있습니다.'.format(y_pred[0,0]))
        st.write('예측결과 {}달러의 차를 살 수 있습니다.'.format(round(y_pred[0,0],1)))
