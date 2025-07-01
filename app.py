import streamlit as st
from data_store import load_cases
from dashboard import show_dashboard

def main():
    st.title("AI Counsel: Pro Se Litigant's Assistant")
    show_dashboard()  # This function should be defined in dashboard.py

if __name__ == "__main__":
    main()
