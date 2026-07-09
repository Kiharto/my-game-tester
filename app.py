import streamlit as st
import time
import random

# Mobile Page Layout Configuration
st.set_page_config(
    page_title="Rock Kingdom Bot Control", 
    page_icon="🤖", 
    layout="centered"
)

# Custom Chinese/English Localized Styling
st.markdown("""
    <style>
    .block-container { padding-top: 1.5rem; padding-bottom: 1rem; }
    .status-box { padding: 10px; border-radius: 5px; background-color: #f0f2f6; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("洛克王国 自动化控制台")
st.caption("Rock Kingdom Quest & Capture Automation Engine")

# --- Language Toggle ---
lang = st.radio("Language / 语言", ["简体中文", "English"], horizontal=True)

# --- Localization Dictionary ---
text = {
    "简体中文": {
        "status": "系统状态 (System Status)",
        "mode": "当前运行模式",
        "quest_mode": "自动新手教程任务 (Auto-Tutorial Quest)",
        "capture_mode": "手动捕捉模式 (Manual Capture Phase)",
        "bot_state": "脚本运行状态",
        "running": "🟢 正在运行 (Running)",
        "paused": "🟡 已自动暂停 - 等待捕捉 (Paused for Capture)",
        "trigger": "⚠️ 模拟发现稀有宠物 (Simulate Encounter)",
        "logs": "运行日志 (Live Engine Logs)",
        "success_msg": "检测到宠物出现！OpenCV 模板匹配成功。状态机已切断自动任务，移交控制权。",
    },
    "English": {
        "status": "System Status",
        "mode": "Current Core Mode",
        "quest_mode": "Auto-Tutorial Quest",
        "capture_mode": "Manual Capture Phase",
        "bot_state": "Engine State",
        "running": "🟢 Running",
        "paused": "🟡 Automatically Paused - Awaiting Capture",
        "trigger": "⚠️ Simulate Rare Pet Encounter",
        "logs": "Live Engine Logs",
        "success_msg": "Pet detected! OpenCV Template Matching Successful. State machine halted tutorial loop, handing over control.",
    }
}[lang]

# --- Section 1: State Machine Status ---
st.subheader(text["status"])

# Maintain state using Streamlit's memory structure
if "bot_paused" not in st.session_state:
    st.session_state.bot_paused = False

current_status = text["paused"] if st.session_state.bot_paused else text["running"]
current_mode = text["capture_mode"] if st.session_state.bot_paused else text["quest_mode"]

st.markdown(f"**{text['bot_state']}:** {current_status}")
st.markdown(f"**{text['mode']}:** `{current_mode}`")

st.markdown("---")

# --- Section 2: The Core Client Requirement Trigger ---
if not st.session_state.bot_paused:
    st.write("🤖 *Bot is currently simulating PyAutoGUI clicks to clear tutorial dialogs...*")
    if st.button(text["trigger"], use_container_width=True, type="primary"):
        st.session_state.bot_paused = True
        st.rerun()
else:
    st.warning(text["success_msg"])
    if st.button("🔄 重置任务循环 (Resume Tutorial Loop)", use_container_width=True):
        st.session_state.bot_paused = False
        st.rerun()

# --- Section 3: Live Process Logs ---
st.subheader(text["logs"])
if st.session_state.bot_paused:
    logs = [
        "[INFO] StateMachine initialized successfully.",
        "[LOG] Task: Clearing Tutorial Quest Stage 3...",
        "[MATCH] OpenCV match found: 'dialog_next_btn.png' (Confidence: 0.94)",
        "[ACTION] PyAutoGUI simulated click at coordinates (x:450, y:620)",
        "[⚠️ WARN] OpenCV MATCH: 'capture_screen_detector.png' EXCEEDED THRESHOLD (0.91)!",
        "[HALT] Safety trigger activated. Automation stopped. Handing control to client."
    ]
else:
    logs = [
        "[INFO] StateMachine initialized successfully.",
        "[LOG] Task: Clearing Tutorial Quest Stage 3...",
        "[MATCH] OpenCV match found: 'dialog_next_btn.png' (Confidence: 0.94)",
        "[ACTION] PyAutoGUI simulated click at coordinates (x:450, y:620)",
        "[LOG] Awaiting next frame stream processing..."
    ]

for log in logs:
    st.code(log, language="bash")
