import streamlit as st
import pandas as pd
import matplotlib.pyplot as pyp
import numpy as np

st.title('IRIS FLOWER DASHBOARD')
st.divider()
st.sidebar.header('Discription')
df=pd.read_csv("iris.csv")
st.dataframe(df)
st.table(df)
col1,col2=st.columns(2)
with col1:
    st.header("Pie chart of species")
    
with col2:
    st.header('Bar chart of species')
st.header('line chart')   
