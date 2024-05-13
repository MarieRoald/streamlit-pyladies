import streamlit as st

st.title("Click button without state")
st.markdown(
    """\
This app attempts to count the number of time the button has been pressed.
However, since the count is stored in a normal Python variable, it is reinitialised to zero every time we run the app.
It can therefore not count above one.
"""
)

button = st.button(label="Click me")
count = 0
placeholder = st.empty()

if button:
    count += 1

placeholder.write(f"The button has been pressed {count} times")
