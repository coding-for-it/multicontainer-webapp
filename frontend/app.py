import streamlit as st
import requests
import pandas as pd

st.title("User Data Dashboard")

response = requests.get("http://backend:8000/data")

if response.status_code == 200:
    data = response.json()["data"]
    
    df = pd.DataFrame(data, columns=["ID", "Name"])
    st.table(df)

else:
    st.write("Error fetching data")