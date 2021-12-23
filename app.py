import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle

from eda_app import run_eda_app
from ml_app import run_ml_app
# 자동으로 비주얼 코드가 임포트 해준다
def main():
    st.title('교통사고 현황 확인하기')

    #사이드바 메뉴
    menu=['Home','데이터검색','데이터분석']
    choice=st.sidebar.selectbox('메뉴',menu)

    if choice=='Home':
        
        st.write('교통사고 현황을 확인하실 수 있습니다.')
        st.write('왼쪽의 사이드바에서 선택하세요')

    elif choice =='데이터검색' :
        run_eda_app()
    elif choice == '데이터분석':
        run_ml_app()
if __name__ =='__main__':
    main()
