import streamlit as st
import random
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os

# Mock data for fallback when API fails
MOCK_DATA = {
    "India": {
        "state_name": "Rajasthan", 
        "description": "Known as the 'Land of Kings', Rajasthan is a mosaic of desert landscapes, majestic forts, and vibrant heritage.",
        "places": "Hawa Mahal, Amber Fort, City Palace, Jantar Mantar, Jal Mahal, Nahargarh Fort, Albert Hall Museum"
    },
    "USA": {
        "state_name": "California", 
        "description": "From Hollywood glamour to Silicon Valley innovation, the Golden State offers diverse landscapes and iconic culture.",
        "places": "Golden Gate Bridge, Yosemite National Park, Hollywood Sign, Disneyland Park, Alcatraz Island, Griffith Observatory, Santa Monica Pier"
    },
    "China": {
        "state_name": "Beijing", 
        "description": "A city where ancient dynasties meet modern futurism, Beijing is the beating heart of Chinese history.",
        "places": "Great Wall of China, Forbidden City, Temple of Heaven, Summer Palace, Tiananmen Square, Lama Temple, Beihai Park"
    },
    "Brazil": {
        "state_name": "Rio de Janeiro", 
        "description": "Famed for its festive carnival spirit, breathtaking beaches, and the iconic Christ the Redeemer.",
        "places": "Christ the Redeemer, Sugarloaf Mountain, Copacabana Beach, Tijuca National Park, Escadaria Selarón, Maracanã Stadium, Ipanema Beach"
    },
    "Canada": {
        "state_name": "British Columbia", 
        "description": "A coastal paradise offering a perfect blend of modern urban living and wild, untamed nature.",
        "places": "Stanley Park, Capilano Suspension Bridge, Granville Island, Butchart Gardens, Whistler Blackcomb, Royal BC Museum, Gastown Steam Clock"
    },
    "Italy": {
        "state_name": "Tuscany", 
        "description": "The cradle of the Renaissance, renowned for its art, rolling hills, and world-class culinary traditions.",
        "places": "Leaning Tower of Pisa, Uffizi Gallery, Florence Cathedral, Piazza del Campo, Ponte Vecchio, Boboli Gardens, Val d'Orcia"
    },
    "Singapore": {
        "state_name": "Singapore", 
        "description": "A futuristic city-state where nature and technology coexist in perfect, breathtaking harmony.",
        "places": "Marina Bay Sands, Gardens by the Bay, Sentosa Island, Universal Studios Singapore, Singapore Zoo, Orchard Road, China Town"
    }
}

def get_llm():
    """Initialize LLM with error handling for missing secrets"""
    try:
        api_key = st.secrets.get("GROQ_API_KEY")
        if not api_key or api_key == "your-api-key-here":
            return None
            
        return ChatGroq(
            model_name="llama-3.1-8b-instant",
            temperature=0.7,
            timeout=10, # Reduced timeout for faster fallback
            groq_api_key=api_key,
            max_tokens=100
        )
    except Exception:
        return None

def generate_state_destinations(country):
    try:
        llm = get_llm()
        
        # If no valid LLM or API key, raise exception to trigger fallback
        if not llm:
            raise Exception("No valid API key found")

        prompt_template_state = PromptTemplate(
            input_variables=['country'],
            template="Give the name of a state from {country}. Just the name."
        )

        prompt_template_desc = PromptTemplate(
            input_variables=['state'],
            template="Give a short, fascinating 1-sentence description of {state} for a travel app. Max 15 words."
        )

        prompt_template_places = PromptTemplate(
            input_variables=['state'],
            template="Give ONLY names of 7 famous tourist attractions in the {state}, separated by commas."
        )

        # Chain 1: Get State Name
        state_name_response = (prompt_template_state | llm).invoke({"country": country})
        state_name = state_name_response.content.strip() if hasattr(state_name_response, "content") else state_name_response.strip()

        # Chain 2: Get Description
        desc_response = (prompt_template_desc | llm).invoke({"state": state_name})
        description = desc_response.content.strip() if hasattr(desc_response, "content") else desc_response.strip()

        # Chain 3: Get Places
        places_name_response = (prompt_template_places | llm).invoke({"state": state_name})
        places = places_name_response.content.strip() if hasattr(places_name_response, "content") else places_name_response.strip()
        
        return {
            "state_name": state_name,
            "description": description,
            "places": places
        }

    except Exception as e:
        # Fallback to mock data
        return MOCK_DATA.get(country, {
            "state_name": f"Top Destinations in {country}",
            "description": f"Explore the majestic beauty and rich culture hidden within {country}.",
            "places": "Famous Landmark 1, Historical Site 2, National Park 3, Popular Beach 4, City Museum 5, Iconic Tower 6, Central Square 7"
        })





