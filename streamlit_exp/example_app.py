import streamlit as st
import pandas as pd
import numpy as np


st.title("Example APP")

st.write("Here's our first attempt at using data to create a table:")
st.write(
    pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
)

my_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(my_chart_data)


x = st.slider("x", value=0)  # 👈 this
st.write(x, "squared is", x * x)

st.session_state
