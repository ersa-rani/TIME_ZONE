import streamlit as st
from datetime import datetime, date, time
from zoneinfo import ZoneInfo
import time as tm

# Time Zones List
TIME_ZONES = [
    "UTC", "Asia/Karachi", "America/New_York", "Europe/London", "Asia/Tokyo",
    "Australia/Sydney", "America/Los_Angeles", "Europe/Berlin", "Asia/Dubai", "Asia/Kolkata"
]

# Streamlit Page Configuration
st.set_page_config(page_title="Time Zone App", page_icon="⏰", layout="centered")

st.title("🌍 Time Zone Converter")
st.markdown("---")

# Live Time Display
st.sidebar.header("🕒 Live Time in Selected Timezones")
selected_timezones = st.sidebar.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

for tz in selected_timezones:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.sidebar.write(f"**{tz}**: {current_time}")

# Time Conversion Section
st.header("🔄 Convert Time Between Timezones")

col1, col2 = st.columns(2)
with col1:
    from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
with col2:
    to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

current_time = st.time_input("⏱ Enter Time to Convert", value=datetime.now().time())

if st.button("Convert Time"):
    dt = datetime.combine(date.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    
    st.success(f"✅ Converted Time in {to_tz}: {converted_time}")

st.markdown("---")
st.info("🌟 This app helps you quickly convert time between different timezones.")
