import streamlit as st
from dhlab import Ngram


st.title("Word frequencies")
st.markdown("Write words and see how their use in Norwegian books change over time.")


words = st.text_input("Key words", "Skriv inn ord")
from_year, to_year = st.select_slider(
    "Year", options=range(1800, 2000, 10), value=(1950, 1990)
)
is_relative = st.toggle(
    "Relative frequency",
    value=True,
    help="If toggled, the frequency is given as percent of total words that year. If not toggled, the frequency is given as absolute word counts.",
)


mode = "relative"
if not is_relative:
    mode = "absolute"


ngram = Ngram(
    words=words.split(),
    from_year=from_year,
    to_year=to_year,
    mode=mode,
    doctype="bok",
).frame


st.line_chart(ngram)
st.dataframe(ngram)
