import streamlit as st
from spell import check_spelling


st.title('Spell Checker')


input_text = st.text_area("Enter the text to check:", "")


if st.button('Check Spelling'):
    if input_text:
        results = check_spelling(input_text)
        if results:
            for misspelled_word, suggestion in results:
                st.write(f"Misspelled Word: **{misspelled_word}**")
                st.write(f"Suggested Correction: **{suggestion}**")
        else:
            st.write("No spelling mistakes found!")
    else:
        st.write("Please enter some text.")
