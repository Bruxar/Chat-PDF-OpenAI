import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat con multiples PDFs", page_icon=":books:")

    st.header("Chat con multiples PDFs :books:") 
    st.text_input("Haz tu pregunta:")

    with st.sidebar:
        st.subheader("Tus documentos")
        pdf_docs = st.file_uploader(
            "Sube tus archivos PDF", accept_multiple_files=True)
        if st.button("Cargar"):
            with st.spinner("Procesando documentos..."):
                # Obtener el texto del pdf
                raw_text = get_pdf_text(pdf_docs)

                # Obtener el chunck de texto
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)
                # Crear el almacenamiento de vectores

if __name__ == "__main__":
    main()