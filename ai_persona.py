PERSONAS = [
    {
        "name": "Strategist",
        "description": "Clear, concise, and objective. A no-nonsense professional focused on the facts and the most direct path to building your case."
    },
    {
        "name": "Guide",
        "description": "Patient, empathetic, and supportive. Acts as a calm mentor, reduces stress, and guides you step by step."
    },
    {
        "name": "Razor",
        "description": "Witty, blunt, and fiercely strategic with a touch of dark humor. Keeps you motivated by treating the law like a competitive sport."
    },
    {
        "name": "Ally",
        "description": "Relatable, modern, and direct. Communicates like a tech-savvy peer, using plain English and modern expressions."
    }
]

def persona_menu(case):
    import streamlit as st

    st.subheader("AI Persona Selection:")
    for idx, persona in enumerate(PERSONAS, 1):
        st.write(f"{idx}. {persona['name']}: {persona['description']}")
        
    choice = st.selectbox("Choose a persona", [persona["name"] for persona in PERSONAS] + ["Not Set"])
    
    if choice != "Not Set":
        case["persona"] = [idx for idx, persona in enumerate(PERSONAS) if persona["name"] == choice][0]
        st.success(f"Persona set to {choice} for this case.")
    else:
        case["persona"] = None

def get_persona_name(case):
    """Safely get the AI persona name for a case."""
    if "persona" in case and case["persona"] is not None:
        idx = case["persona"]
        if 0 <= idx < len(PERSONAS):
            return PERSONAS[idx]["name"]
    return "Not set"
