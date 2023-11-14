import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Data Visualizer", layout="wide")

if "data" not in st.session_state:
    st.session_state.data = None

st.title("Data Visualizer")
st.markdown("Use this streamlit app to make your own scatterplot using any data")

def maintain():
    if st.session_state.csv is not None:
        st.session_state.data = pd.read_csv(st.session_state.csv)
    else:
        st.session_state.data = None

st.file_uploader("Select your local csv file", type=["csv"], key="csv", on_change=maintain)
if st.session_state.data is None:
    st.stop()

st.session_state.data

selected_x_var = st.selectbox(
    "What do you want the x variable to be?",
    st.session_state.data.select_dtypes(exclude=["object"]).columns
)

selected_y_var = st.selectbox(
    "What about the y variable?",
    st.session_state.data.select_dtypes(exclude=["object"]).columns
)

selected_color_var = st.selectbox(
    "What about the color?",
    st.session_state.data.select_dtypes(include=["object"]).columns
)

col1,col2,col3 = st.columns(3)

with col1:
    st.metric("X Mean with Variance",
              value=round(np.mean(st.session_state.data[selected_x_var]),3),
              delta=np.var(st.session_state.data[selected_x_var]), delta_color="off")
    
with col2:
    st.metric("Y Mean with Variance",
              value=round(np.mean(st.session_state.data[selected_y_var]),3),
              delta=np.var(st.session_state.data[selected_y_var]), delta_color="off")
    
with col3:
    st.metric("Color Unique Values", value=len(np.unique(st.session_state.data[selected_color_var].dropna())))

with st.spinner("Patience, my friend.."):
    fig = px.scatter(st.session_state.data, x=selected_x_var, y=selected_y_var, color=selected_color_var)
    st.plotly_chart(fig, use_container_width=True)

st.download_button("Download", data=st.session_state.data.to_csv().encode("utf-8"), file_name="large_df.csv", mime="text/csv")

