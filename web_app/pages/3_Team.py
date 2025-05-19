import streamlit as st

# Page Title
st.title("🚀 Meet the Team")

# Team Members
team_members = [
    {"name": "Elodie Dai", "role": "CEO", "photo": "web_app/images/shark.png"},
    {"name": "Joëlle Huyen", "role": "CTO", "photo": "web_app/images/penguin.png"},
    {"name": "Julie Huyen", "role": "Lead Developer", "photo": "web_app/images/panda.png"},
    {"name": "Léonore Sarfati", "role": "Product Manager", "photo": "web_app/images/Wolfore.png"},
]

# Display team members
for member in team_members:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(member["photo"], width=100)
    with col2:
        st.subheader(member["name"])
        st.write(member["role"])
    st.divider()  # Adds a horizontal line for separation