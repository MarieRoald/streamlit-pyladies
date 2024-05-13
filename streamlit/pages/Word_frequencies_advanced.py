from typing import Literal

import pandas as pd
import streamlit as st
import plotly.express as px
from dhlab import Ngram


@st.cache_data
def get_ngram(
    words: str,
    start_year: int,
    end_year: int,
    mode: Literal["relative", "absolute"],
    doctype: Literal["bok", "avis"],
    lang: Literal["nob", "nno", "sme", "smj", "sma", "fkv"],
) -> pd.DataFrame:
    return Ngram(
        words=words.split(),
        from_year=start_year,
        to_year=end_year,
        mode=mode,
        doctype=doctype,
        lang=lang,
    ).frame.fillna(0)


st.set_page_config(page_title="Word frequencies", page_icon="📈")
st.title("Word frequencies")
st.markdown(
    "Write words and see how their use in Norwegian books and newspapers change over time."
)
st.divider()

words = st.text_input("Key words", "Skriv inn ord")
start_year, end_year = st.select_slider(
    "Year", options=range(1800, 2000, 10), value=(1950, 1990)
)

st.sidebar.header("Parameters")
is_relative = st.sidebar.toggle(
    "Relative freq uency",
    value=True,
    help="If toggled, the frequency is given as percent of total words that year. If not toggled, the frequency is given as absolute word counts.",
)

document_types = {"Books": "bok", "Newspapers": "avis"}
doctype_name = st.sidebar.selectbox("Document types", document_types.keys())
doctype = document_types[doctype_name]

if doctype == "bok":
    languages = {
        "All Norwegian languages": "nor",
        "Norwegian Bokmål": "nob",
        "Norwegian Nynorsk": "nno",
        "Northern Sámi": "sme",
        "Lule Sámi": "smj",
        "Southern Sámi": "sma",
        "Kven": "fkv",
    }
    language_name = st.sidebar.selectbox("Language", languages.keys())
    language = languages[language_name]
else:
    language = None


mode = "relative"
if not is_relative:
    mode = "absolute"

ngram = get_ngram(words, start_year, end_year, mode, doctype=doctype, lang=language)

fig = px.line(ngram, x=ngram.index, y=words.split())
fig.update_xaxes(title="Year").update_yaxes(title="Word frequency")
st.plotly_chart(fig)
st.dataframe(ngram)
