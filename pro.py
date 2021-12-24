import streamlit as st
import pandas as pd

def main():
    df=pd.read_csv('data/Car_Purchasing_Data.csv')

    print(df) 

    
    st.dataframe(df)
if __name__== '__main__':
    main()