import streamlit as st
import pandas as pd

st.title("Title")
st.header('Header')
st.subheader("Subheader")
st.text("text")
st.markdown("**MARKDOWN**")
st.markdown("<h4> HTML stuff </h4>",unsafe_allow_html=True) #Script tag for javascript and Style for css
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json = {"a":[1,2,3], "b":[4,5,6]}
st.json(json)
code="""
print("Code")
a = 3"""
st.code(code,language="python")

table = pd.DataFrame(json)
st.write("## H2")
st.metric(label="Speed", value="120ms²", delta="-1.4ms²")
st.table(table)
st.dataframe(table, use_container_width=True)
st.image("image.gif", caption="Michael Scott", use_column_width=True)
#st.audio("audio.mp3")
#st.video can also be used

#check = st.checkbox("Checkbox", value=True)
#if check:
#    st.write("checked")
#else:
#    st.write("unchecked")
#def change():
#    st.write(st.session_state.checker)

check = st.checkbox("Checkbox", value=True, key="checker") # on_change=change,
st.write(st.session_state.checker)

if "clicked" not in st.session_state:
    st.session_state.clicked = False

def clicked():
    st.session_state.clicked = True
button = st.button("click", on_click=clicked)
if st.session_state.clicked:
    st.write("clicked")

st.radio("Radio", options=["1","2"])
st.selectbox("SelectBox", options=[1,2,3])
multi = st.multiselect("MultiSelect", options=[1,2,3,4,5])
st.write(multi)
