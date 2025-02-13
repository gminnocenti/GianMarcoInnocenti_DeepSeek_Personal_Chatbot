import os
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader

# Load environment variables
load_dotenv()
api_key: str = os.getenv('key')

# Initialize model
model: str = "deepseek-r1-distill-llama-70b"
deepseek = ChatGroq(api_key=api_key, model_name=model)

# Attach parser to the model
parser = StrOutputParser()
deepseek_chain = deepseek | parser

# Load your data (the 'data.txt' file)
loader = TextLoader('data.txt', encoding='utf-8')
data = loader.load()

# Prepare your template
template = """
You are an AI-powered chatbot designed to provide 
information and assistance for people
based on the context provided to you only.
Don't in any way make things up.

Context: {context}
Question: {question}
"""

#Prompt the user for a question
user_question = str(input("Please enter your question: "))

# Create the final prompt by injecting both context and user question
prompt = template.format(context=data, question=user_question)

# Send prompt to the model
answer = deepseek_chain.invoke(prompt)

# Remove <think>...</think> sections from the response
answer_no_think = re.sub(r"<think>.*?</think>", "", answer, flags=re.DOTALL).strip()

print("\n=== Model's Response ===")
print(answer_no_think)
