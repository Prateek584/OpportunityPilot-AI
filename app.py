import streamlit as st
from agents import (
    opportunity_scout,
    eligibility_agent,
    roadmap_agent,
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="OpportunityPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD CSS ---------------- #

try:
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )
except:
    pass

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("🚀 OpportunityPilot AI")

    st.caption("Version 2.0")

    st.divider()

    st.markdown("### 🤖 AI Agents")

    st.success("Opportunity Scout")

    st.success("Eligibility Analyzer")

    st.success("Career Roadmap")

    st.divider()

    st.markdown("### 🛠 Tech Stack")

    st.write("• Python")

    st.write("• Streamlit")

    st.write("• Gemini AI")

    st.write("• AI Agents")

    st.divider()

    st.info(
        "Helping students discover opportunities using AI."
    )

# ---------------- HERO ---------------- #

st.markdown(
"""
# 🚀 OpportunityPilot AI

### AI-Powered Career Intelligence Platform

Discover internships, hackathons, scholarships and build a career roadmap using AI.

""")

st.divider()

# ---------------- METRICS ---------------- #

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        "AI Agents",
        "3"
    )

with m2:
    st.metric(
        "Reports",
        "Unlimited"
    )

with m3:
    st.metric(
        "Response",
        "<5 sec"
    )

with m4:
    st.metric(
        "Career Ready",
        "100%"
    )

st.divider()

# ---------------- PROFILE ---------------- #

st.subheader("👤 Student Profile")

profile = st.text_area(
    "",
    height=220,
    placeholder="""
Name: Prateek Gautam

Degree: B.Tech CSE (AI & ML)

Year: 2nd Year

Skills:
Python
Java
HTML
CSS
JavaScript
GitHub

Interests:
Artificial Intelligence
Machine Learning
Web Development
Open Source

Career Goal:
Software Development Internship
"""
)

# ---------------- FEATURE CARDS ---------------- #

c1, c2, c3 = st.columns(3)

with c1:
    st.info(
        """
### 🔍 Opportunity Scout

Find

• Internships

• Hackathons

• Scholarships

• Campus Ambassador Programs
"""
    )

with c2:
    st.success(
        """
### ✅ Eligibility Analyzer

Check

• Eligibility

• Missing Skills

• Readiness

• Recommendations
"""
    )

with c3:
    st.warning(
        """
### 📈 Career Roadmap

Generate

• 3 Month Plan

• Learning Path

• Project Ideas

• Career Goals
"""
    )

st.divider()

# ---------------- BUTTONS ---------------- #

col1, col2, col3 = st.columns(3)

with col1:

    opportunity = st.button(
        "🔍 Opportunity Scout",
        use_container_width=True
    )

with col2:

    eligibility = st.button(
        "✅ Eligibility Check",
        use_container_width=True
    )

with col3:

    roadmap = st.button(
        "📈 Career Roadmap",
        use_container_width=True
    )

st.divider()

# ---------------- RESULTS ---------------- #

if not profile.strip():

    st.warning("Please enter your profile first.")

else:

    if opportunity:

        with st.spinner(
            "Searching opportunities..."
        ):

            report = opportunity_scout(profile)

        st.success("Opportunity Report Generated")

        st.markdown(report)

    if eligibility:

        with st.spinner(
            "Analyzing profile..."
        ):

            report = eligibility_agent(profile)

        st.success("Eligibility Report Generated")

        st.markdown(report)

    if roadmap:

        with st.spinner(
            "Building roadmap..."
        ):

            report = roadmap_agent(profile)

        st.success("Roadmap Generated")

        st.markdown(report)

# ---------------- DOWNLOAD ---------------- #

st.divider()

st.download_button(

    label="📥 Download Sample Report",

    data="""
OpportunityPilot AI Report

Generated Successfully.
""",

    file_name="Opportunity_Report.txt",

    mime="text/plain",
)

# ---------------- FOOTER ---------------- #

st.divider()

st.markdown(
"""
## 👨‍💻 About

**OpportunityPilot AI** helps students discover opportunities,
evaluate eligibility and create AI-powered career roadmaps.

---

### Built By

**Prateek Gautam**

B.Tech CSE (AI & ML)

Powered by **Python • Streamlit • Gemini AI**
"""
)