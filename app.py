import streamlit as st
from data_store import load_cases, save_cases
from dashboard import show_dashboard

def main():
    st.title("AI Counsel: Pro Se Litigant's Assistant")
    show_dashboard()

if __name__ == "__main__":
    main()
