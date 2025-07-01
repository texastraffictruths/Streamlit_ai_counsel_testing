def sources_menu(case):
    import streamlit as st

    st.subheader(f"Legal Sources for {case['name']}:")
    for idx, src in enumerate(case["legal_sources"], 1):
        st.write(f"{idx}. {src['name']}")
        if src["link"]:
            st.write(f"   Link: {src['link']}")
        if src["summary"]:
            st.write(f"   Summary: {src['summary']}")
    
    name = st.text_input("Source Name:")
    link = st.text_input("Link (optional):")
    summary = st.text_input("Summary (optional):")
    
    if st.button("Add Source"):
        case["legal_sources"].append({"name": name, "link": link, "summary": summary})
        st.success("Source added.")
