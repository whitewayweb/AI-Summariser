import re

# Import from 3rd party libraries
import streamlit as st
import streamlit.components.v1 as components
from summarizer import Summarizer, TransformerSummarizer

from util import Util

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

st.title("🔑 AI Summarizer")
st.header("")

with st.expander("ℹ️ - About this app", expanded=False):

    st.write(
        """     
-   The *AI Summarizer* app is an easy-to-use interface built in Streamlit for text summarization purpose!
-   It uses BERT model for text summarization of web page content scrapped using Beautifulsoup library.
	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("## **📌 Enter Website URL to scrap and summarize **")

with st.form(key="my_form"):
    #ce, c1, ce, c2, c3 = st.columns([0.07, 1, 0.07, 5, 0.07])
    # with c1:
    #     ModelType = st.radio(
    #         "Choose your model",
    #         ["BERT (Default)", "DistilBERT", "Flair"],
    #         help="At present, you can choose between following models. More to come!",
    #     )

    #with c2:
    url = st.text_input("Paste your webpage URL below",)
    submit_button = st.form_submit_button(label="✨ Get me summary !")


if not submit_button:
    st.stop()

with st.spinner("Generating summary details..."):
    st.header("")

    util = Util(url)
    soup = util.scrap()
    title = soup.title.get_text() # Article Title
    pub_date = util.getDate(soup)
    des = util.getDescription(soup)
    publisher = util.getPublisher(soup)
    summary = util.getSummary(soup)
    imageurl = util.getImage(soup)

    if imageurl != None:
        image = f"<img src ='{imageurl}' width='100%' />"
    else:
        image = ""
    

    st.markdown(
        " ".join([
            "<h2>🎈 Summary Details:</h2>",
            "<table class='summary'>",
            "<tr>",
            "<th>Title</th>",
            f"<td class='font-title text-bold'>{title}</td>",
            "</tr>",
            "<tr>",
            "<th>Publisher</th>",
            f"<td class='font-title text-bold'>{publisher}</td>",
            "</tr>",
            "<tr>",
            "<th>Summary</th>",
            f"<td class=''>{summary}</td>",
            "</tr>",
            "<tr>",
            "<th>Description</th>",
            f"<td class=''>{des}</td>",
            "</tr>",
            "<tr>",
            "<th>Image</th>",
            f"<td class=''>{image}</td>",
            "</tr>",
            "</table>"
        ]),
        unsafe_allow_html=True
    )


    st.markdown("""---""")
    # col1, col2 = st.columns(2)
    # with col1:
    #     st.markdown(
    #         "**Other Streamlit apps by [@alpeshkumar](https://alpeshkumar.com/)**"
    #     )
    #     st.markdown("[Twitter Wrapped](https://twitter-likes.streamlit.app)")
    #     st.markdown("[Content Summarizer](https://web-summarizer.streamlit.app)")
    #     st.markdown("[Code Translator](https://english-to-code.streamlit.app)")
    #     st.markdown("[PDF Analyzer](https://pdf-keywords.streamlit.app)")
    # with col2:
    #     st.write("If you like this app, please consider to")
    #     components.html(
    #     """
    #         <form action="https://www.paypal.com/donate" method="post" target="_top">
    #             <input type="hidden" name="hosted_button_id" value="8JJTGY95URQCQ" />
    #             <input type="image" src="https://pics.paypal.com/00/s/MDY0MzZhODAtNGI0MC00ZmU5LWI3ODYtZTY5YTcxOTNlMjRm/file.PNG" height="35" border="0" name="submit" title="Donate with PayPal" alt="Donate with PayPal button" />
    #             <img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
    #         </form>
    #     """,
    #     height=45,
    #     )
    #     st.write("so I can keep it alive. Thank you!")