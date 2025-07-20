import streamlit as st

st.title("Demo app")
st.header("My header")
st.subheader("My subheader")
st.write("Hello, streamlit")
st.markdown("This is random text")

import pandas as pd

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
st.dataframe(df)

st.table(df)
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
st.map()

st.metric("Temperature", "70 °F", "1.2 °F")
