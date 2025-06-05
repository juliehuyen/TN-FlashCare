import streamlit as st
from datetime import datetime

# === Page config ===
st.set_page_config(page_title="Patient Intake Form", layout="centered")

# === Custom CSS ===
st.markdown("""
<style>
.stTextInput input, .stDateInput input {
    background-color: #E1E6EB !important;
    color: black !important;
    border: 2px solid #ccc !important;
    border-radius: 8px !important;
    padding: 8px !important;
    transition: border 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.stTextInput input:focus, .stDateInput input:focus {
    border: 2px solid #4DAFEB !important;
    box-shadow: 0 0 0 3px rgba(77, 175, 235, 0.3);
    outline: none !important;
}

/* === ZONES DE TEXTE MULTILIGNES (text_area) === */
textarea, .stTextArea textarea {
    background-color: #E1E6EB !important;
    color: black !important;
    border: 2px solid #ccc !important;
    border-radius: 8px !important;
    padding: 8px !important;
    box-shadow: none !important;
    outline: none !important;
    transition: border 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

/* Effet focus ou hover avec halo bleu */
textarea:focus, .stTextArea textarea:focus,
textarea:hover, .stTextArea textarea:hover {
    border: 2px solid #4DAFEB !important;
    box-shadow: 0 0 0 3px rgba(77, 175, 235, 0.3) !important;
    outline: none !important;
}

.stMultiSelect [data-baseweb="tag"] {
    background-color: #4DAFEB; 
}
            
div[data-baseweb="select"] > div {
    background-color: #E1E6EB !important;
    color: black !important;
    border-radius: 6px !important;
    border: 2px solid #cccccc !important;
    transition: border 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}


/* File uploader - override entire container */
section[data-testid="stFileUploader"] {
    background-color: #E1E6EB !important;
    padding: 1rem;
    border-radius: 10px;
    color: black !important;
}

/* Customize file upload button */
section[data-testid="stFileUploader"] label {
    color: black !important;
}
            
/* ---- ON FOCUS or ACTIVE ---- */
div[data-baseweb="select"]:focus-within > div,
div[data-baseweb="select"]:hover > div {
    border: 2px solid #4DAFEB !important;
    box-shadow: 0 0 0 3px rgba(77, 175, 235, 0.3);
}

/* Buttons */
div.stButton > button {
    background-color: #4DAFEB;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
    border: none;
}

div.stButton > button:hover {
    background-color: #3ca4d3;
}
</style>
""", unsafe_allow_html=True)



# === Title & Introduction ===
st.title("🏥 Patient Intake Form")
st.markdown("""
Please fill out this form while you're on your way to the hospital.  
This will help the medical team prepare for your arrival and ensure faster, safer care.
""")

# === Personal Information ===
st.header("🧍 Personal Information")
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
birth_date = st.date_input("Date of Birth")
arrival_time = st.time_input("Estimated Arrival Time", value=datetime.now().time())

# === Medical History ===
st.header("🩺 Medical History")
medical_history = st.multiselect(
    "Select any known medical conditions:",
    [
        "Hypertension",
        "Diabetes",
        "Asthma",
        "Allergies",
        "Cardiac history",
        "Surgical history",
        "None"
    ]
)
other_conditions = st.text_area("Other relevant medical information")

# === Current Symptoms ===
st.header("🤒 Current Symptoms")
symptoms = st.text_area("What symptoms are you experiencing?")

# === Emergency Situation ===
st.header("🚨 Emergency Details")
emergency = st.text_area("Briefly describe what brings you to the emergency room")

# === File Upload ===
st.header("📎 Attachments")
uploaded_files = st.file_uploader(
    "Upload any relevant images (prescription, ID card, injury, etc.)", 
    type=["png", "jpg", "jpeg"], 
    accept_multiple_files=True
)

# === Submit Button ===
if st.button("📨 Submit Form"):
    if not first_name or not last_name:
        st.warning("Please enter your first and last name.")
    elif not symptoms or not emergency:
        st.warning("Please describe your symptoms and the emergency situation.")
    else:
        st.success("Form successfully submitted. Thank you for your cooperation!")

        # Recap
        st.markdown("### ✅ Summary")
        st.write(f"**First Name:** {first_name}")
        st.write(f"**Last Name:** {last_name}")
        st.write(f"**Date of Birth:** {birth_date}")
        st.write(f"**Estimated Arrival Time:** {arrival_time.strftime('%H:%M')}")
        st.write(f"**Medical History:** {', '.join(medical_history) if medical_history else 'None'}")
        st.write(f"**Other Info:** {other_conditions if other_conditions else 'Not specified'}")
        st.write(f"**Current Symptoms:** {symptoms}")
        st.write(f"**Emergency Details:** {emergency}")

        if uploaded_files:
            st.write("**📷 Uploaded Images:**")
            for img in uploaded_files:
                st.image(img, width=300)
        else:
            st.write("No images provided.")
