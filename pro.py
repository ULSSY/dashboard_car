import streamlit as st
import pandas as pd

def main():
    df=pd.read_csv('data/OBS_계절관측_2.csv')

    print(df) 

    
    st.dataframe(df)
if __name__== '__main__':
    main()