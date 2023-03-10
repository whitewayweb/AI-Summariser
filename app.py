import streamlit as st
import numpy as np

st.set_page_config(
    page_title="AI Summarizer",
    page_icon="🎈",
)

def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

c30, c31, c32 = st.columns([2.5, 1, 3])

with c30:
    # st.image("logo.png", width=400)
    st.title("🔑 AI Summarizer")
    st.header("")

with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """     
-   The *AI Summarizer* app is an easy-to-use interface built in Streamlit for text summarization purpose!
-   It uses BERT model for text summarization of web page content scrapped using Beautifulsoup library.
	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("## **📌 Paste document **")