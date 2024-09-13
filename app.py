import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

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

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

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

                # Crear el almacenamiento de vectores
                vectorstore = get_vectorstore(text_chunks)

                # Crear chain conversation
                conversation = get_conversation_chain(vectorstore)

if __name__ == "__main__":
    main()