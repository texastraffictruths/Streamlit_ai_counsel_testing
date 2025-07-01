from data_store import save_cases, load_cases
from ai_persona import get_persona_name

def show_dashboard():
    cases = load_cases()  # Load existing cases
    st.subheader("Your Cases")

    if len(cases) == 0:
        st.write("No cases yet. Please create a new case.")
    else:
        case_names = [case["name"] for case in cases]
        selected_case = st.selectbox("Select a case", case_names)

        if selected_case:
            case_index = case_names.index(selected_case)
            case_menu(cases, case_index)

    new_case_name = st.text_input("Enter new case name:")
    if st.button("Add New Case"):
        if new_case_name:
            new_case = {
                "name": new_case_name,
                "persona": None,
                "timeline": [],
                "evidence": [],
                "entities": [],
                "notes": [],
                "legal_sources": [],
                "post_filing_log": [],
                "drafts": []
            }
            cases.append(new_case)
            save_cases(cases)
            st.success(f"Case '{new_case_name}' added!")

def case_menu(cases, idx):
    case = cases[idx]
    st.subheader(f"--- {case['name']} ---")
    persona = get_persona_name(case)
    st.write(f"AI Persona: {persona}")

    st.write("Modules:")
    if st.button("Timeline"):
        from timeline import timeline_menu
        timeline_menu(case)
    if st.button("Evidence"):
        from evidence_locker import evidence_menu
        evidence_menu(case)
    if st.button("Entities"):
        from persons_entities import entities_menu
        entities_menu(case)
    if st.button("Notes"):
        from notes import notes_menu
        notes_menu(case)
    if st.button("Legal Sources"):
        from legal_sources import sources_menu
        sources_menu(case)
    if st.button("Post-Filing Log"):
        from post_filing_log import post_filing_menu
        post_filing_menu(case)
    if st.button("Drafts"):
        from drafting_suite import drafts_menu
        drafts_menu(case)
    if st.button("AI Persona"):
        from ai_persona import persona_menu
        persona_menu(case)
