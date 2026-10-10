# 暂时禁用RAG功能，避免嵌入模型报错
# 后续需要时再取消注释
"""
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os

API_KEY = "ark-de4c62ac-29d7-42e5-8890-3c5dac9c06b1-b7fd5"
BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
MODEL = "doubao-seed-2-0-pro-260215"
EMBEDDING_MODEL = "doubao-embedding-250315"

embedding = OpenAIEmbeddings(
    model=EMBEDDING_MODEL,
    api_key=API_KEY,
    base_url=BASE_URL,
    timeout=60
)

llm = ChatOpenAI(
    model=MODEL,
    api_key=API_KEY,
    base_url=BASE_URL,
    temperature=0,
    timeout=60
)

def build_knowledge():
    if not os.listdir("knowledge"):
        with open("knowledge/guide.txt", "w", encoding="utf-8") as f:
            f.write("面试技巧：自我介绍1分钟，突出项目经验；技术问题结合实际项目回答；态度诚恳。")
        with open("knowledge/bank.txt", "w", encoding="utf-8") as f:
            f.write("1. 自我介绍？2. 你的项目难点？3. 职业规划？")

    docs = []
    for file in os.listdir("knowledge"):
        path = f"knowledge/{file}"
        loader = TextLoader(path, encoding="utf-8")
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500)
    splits = splitter.split_documents(docs)
    db = FAISS.from_documents(splits, embedding)
    db.save_local("vector_store")

def search_knowledge(query):
    if not os.path.exists("vector_store/index.faiss"):
        build_knowledge()
    db = FAISS.load_local("vector_store", embedding, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 2})
    return retriever.get_relevant_documents(query)
"""

# 空函数占位，避免导入报错
def build_knowledge():
    pass

def search_knowledge(query):
    return []