import streamlit as st


st.set_page_config(page_title="Fitness Tracker",)

pages = {
    "Páginas": [
        st.Page("Home.py", title="Home"),
        st.Page("Rutina.py", title="Rutina"),
        st.Page("Workout.py", title="Workout Logger"),
        st.Page("BMItracker.py", title="BMI Tracker"),
        st.Page("Progress.py", title="Progress Tracker"),
        st.Page("Distancia.py", title="Distancia"),
        st.Page("Chatbot.py", title="Chatbot"),
    ]
    
}

pg = st.navigation(pages)
pg.run()
