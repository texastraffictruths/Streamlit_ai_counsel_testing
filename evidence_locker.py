def evidence_menu(case):
    import streamlit as st

    st.subheader(f"Evidence for {case['name']}:")
    for idx, item in enumerate(case["evidence"], 1):
        st.write(f"{idx}. {item['file']} - {item['description']}")
    
    fname = st.text_input("File name:")
    desc = st.text_input("Description:")
    
    if st.button("Add Evidence"):
        case["evidence"].append({"file": fname, "description": desc})
        st.success("Evidence added.")
