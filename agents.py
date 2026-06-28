import os
import google.generativeai as genai
from dotenv import load_dotenv

# -----------------------------
# Load API Key
# -----------------------------

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


# -----------------------------
# Helper Function
# -----------------------------

def generate_response(prompt):

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"""
# ❌ Error

{str(e)}

Possible reasons:

• API quota exceeded
• Invalid API key
• Internet connection issue
• Gemini service temporarily unavailable
"""


# -----------------------------
# Opportunity Scout Agent
# -----------------------------

def opportunity_scout(profile):

    prompt = f"""
You are an expert Career Opportunity Scout AI.

Student Profile:

{profile}

Generate a professional report with these sections:

# Opportunity Scout Report

1. Student Summary

2. Best Internship Opportunities

3. Best Hackathons

4. Scholarships

5. Campus Ambassador Programs

6. Open Source Programs

7. Certifications

8. Companies to Target

9. AI Recommendation

Format everything beautifully using Markdown.
"""

    return generate_response(prompt)


# -----------------------------
# Eligibility Agent
# -----------------------------

def eligibility_agent(profile):

    prompt = f"""
You are an Eligibility Analysis AI.

Student Profile:

{profile}

Create a detailed report.

Include:

# Eligibility Report

1. Profile Analysis

2. Overall Career Score out of 100

3. Strong Skills

4. Weak Skills

5. Eligible Opportunities

6. Missing Skills

7. Hiring Readiness

8. Resume Score

9. LinkedIn Score

10. GitHub Score

11. AI Suggestions

Return only Markdown.
"""

    return generate_response(prompt)


# -----------------------------
# Roadmap Agent
# -----------------------------

def roadmap_agent(profile):

    prompt = f"""
You are a Career Roadmap AI.

Student Profile:

{profile}

Create a detailed 3-month roadmap.

Include:

# Month 1

Skills

Projects

Resources

Goals

# Month 2

Skills

Projects

Resources

Goals

# Month 3

Skills

Projects

Resources

Goals

End with:

Final Career Goal

Internship Preparation Checklist

Daily Study Routine

Weekly Targets

Return everything in beautiful Markdown.
"""

    return generate_response(prompt)