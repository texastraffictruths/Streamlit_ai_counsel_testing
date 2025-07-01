def entities_menu(case):
    import streamlit as st

    st.subheader(f"Entities for {case['name']}:")
    for idx, ent in enumerate(case["entities"], 1):
        st.write(f"{idx}. {ent['name']} ({ent['role']})")
    
    name = st.text_input("Entity Name:")
    role = st.text_input("Role:")
    
    if st.button("Add Entity"):
        case["entities"].append({"name": name, "role": role})
        st.success("Entity added.")
