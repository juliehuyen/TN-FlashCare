## This page is the home page of your front application


# Import Streamlit packages
import streamlit as st

# Page Title
st.title("Welcome to the Application Development Project")

# Introduction
st.markdown("""
Welcome to this application development course at Dauphine.
The goal of this project is to enable each group to develop their own application using a series of modern and powerful technologies.

## Technologies Used
For this project, you will work with the following technologies:

1. **Streamlit**: To create interactive and user-friendly web interfaces. Streamlit simplifies the process of building custom web applications with Python.

2. **Cohere**: A natural language processing (NLP) model that offers powerful capabilities for text analysis, text generation, and other NLP tasks.

3. **FastAPI**: A modern and fast web framework for building APIs with Python. It is ideal for creating performant and scalable backend services.

## Project Objectives
Each group is expected to create a functional application using the technologies mentioned above. The application should address a specific need and be accessible via a web interface.

## Project Structure
1. **Phase 1: Design** - Define the problem you want to solve with your application and design a solution using the mentioned technologies.

2. **Phase 2: Development** - Develop the application using Streamlit for the interface, Cohere for NLP processing and FastAPI for the backend.

3. **Phase 3: Deployment** - Deploy your application on a platform of your choice, ensuring it is accessible and functional.

## Resources and Support
We will provide tutorials and documentation to help you familiarize yourself with these technologies. Technical support will also be available to answer your questions throughout the project.

## Evaluation Criteria
Your application will be evaluated based on the following criteria
- Relevance and originality of the proposed solution.
- Effective or simulated integration of various technologies.
- The quality of the user interface.
- Robustness and design of the system architecture

Good luck to everyone, and may the best project win!



## Now, you can either delete this text (or save it in a new tab) and describe your problem instead

""")

st.markdown("""
    <style>
    /* Texte dans la barre latérale */
    .css-1d391kg {  /* Classe par défaut de la sidebar */
        color: white !important;  /* Texte blanc */
    }

    /* Texte dans le reste de l'application */
    .css-10trblm {  /* Classe par défaut pour le texte principal */
        color: #1a1a3d !important;  /* Texte de la couleur de secondaryBackgroundColor */
    }
    </style>
""", unsafe_allow_html=True)