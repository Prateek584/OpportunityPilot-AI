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

hero1, hero2 = st.columns([3,2])

with hero1:

    st.markdown("""
# 🚀 OpportunityPilot AI

## Your AI-Powered Career Intelligence Platform

Discover internships, hackathons, scholarships,
AI recommendations and personalized career roadmaps.

⭐⭐⭐⭐⭐ Trusted by students
""")

    st.button("🚀 Start Career Journey")

with hero2:

    st.image(
        "assets/hero_dashboard.png",
        use_container_width=True
    )

st.divider()

# ---------------- METRICS ---------------- #

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("🤖 AI Agents","3")

with m2:
    st.metric("📄 Reports","Unlimited")

with m3:
    st.metric("⚡ Response","<5 sec")

with m4:
    st.metric("🎯 AI Powered","100%")

st.divider()

# ---------------- PROFILE ---------------- #

st.subheader("👤 Tell AI About Yourself")

st.caption(
"Provide as much information as possible for more accurate recommendations."
)

st.subheader("👤 Student Profile")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Full Name")
    degree = st.selectbox(
        "Degree",
        [
            "B.Tech CSE",
            "B.Tech CSE (AI & ML)",
            "BCA",
            "MCA"
        ]
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.5
    )

with col2:
    year = st.selectbox(
        "Current Year",
        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year"
        ]
    )

    goal = st.selectbox(
        "Career Goal",
        [
            "Software Engineer",
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Web Developer"
        ]
    )

skills = st.text_area(
    "Skills",
    placeholder="Python, Java, HTML, CSS, JavaScript, SQL..."
)

interests = st.text_input(
    "Interests",
    placeholder="Artificial Intelligence, Web Development, Data Science..."
)

resume = st.file_uploader(
    "Upload Resume (Optional)",
    type=["pdf", "docx"]
)

profile = f"""
Name: {name}
Degree: {degree}
CGPA: {cgpa}
Year: {year}
Skills:
{skills}

Interests:
{interests}

Career Goal:
{goal}

Resume Uploaded:
{"Yes" if resume else "No"}
"""


# ---------------- FEATURE CARDS ---------------- #

c1, c2, c3 = st.columns(3)

with c1:
    st.info(
        """
### 🚀 Find Opportunities

✔ Internships

✔ Hackathons

✔ Scholarships

✔ Open Source

✔ Campus Ambassador Programs
"""
    )

with c2:
    st.success(
        """
### 🧠 AI Eligibility

✔ Profile Analysis

✔ Skill Gap

✔ Career Score

✔ Improvement Tips
"""
    )

with c3:
    st.warning(
        """
### 🗺 AI Career Roadmap

✔ 3-Month Learning Plan

✔ Weekly Goals

✔ Recommended Projects

✔ Career Milestones
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