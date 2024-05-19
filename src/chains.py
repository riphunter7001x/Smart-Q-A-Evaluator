from src.prompt import prompt_template_for_qa, prompt_template_for_eval
from langchain_core.prompts import PromptTemplate
from src.helper import dictOutput
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Get GROQ API key from environment variables
groq_api_key = os.environ["GROQ_API_KEY"]

# Initialize ChatGroq with the GROQ API key and model
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="mixtral-8x7b-32768"
)

# Prompt template for generating question and answer
prompt_for_qa = PromptTemplate(
    input_variables=["topic"],
    template=prompt_template_for_qa
)

# Chain for generating question and answer
chain_for_qa = prompt_for_qa | llm | dictOutput()

# Prompt template for evaluation
prompt_for_eval = PromptTemplate(
    input_variables=["qa", "userAnswer"],
    template=prompt_template_for_eval
)

# Chain for evaluation
chain_for_eval = prompt_for_eval | llm
