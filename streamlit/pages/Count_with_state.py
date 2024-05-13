import streamlit as st

st.title("Click button with state")
st.markdown(
    """\
This app uses the session state to store the number of time the button has been pressed.
The session state is essentially a dictionary where we can store simple Python values between runs of the same app.
"""
)

if "count" not in st.session_state:
    st.session_state["count"] = 0

button = st.button(label="Click me")

if button:
    st.session_state["count"] += 1

st.write(f"The button has been pressed {st.session_state['count']} times")
