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

if st.button("Say hello"):
    st.write("Hello there!")

agree = st.checkbox("I agree")
if agree:
    st.write("Great!")

gender = st.radio("Select gender", ("Male", "Female", "Other"))
st.write(f"You selected: {gender}")

option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

age = st.slider("Select your age", 0, 100, 25)
st.write(f"You are {age} years old")

num = st.number_input("Enter a number", 0, 100)
st.write(f"The square is: {num**2}")