def drafts_menu(case):
    import streamlit as st

    st.subheader(f"Drafts for {case['name']}:")
    for idx, draft in enumerate(case["drafts"], 1):
        st.write(f"{idx}. {draft['title']}")
        st.write(f"   {draft['body'][:50]}...")  # Show first 50 chars
    
    title = st.text_input("Draft Title:")
    body = st.text_area("Draft Content:")
    
    if st.button("Add Draft"):
        case["drafts"].append({"title": title, "body": body})
        st.success("Draft added.")
