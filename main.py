import streamlit as st

from app.agents.report_agent import generate_visit_report
from app.agents.compliance_agent import generate_incident_report, generate_medication_log
from app.agents.scheduling_agent import suggest_schedule_adjustment
from app.agents.summary_agent import generate_family_summary
from app.database.firestore import save_record, get_all_records

st.set_page_config(page_title="CareFlow AI", page_icon="🩺", layout="wide")


def main():
    st.title("CareFlow AI 🩺")
    st.subheader("AI‑Powered Compliance & Workflow Automation for Home‑Care Agencies")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Visit Report", "Compliance Docs", "Scheduling", "Family Summary", "Records"]
    )

    with tab1:
        st.header("AI Visit Report Generator")
        caregiver_name = st.text_input("Caregiver Name")
        client_name = st.text_input("Client Name")
        raw_notes = st.text_area(
            "Caregiver Notes (voice‑to‑text or typed)",
            placeholder="e.g. Visited Mrs. Kelly. She ate half her lunch, took medication, slight swelling on left foot, mood low.",
            height=150,
        )

        if st.button("Generate Visit Report", type="primary"):
            if not (caregiver_name and client_name and raw_notes.strip()):
                st.warning("Please fill in caregiver, client, and notes.")
            else:
                report = generate_visit_report(
                    caregiver_name=caregiver_name,
                    client_name=client_name,
                    notes=raw_notes,
                )
                st.success("Visit report generated.")
                st.json(report)
                save_record("visit_report", report)

    with tab2:
        st.header("Compliance Documentation")

        st.markdown("### Incident Report")
        incident_notes = st.text_area(
            "Incident Description",
            placeholder="Describe any incident, fall, medication error, or risk event.",
            height=120,
            key="incident_notes",
        )
        if st.button("Generate Incident Report"):
            if not incident_notes.strip():
                st.warning("Please describe the incident.")
            else:
                incident = generate_incident_report(incident_notes)
                st.success("Incident report generated.")
                st.json(incident)
                save_record("incident_report", incident)

        st.markdown("---")
        st.markdown("### Medication Log")
        med_notes = st.text_area(
            "Medication Notes",
            placeholder="e.g. Morning meds taken, missed lunchtime dose, evening dose delayed.",
            height=120,
            key="med_notes",
        )
        if st.button("Generate Medication Log"):
            if not med_notes.strip():
                st.warning("Please enter medication notes.")
            else:
                med_log = generate_medication_log(med_notes)
                st.success("Medication log generated.")
                st.json(med_log)
                save_record("medication_log", med_log)

    with tab3:
        st.header("Smart Scheduling Agent")
        current_schedule = st.text_area(
            "Current Schedule Snapshot",
            placeholder="e.g. Mary: Mon–Wed mornings, John: Tue–Thu evenings, conflict on Wednesday.",
            height=120,
        )
        constraints = st.text_area(
            "Constraints / Notes",
            placeholder="e.g. Mrs. Kelly must be seen daily before 11am. John cannot work Wednesdays.",
            height=120,
        )

        if st.button("Suggest Schedule Adjustment"):
            if not current_schedule.strip():
                st.warning("Please describe the current schedule.")
            else:
                suggestion = suggest_schedule_adjustment(
                    current_schedule=current_schedule,
                    constraints=constraints,
                )
                st.success("Schedule suggestion generated.")
                st.json(suggestion)
                save_record("schedule_suggestion", suggestion)

    with tab4:
        st.header("Family Communication Summary")
        week_notes = st.text_area(
            "Weekly Care Notes",
            placeholder="Summarise key events, mood, health changes, and medication adherence for the week.",
            height=150,
        )
        family_name = st.text_input("Family Contact Name (optional)")

        if st.button("Generate Family Summary"):
            if not week_notes.strip():
                st.warning("Please enter weekly notes.")
            else:
                summary = generate_family_summary(
                    notes=week_notes,
                    family_name=family_name or "Family",
                )
                st.success("Family summary generated.")
                st.write(summary)
                save_record("family_summary", {"summary": summary})

    with tab5:
        st.header("Stored Records (Session‑Level Demo)")
        records = get_all_records()
        if not records:
            st.info("No records stored yet in this session.")
        else:
            st.json(records)


if __name__ == "__main__":
    main()
