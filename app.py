import streamlit as st
import os
from pdf2docx import Converter

st.title("📄 PDF to Word Converter")
st.write("Upload a PDF file below to convert it into an editable Word document (.docx).")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    input_pdf_path = "temp_uploaded.pdf"
    output_docx_path = "converted_output.docx"
    
    with open(input_pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    st.success("PDF uploaded successfully!")
    
    if st.button("Convert to Word"):
        with st.spinner("Converting... Please wait."):
            try:
                # Convert PDF to Word
                cv = Converter(input_pdf_path)
                cv.convert(output_docx_path, start=0, end=None)
                cv.close()
                
                st.success("Conversion Complete!")
                
                # Provide download button for the converted Word file
                with open(output_docx_path, "rb") as docx_file:
                    st.download_button(
                        label="Download Converted Word Document",
                        data=docx_file,
                        file_name="converted_document.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            except Exception as e:
                st.error(f"An error occurred during conversion: {e}")
