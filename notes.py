def notes_menu(case):
    import streamlit as st

    st.subheader(f"Notes for {case['name']}:")
    for idx, note in enumerate(case.get("notes", []), 1):
        st.write(f"{idx}. {note}")
    
    note = st.text_input("Enter your note:")
    
    if st.button("Add Note"):
        case["notes"].append(note)
        st.success("Note added.")
