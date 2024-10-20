#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
from urllib.request import urlretrieve
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama


# Helper functions
def load_excel_data(file_path: str):
    loader = UnstructuredExcelLoader(os.path.join(os.getcwd(),file_path), mode="elements")
    return loader.load()


def create_embedding_model(model_name="BAAI/bge-small-en-v1.5", device="cpu"):
    return HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs={'device': device},
        encode_kwargs={'normalize_embeddings': True}
    )


def create_vector_store(documents, embedding_model, k=16):
    vector_store = FAISS.from_documents(documents, embedding_model)
    return vector_store.as_retriever(search_type="mmr", search_kwargs={"k": k})


def create_llm_model(model_name="mistral"):
    return Ollama(model=model_name)


def create_prompt_template():
    answer_prompt_template = """Use the following pieces of context to answer the question at the end. Please follow the following rules:
    1. If you don't know the answer, don't try to make up an answer. Just say "I can't find the final answer but you may want to check the following links".
    2. If you find the answer, write the answer in a concise way with five sentences maximum with the product link.
    3. This dataset is an Excel file containing a survey commissioned by Bounce Insights asking consumers in the 
    UK various questions around how important is sustainability to consumers when they are buying products in general & how engaged are consumers with sustainable brands or products.

    {context}

    Question: {question}

    Helpful Answer:
    """
    return PromptTemplate(template=answer_prompt_template, input_variables=["context", "question"])


# SurveyAnalysis class
class SurveyAnalysis:
    def __init__(self, excel_path: str, llm_name: str = "mistral"):
        self.excel_path = excel_path
        self.embedding_model = create_embedding_model()  # Use default model
        self.llm_model = create_llm_model(llm_name)
        self.prompt_template = create_prompt_template()

    def analyze_survey(self, query: str):
        # Load the survey data from the Excel file
        documents = load_excel_data(self.excel_path)

        # Create the vector store retriever
        retriever = create_vector_store(documents, self.embedding_model)

        # Create the RetrievalQA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm_model,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt_template}
        )

        # Ask the question and retrieve the answer
        result = qa_chain.invoke({"query": query})
        return result['result']


# if __name__ == "__main__":
#     # Define the path to the Excel file and the query
#     excel_path = "./Dataset1_Sustainability_Research_Results.xlsx"
#     query = 'What is the most preferred dietary plan according to the survey mentioned in Excel?'

#     # Initialize the SurveyAnalysis class and run the analysis
#     survey_analysis = SurveyAnalysis(excel_path)
#     result = survey_analysis.analyze_survey(query)

#     # Print the result
#     print(result)
