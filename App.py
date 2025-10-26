import streamlit as st
from language_analyzer import LanguageAnalyzer

# Streamlit page setup
st.set_page_config(page_title="Language Detection", page_icon="🌍")

st.title("🌍 Advanced NLP Language Detection")
st.write("Enter any text below, and the app will detect the language using NLP models.")

# Text input
text = st.text_area("Enter text here:", height=150)

# Button to detect language
if st.button("🔍 Detect Language"):
    if text.strip():
        analyzer = LanguageAnalyzer(text)
        try:
            detected_lang = analyzer.get_language_name()
            st.success(f"**Detected Language:** {detected_lang}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text first!")

st.markdown("---")
st.caption("Built using Streamlit and your Advanced NLP Language Detection project 💡")
