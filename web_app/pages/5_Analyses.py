import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Medical Test Tracker", layout="centered")
st.title("🧪 Medical Test Tracker")
st.markdown("""
Welcome to your personal test dashboard.  
Here you can follow the progress of your medical tests, see appointments, and access results.
""")
tests = [
    {
        "name": "Blood Test",
        "status": "To do",
        "result_link": None,
        "appointment": {"time": "10:00 AM", "floor": "1st", "room": "B102"},
        "pdf": None,
        "details": "This is some extra info about the Blood Test."
    },
    {
        "name": "X-Ray - Chest",
        "status": "Waiting Results",
        "result_link": None,
        "appointment": {"time": "2:00 PM", "floor": "2nd", "room": "Radiology 204"},
        "pdf": None,
        "details": "X-Ray details and instructions."
    },
    {
        "name": "COVID-19 PCR",
        "status": "Results Ready",
        "result_link": "https://example.com/results/covid",
        "appointment": None,
        "pdf": "https://example.com/files/covid_results.pdf",
        "details": "COVID-19 PCR test was performed on 2025-06-01."
    },
]

# Construire le HTML avec CSS et JS inclus
cards_html = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro&display=swap');

html, body {
    font-family: 'Source Sans Pro', sans-serif !important;
    margin: 0;
    padding: 0;
}
.test-card {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px 20px;
    margin-bottom: 15px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    transition: border 0.2s ease, box-shadow 0.2s ease;
    position: relative;
    cursor: pointer;
    user-select: none;
    font-family: 'Source Sans Pro', sans-serif !important;
    max-width: 600px;
}
.test-card:hover {
    border: 1px solid #4DAFEB;
    box-shadow: 0 0 10px rgba(77, 175, 235, 0.3);
}
.status-pill {
    padding: 4px 12px;
    border-radius: 20px;
    color: white;
    font-size: 13px;
    position: absolute;
    top: 20px;
    right: 50px;
    user-select: none;
}
.status-todo { background-color: #ccc; }
.status-waiting { background-color: #f0ad4e; }
.status-done { background-color: #5cb85c; }
.sub-info {
    font-size: 13px;
    color: #666;
    margin-top: 4px;
}
.download-link {
    font-size: 13px;
    margin-top: 8px;
    display: inline-block;
    background-color: #4DAFEB;
    color: white !important;
    padding: 6px 12px;
    border-radius: 6px;
    text-decoration: none !important;
}
.download-link:hover {
    background-color: #3c9bd6;
    text-decoration: none;
}
.details {
    margin-top: 12px;
    font-size: 14px;
    color: #333;
    display: none;
}
.toggle-icon {
    position: absolute;
    top: 20px;
    right: 20px;
    font-size: 18px;
    user-select: none;
}
</style>

<script>
function toggleDetails(id, iconId) {
    const detailsEl = document.getElementById(id);
    const iconEl = document.getElementById(iconId);
    if (detailsEl.style.display === "block") {
        detailsEl.style.display = "none";
        iconEl.textContent = "▶";
    } else {
        detailsEl.style.display = "block";
        iconEl.textContent = "▼";
    }
}
</script>
"""

for i, test in enumerate(tests):
    name = test["name"]
    status = test["status"]
    appointment = test.get("appointment")
    pdf = test.get("pdf")
    details = test.get("details", "")

    if status == "To do":
        status_class = "status-todo"
        status_text = "To do"
    elif status == "Waiting Results":
        status_class = "status-waiting"
        status_text = "Waiting"
    elif status == "Results Ready":
        status_class = "status-done"
        status_text = "Done"
    else:
        status_class = ""
        status_text = ""

    if appointment:
        appointment_info = f"{appointment['time']} — Floor: {appointment['floor']}, Room: {appointment['room']}"
    elif status != "Results Ready":
        appointment_info = "Waiting for scheduling..."
    else:
        appointment_info = ""

    pdf_link_html = f'<a href="{pdf}" target="_blank" class="download-link">Download PDF</a>' if pdf else ""

    cards_html += f"""
    <div class="test-card" onclick="toggleDetails('details-{i}', 'icon-{i}')">
        <span id="icon-{i}" class="toggle-icon">▶</span>
        <strong>{name}</strong>
        <span class="status-pill {status_class}">{status_text}</span>
        <div class="sub-info">{appointment_info}</div>
        {pdf_link_html}
        <div id="details-{i}" class="details">{details}</div>
    </div>
    """

html(cards_html, height=600, scrolling=True)
