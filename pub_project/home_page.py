import streamlit as st
import pandas as pd
import numpy as np

title = '<h1 style="font-family:sans-serif; color:Green; font-weight:bold">PUB\'s IN UNITED KINGDOM</h1>'
st.markdown(title, unsafe_allow_html=True)


st.subheader("Information about the pubs")



df1 = pd.read_csv("data\pub.csv")



# Using object notation
information = st.sidebar.selectbox(
    "Statistical Data",
    ('Number of Pub\'s','Data_shape','Head', 'Tail', 'Unique Area\'s', 'Null values', 'Describe'))

if information=='Number of Pub\'s':
    st.markdown(f'**{df1.shape[0]}**  Pubs  in  **UK**')

elif information == 'Data_shape':
    st.text('Number of rows: {}'.format(df1.shape[0]))
    st.text('Number of columns: {}'.format(df1.shape[1]))

elif information == 'Head':
    st.dataframe(df1.head())

elif information == 'Tail':
    st.dataframe(df1.tail())

elif information=='Unique Area\'s':
    st.markdown(f'Total no of unique locations where pubs are present in UK is **{len(df1.local_authority.unique())}** ')

elif information == 'Null values':
    st.markdown('**We can see that there are no null values in the data**')
    st.table(df1.isna().sum())

elif information == 'Describe':
    st.table(df1.describe())



