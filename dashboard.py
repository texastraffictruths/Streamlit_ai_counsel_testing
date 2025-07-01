from data_store import save_cases, load_cases
from ai_persona import get_persona_name

def show_dashboard():
    cases = load_cases()  # Ensure this function is correctly defined in data_store.py
    st.subheader("Your Cases")

    if len(cases) == 0:
        st.write("No cases yet. Please create a new case.")
    else:
        case_names = [case["name"] for case in cases]
        selected_case = st.selectbox("Select a case", case_names)

        if selected_case:
            case_index = case_names.index(selected_case)
            case_menu(cases, case_index)  # Ensure case_menu is correctly defined

    new_case_name = st.text_input("Enter new case name:")
    if st.button("Add New Case"):
        if new_case_name:
            new_case = {
                "name": new_case_name,
                "persona": None,  # No persona yet!
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
