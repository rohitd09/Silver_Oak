from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader("resume.pdf")

# documents = loader.load()
# # print(documents)

from langchain_text_splitters import RecursiveCharacterTextSplitter

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=200,
#     chunk_overlap=50
# )

# chunks = splitter.split_documents(documents)

# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i + 1}:")
#     print(chunk.page_content)
#     print("-" * 50)

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    embedding_function=embeddings,
    collection_name="resume_col",
    persist_directory="chroma_db"
)

# vector_store.add_documents(chunks)

# from llm import get_llm

# from langchain_classic.chains import RetrievalQA

# llm_model = get_llm()

# db_retriever = vector_store.as_retriever(
#         search_kwargs={"k": 3}
#     )

# retrieved_chunks = db_retriever.invoke("Skills of the candidate?")
# print("Retrieved Chunks:")
# for i, chunk in enumerate(retrieved_chunks):
#     print(f"Chunk {i + 1}:")
#     print(chunk.page_content)
#     print("-" * 50)

# rag_chain = RetrievalQA.from_chain_type(
#     llm=llm_model,
#     retriever=db_retriever
# )

# response = rag_chain.invoke("Skills of the candidate?")

# print(response)