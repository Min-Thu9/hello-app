import streamlit as st
import datetime
import pandas as pd

st.set_page_config(page_title="Tutor Bot Settings", page_icon="🛠️", layout="centered")

st.title("🛠️ Tutor Bot Settings Page")

st.header("👤 User Information")
name = st.text_input("Your Name", value="Student")
age = st.number_input("Age", min_value=5, max_value=100, value=18)

st.header("🎯 Learning Preferences")
learning_style = st.radio("Preferred Learning Style", ["Visual", "Auditory", "Reading/Writing", "Kinesthetic"])
subjects = st.multiselect("Subjects of Interest", ["Math", "Science", "History", "English", "Programming", "Art"])

st.header("⏰ Schedule Preferences")
preferred_days = st.multiselect("Available Days", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
preferred_time = st.time_input("Preferred Time for Tutoring")

st.header("🌐 Communication")
contact_method = st.selectbox("Preferred Contact Method", ["Email", "WhatsApp", "Telegram", "In-App Chat"])
email = st.text_input("Email Address (if applicable)")

st.header("🧠 Goals")
goal = st.text_area("Your learning goal", "I want to improve my understanding of Python.")

st.header("🔒 Privacy Settings")
save_data = st.checkbox("Allow tutor bot to save your preferences", value=True)

if st.button("Save Settings"):
    st.success("✅ Your settings have been saved!")
    st.write("**Summary:**")
    data = {
        "name": name,
        "age": age,
        "learning_style": learning_style,
        "subjects": subjects,
        "available_days": preferred_days,
        "preferred_time": str(preferred_time),
        "contact_method": contact_method,
        "email": email,
        "goal": goal,
        "save_data": save_data
    }
    st.json(data)

    # Convert dict to DataFrame with one row
    df = pd.DataFrame([data])

    # Convert to CSV bytes
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="settings.csv",
        mime="text/csv",
        icon=":material/download:",
    )
