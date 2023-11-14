import streamlit as st
import pandas as pd

st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Text")
st.markdown("<h4> HTML stuff </h4>", unsafe_allow_html=True)
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json = {"a":[1,2,3], "b":[4,5,6]}
st.json(json)
code="""
print("Code")
a = 3
"""
st.code(code, language="python")
table = pd.DataFrame(json)
st.write("## H2")
st.table(table)
st.dataframe(table)
st.metric(label="Speed", value="120ms", delta="1.4")
st.image("image.gif", caption="Michael Scott", use_column_width=True)
st.audio("audio.mp3")

if "Button" not in st.session_state:
    st.session_state["Button"] = False
check = st.checkbox("Checkbox", value=True)

if st.session_state["Button"]:
    st.write("Checked")
else:
    st.write("Unchecked")

def clicked():
    st.session_state["Button"] = True

st.button("Button", on_click=clicked, key="b")

if st.session_state["Button"]:
    st.write("Button clicked")

st.radio("Radio", options=[1,2,3])
st.radio("Radio", options=[1,2,3], key="radio2")
st.selectbox("Selecbox", options=[1,2,3])
multi = st.multiselect("Multiselect", options=[1,2,3])
st.write(multi)