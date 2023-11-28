import streamlit as st
import pandas as pd
import duckdb

st.write('''
# SQL SRS
Spaced Repetition System SQL Practice
''')


option = st.selectbox(
    "What would you like to review?",
    ("Joins", "Groupby", "Window Functions"),
    index = None,
    placeholder = "Select contact method...",
)

st.write("You selected : ", option)

data = {"a" : [1, 2, 3], "b" : [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3, = st.tabs(["Cat", "Dog", "Owl"])

with tab1 :
    st.header('A cat')
    st.image("https://static.streamlit.io/examples/cat.jpg", width = 200)

    sql_query = st.text_area(label = "Insert your sql query")
    result = duckdb.query(sql_query)

    st.write("Inserted Request : {}".format(sql_query))
    st.dataframe(result.df())

with tab2 :
    st.header('A Dog')
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3 :
    st.header(' An owl')
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)