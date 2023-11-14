import streamlit as st
import time
import numpy as np
import plotly.express as px
import pandas as pd

with st.form("Form 1"):
    f=st.text_input("First Name")
    l=st.text_input("Last Name")
    e=st.text_input("Email")
    state = st.form_submit_button("Submit")
    if state:
        if f == "" or l == "" or e == "":
            st.warning("Missing Fields")
        else:
            st.success("Entered Successfully")

with st.sidebar:
    st.write("Sidebar")

#with st.spinner("Wait..."):
#    time.sleep(5)
#    st.write("Done")

with st.expander("Open to see expander"):
    st.write("IT works")

tab1, tab2 = st.tabs(["tab1","tab2"])

with tab2:
    st.write("Tab b")
tab1.write("Tab a")


x = np.linspace(0,10,100)
st.write(x)
plot = px.line(pd.DataFrame({"x":x, "sin":np.sin(x), "cos":np.cos(x)}), x="x", y=["sin","cos"])
st.plotly_chart(plot)

st.line_chart(pd.DataFrame({"x":x, "sin":np.sin(x), "cos":np.cos(x)}), x="x", y=["sin","cos"])
st.area_chart(pd.DataFrame({"x":x, "sin":np.sin(x), "cos":np.cos(x)}), x="x", y=["sin","cos"])
st.bar_chart(pd.DataFrame({"x":x, "sin":np.sin(x), "cos":np.cos(x)}), x="x", y=["sin","cos"])

st.balloons()