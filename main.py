import streamlit as st # type: ignore
import functions as fn


st.title("Travel Recommendation")

country=st.sidebar.selectbox("Choose a country",["India","USA","China","Brazil","Canada","Italy","Singapore"])

if country:
    response=fn.generate_state_destinations(country)
    st.header(response['state_name'])
    places=response['places'].split(",")
    st.write("**Famous Places**")
    for item in places:
        st.write("-",item.strip())