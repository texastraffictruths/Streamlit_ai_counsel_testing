def timeline_menu(case):
    import streamlit as st

    st.subheader(f"Timeline for {case['name']}:")
    for idx, event in enumerate(case["timeline"], 1):
        st.write(f"{idx}. {event['date']} - {event['event']}")
    
    event_text = st.text_input("Event description:")
    event_date = st.text_input("Date (optional):")
    
    if st.button("Add Event"):
        case["timeline"].append({"event": event_text, "date": event_date or "No date"})
        st.success(f"Event added: {event_text}")
