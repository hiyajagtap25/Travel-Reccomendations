import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm=ChatGroq (
    model_name="llama-3.1-8b-instant",
    temperature=0.7,
    timeout=80,
    groq_api_key=st.secrets["GROQ_API_KEY"],
    max_tokens=100
    
)

def generate_state_destinations(country):

    prompt_template_state=PromptTemplate(
        input_variables=['country'],
        template="Give the name of a state from {country}"
    )

    prompt_template_places=PromptTemplate(
        input_variables=['state'],
        template="Give ONLY names of 7 famous tourist attractions in the {state}"
    )


    state_name_response=(prompt_template_state|llm).invoke({"country":country})

    if hasattr(state_name_response, "content"):
        state_name = state_name_response.content.strip()
    else:
        state_name = state_name_response.strip()

    places_name_response=(prompt_template_places|llm).invoke({"state":state_name})

    if hasattr(places_name_response,"content"):
        places=places_name_response.content.strip()
    else:
        places=places_name_response.strip()

    
    return{
        "state_name": state_name,
        "places": places

    }





