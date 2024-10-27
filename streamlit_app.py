import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom
)

from parse import parse_with_ollama

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")
        domc = scrape_website(url)
        body = extract_body_content(domc)
        clean_body = clean_body_content(body)


        st.session_state.dom_content = clean_body
        with st.expander("View DOM Content"):
            #.text_area = Display a multi-line text input widget.
            st.text_area("DOM Content", clean_body, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        st.write("Parsing the content ..")

        dom_chunks = split_dom(st.session_state.dom_content)
        result = parse_with_ollama(dom_chunks,parse_description)
        st.write(result)
