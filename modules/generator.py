from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_answer(query, relevant_chunks):
    context = "\n".join([str(chunk.page_content) for chunk in relevant_chunks])
    template = """You are a travel guide for Ethiopia.
    Use the following context to answer the question:
    {context}

    Question: {question}
    Answer:"""
    prompt = PromptTemplate(input_variables=["context", "question"], template=template)
    llm = ChatOpenAI(temperature=0)
    chain = LLMChain(llm=llm, prompt=prompt)
    answer = chain.run({"context": context, "question": query})
    return answer
