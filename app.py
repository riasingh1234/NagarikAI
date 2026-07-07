import streamlit as st
import google.generativeai as genai
import random
import string
import datetime

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="NagarikAI - Smart Bharat Civic Companion",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
<style>
    .main-header {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF9933, #FFFFFF, #138808);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 10px 0 0 0;
    }
    .sub-header {
        text-align: center;
        color: #6b7280;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        font-weight: 600;
    }
    div.stButton > button {
        border-radius: 10px;
        font-weight: 700;
        padding: 0.6rem 1.2rem;
        background: linear-gradient(90deg, #FF9933, #138808);
        color: white;
        border: none;
    }
    div.stButton > button:hover {
        opacity: 0.9;
        color: white;
    }
    .result-box {
        background-color: #f8f9fb;
        border-left: 5px solid #FF9933;
        border-radius: 8px;
        padding: 20px;
        margin-top: 15px;
    }
    .tracking-id {
        font-size: 1.3rem;
        font-weight: 800;
        color: #138808;
        background-color: #eafaf0;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        border: 2px dashed #138808;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
st.markdown('<div class="main-header">🇮🇳 NagarikAI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Smart Bharat – AI-Powered Civic Companion</div>', unsafe_allow_html=True)

# ---------------------- SIDEBAR ----------------------
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    language = st.selectbox(
        "🌐 Select Your Language",
        ["English", "Hindi", "Tamil", "Telugu", "Bengali", "Marathi"],
        index=0
    )
    st.markdown("---")
    st.markdown("### ℹ️ About NagarikAI")
    st.info(
        "NagarikAI is your AI-powered civic companion that helps you:\n\n"
        "- 💬 Get answers about government services\n"
        "- 📄 Simplify complex scheme documents\n"
        "- 🚨 File structured grievances instantly\n\n"
        "Built for **Smart Bharat Hackathon**."
    )
    st.markdown("---")
    st.caption("Powered by Google Gemini ⚡")

# ---------------------- GEMINI SETUP ----------------------
def get_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        st.error("⚠️ GEMINI_API_KEY not found in Streamlit secrets. Please add it to `.streamlit/secrets.toml`.")
        st.stop()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    return model

def call_gemini(prompt):
    try:
        model = get_model()
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error communicating with Gemini API: {str(e)}"

def generate_tracking_id():
    prefix = "NGR"
    date_part = datetime.datetime.now().strftime("%Y%m%d")
    rand_part = ''.join(random.choices(string.digits, k=5))
    return f"{prefix}-{date_part}-{rand_part}"

# ---------------------- TABS ----------------------
tab1, tab2, tab3 = st.tabs([
    "💬 AI Civic Companion",
    "📄 Scheme Simplifier",
    "🚨 Smart Grievance"
])

# ============================================================
# TAB 1: AI CIVIC COMPANION
# ============================================================
with tab1:
    st.markdown("### 💬 Ask Anything About Government Services")
    st.write("Get quick, reliable answers about schemes, documents, procedures, and civic services in India.")

    user_query = st.text_area(
        "Your Question",
        placeholder="e.g., How do I apply for a new ration card? What documents are needed for a passport renewal?",
        height=120,
        key="civic_query"
    )

    col1, col2 = st.columns([1, 5])
    with col1:
        ask_btn = st.button("🔍 Get Answer", key="ask_civic")

    if ask_btn:
        if not user_query.strip():
            st.warning("Please enter a question first.")
        else:
            with st.spinner("NagarikAI is thinking..."):
                prompt = f"""
You are NagarikAI, an expert AI Civic Companion for Indian citizens, deeply knowledgeable about Indian government services, schemes, procedures, documents, and civic processes at central, state, and municipal levels.

IMPORTANT INSTRUCTION: You must respond ENTIRELY in the {language} language. Do not use any other language in your response, including headings and labels. Every word of your response must be in {language}.

Citizen's Question: "{user_query}"

Provide a clear, accurate, well-structured, and helpful answer. Include:
- A direct answer to the question
- Relevant government department or authority (if applicable)
- Step-by-step process (if applicable)
- Required documents (if applicable)
- Any official portal or helpline reference (if commonly known)

Keep the tone friendly, respectful, and easy to understand for a common citizen. Use simple formatting with headings and bullet points where helpful.
"""
                answer = call_gemini(prompt)
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.markdown(answer)
                st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# TAB 2: SCHEME SIMPLIFIER
# ============================================================
with tab2:
    st.markdown("### 📄 Government Scheme Simplifier")
    st.write("Paste any complex government scheme text, notification, or circular, and get it broken down into simple, clear sections.")

    scheme_text = st.text_area(
        "Paste Government Scheme Text / Notification",
        placeholder="Paste the long, complex government scheme text here...",
        height=220,
        key="scheme_text"
    )

    col1, col2 = st.columns([1, 5])
    with col1:
        simplify_btn = st.button("✨ Simplify Now", key="simplify_scheme")

    if simplify_btn:
        if not scheme_text.strip():
            st.warning("Please paste the scheme text first.")
        else:
            with st.spinner("Simplifying the scheme document..."):
                prompt = f"""
You are NagarikAI, an expert at simplifying complex Indian government scheme documents, notifications, and circulars for common citizens.

IMPORTANT INSTRUCTION: You must respond ENTIRELY in the {language} language. Do not use any other language anywhere in your response, including section headings. Every word must be in {language}.

Below is a complex government scheme text. Break it down into the following clearly labeled sections (translate the section headings into {language} as well):

1. Scheme Name / Overview (a short 2-3 line summary of what this scheme is about)
2. Eligibility (who can apply, in simple bullet points)
3. Benefits (what the citizen gets, in simple bullet points)
4. How to Apply (step-by-step process in simple bullet points)
5. Documents Required (if mentioned or reasonably inferable)
6. Important Notes / Deadlines (if any)

Use simple, everyday language avoiding bureaucratic jargon. Use clear bullet points and headings. If some information is not present in the text, mention that it is not specified rather than guessing.

Government Scheme Text:
\"\"\"
{scheme_text}
\"\"\"
"""
                simplified = call_gemini(prompt)
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.markdown(simplified)
                st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# TAB 3: SMART GRIEVANCE
# ============================================================
with tab3:
    st.markdown("### 🚨 Smart Grievance Redressal")
    st.write("Describe your civic issue in your own words. NagarikAI will convert it into a formal complaint letter, assign the right department, and generate a tracking ID.")

    col_a, col_b = st.columns(2)
    with col_a:
        citizen_name = st.text_input("Your Name (optional)", placeholder="e.g., Ramesh Kumar", key="grievance_name")
    with col_b:
        citizen_area = st.text_input("Area / Locality", placeholder="e.g., Sector 15, Faridabad", key="grievance_area")

    complaint_text = st.text_area(
        "Describe Your Complaint",
        placeholder="e.g., there is a huge pothole near my street since 2 months and yesterday a bike rider fell because of it, nobody is fixing it",
        height=150,
        key="complaint_text"
    )

    col1, col2 = st.columns([1, 5])
    with col1:
        submit_btn = st.button("📝 Generate Grievance", key="submit_grievance")

    if submit_btn:
        if not complaint_text.strip():
            st.warning("Please describe your complaint first.")
        else:
            with st.spinner("Drafting your formal grievance..."):
                name_line = citizen_name.strip() if citizen_name.strip() else "Concerned Citizen"
                area_line = citizen_area.strip() if citizen_area.strip() else "Not specified"

                prompt = f"""
You are NagarikAI, an expert AI assistant that converts raw, casual citizen complaints about public infrastructure into formal, professional municipal/legal grievance letters for Indian government authorities.

IMPORTANT INSTRUCTION: You must respond ENTIRELY in the {language} language. Every word of your response, including all headings and labels, must be in {language}.

Citizen Details:
- Name: {name_line}
- Area/Locality: {area_line}

Raw Complaint (in citizen's own words):
\"\"\"
{complaint_text}
\"\"\"

Your task has two parts:

PART 1: Identify the most relevant municipal/government department for this issue from categories such as: Roads & Infrastructure (PWD), Water Supply, Electricity, Sanitation & Waste Management, Public Health, Parks & Environment, Traffic & Transport, Drainage & Sewage, or Other. State the department name clearly on its own line, prefixed exactly with "DEPARTMENT:" (translate the label "DEPARTMENT:" itself into {language} but keep it as a clear prefix on its own line).

PART 2: Write a formal, professional, well-structured grievance/complaint letter addressed to the appropriate municipal authority (e.g., Municipal Commissioner / concerned department). The letter must include:
- A formal salutation
- Subject line clearly stating the issue
- A professional, factual, non-emotional description of the problem (rewritten from the casual complaint, removing slang, adding severity and public safety context where relevant)
- A clear, respectful request for prompt action/resolution
- A formal closing with the citizen's name and locality

Format your entire response as:
DEPARTMENT: [department name in {language}]

[Full formal letter in {language}]
"""
                grievance_output = call_gemini(prompt)
                tracking_id = generate_tracking_id()

                department_name = "General Civic Department"
                letter_body = grievance_output
                if "DEPARTMENT:" in grievance_output:
                    parts = grievance_output.split("DEPARTMENT:", 1)[1]
                    lines = parts.strip().split("\n", 1)
                    department_name = lines[0].strip()
                    letter_body = lines[1].strip() if len(lines) > 1 else grievance_output
                elif ":" in grievance_output.split("\n")[0]:
                    first_line = grievance_output.split("\n")[0]
                    department_name = first_line.split(":", 1)[-1].strip()
                    letter_body = "\n".join(grievance_output.split("\n")[1:]).strip()

                st.success("✅ Grievance drafted successfully!")

                colx, coly = st.columns(2)
                with colx:
                    st.markdown("**🏢 Assigned Department**")
                    st.markdown(f"### {department_name}")
                with coly:
                    st.markdown("**🔖 Tracking ID**")
                    st.markdown(f'<div class="tracking-id">{tracking_id}</div>', unsafe_allow_html=True)

                st.markdown("---")
                st.markdown("### 📜 Formal Grievance Letter")
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.markdown(letter_body)
                st.markdown('</div>', unsafe_allow_html=True)

                st.download_button(
                    label="⬇️ Download Grievance Letter",
                    data=letter_body,
                    file_name=f"grievance_{tracking_id}.txt",
                    mime="text/plain"
                )

# ---------------------- FOOTER ----------------------
st.markdown("---")
st.caption("🇮🇳 NagarikAI | Smart Bharat Hackathon Submission | Powered by Google Gemini")
