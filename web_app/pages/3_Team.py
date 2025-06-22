import streamlit as st
from PIL import Image
import base64

# === Configuration de la page ===
st.set_page_config(page_title="Notre Équipe", layout="wide")

# === CSS personnalisé ===
st.markdown("""
    <style>
    /* Titre principal personnalisé */
    .custom-title {
        font-family: 'Helvetica Neue', sans-serif;
        color: #4DAFEB;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 30px;
    }

    /* Cartes membres de l’équipe */
    .team-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: #1a1a1a;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 20px;
    }

    /* Effet hover */
    .team-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
    }

    
    </style>
""", unsafe_allow_html=True)

# === Titre principal ===
st.markdown("""
    <h1 style='font-family: Helvetica, sans-serif; font-size: 40px;'>
        Hello, we are <span style='color: #4DAFEB'>Fantasmic</span> 
    </h1>
""", unsafe_allow_html=True)

st.markdown("""
Welcome to our team page.

At the heart of our mission is a commitment to transforming the hospital experience through smart, human-centered technology.  
We are a multidisciplinary team working together to develop innovative digital solutions that streamline patient intake, improve operational efficiency, and enhance quality of care from the moment a patient walks in.

By combining medical insight with advanced technology, we aim to create a faster, safer, and more compassionate healthcare journey.
""", unsafe_allow_html=True)

# === Membres de l'équipe ===
team_members = [
    {"name": "Elodie Dai", "role": "CEO", "photo": "web_app/images/shark.png", "bio": "Vision stratégique et direction générale du projet."},
    {"name": "Joëlle Huyen", "role": "CTO", "photo": "web_app/images/penguin.png", "bio": "Supervision de l’architecture technique"},
    {"name": "Julie Huyen", "role": "Lead Developer", "photo": "web_app/images/panda.png", "bio": "Responsable du développement logiciel et de la qualité du code."},
    {"name": "Léonore Sarfati", "role": "Product Manager", "photo": "web_app/images/Wolfore.png", "bio": "Pilote la roadmap produit et l’expérience utilisateur."},
]

# === Affichage des membres ===
cols = st.columns(4)

for col, member in zip(cols, team_members):
    with col:
        try:
            image = Image.open(member["photo"])
            buffered = base64.b64encode(image.tobytes()).decode()
            img_tag = f'<img src="data:image/png;base64,{base64.b64encode(open(member["photo"], "rb").read()).decode()}" width="50%" class="img">'
        except Exception:
            img_tag = f'<div style="color: red;">Image manquante</div>'

        st.markdown(f"""
        <div class="team-card">
            {img_tag}
            <h4>{member['name']}</h4>
            <p><strong>{member['role']}</strong></p>
            <p>{member['bio']}</p>
        </div>
        """, unsafe_allow_html=True)
