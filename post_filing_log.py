def post_filing_menu(case):
    import streamlit as st

    st.subheader(f"Incident Log for {case['name']}:")
    for idx, inc in enumerate(case["post_filing_log"], 1):
        st.write(f"{idx}. {inc['date'] or 'No date'} - {inc['desc']}")
    
    desc = st.text_input("Incident Description:")
    date = st.text_input("Date (optional):")
    
    if st.button("Add Incident"):
        case["post_filing_log"].append({"desc": desc, "date": date})
        st.success("Incident added.")
