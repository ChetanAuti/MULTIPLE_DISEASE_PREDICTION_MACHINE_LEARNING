from pathlib import Path
import pickle

import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Multiple Disease Prediction System",
    page_icon="MD",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent


@st.cache_resource
def load_models():
    model_dir = BASE_DIR / "savedModels"
    with open(model_dir / "diabetes.sav", "rb") as file:
        diabetes_model = pickle.load(file)
    with open(model_dir / "heart.sav", "rb") as file:
        heart_model = pickle.load(file)
    with open(model_dir / "parkinsons.sav", "rb") as file:
        parkinsons_model = pickle.load(file)
    return diabetes_model, heart_model, parkinsons_model


diabetes_model, heart_model, parkinsons_model = load_models()


st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(14, 116, 144, 0.18), transparent 28%),
            radial-gradient(circle at top right, rgba(59, 130, 246, 0.14), transparent 26%),
            linear-gradient(180deg, #f8fbff 0%, #eef4fb 55%, #e9f0f8 100%);
    }
    .block-container {
        padding-top: 1.4rem;
        padding-bottom: 2.2rem;
    }
    .hero-card, .panel-card, .result-card, .sidebar-card {
        background: rgba(255, 255, 255, 0.82);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(15, 23, 42, 0.08);
        border-radius: 24px;
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
    }
    .hero-card {
        padding: 1.5rem 1.6rem;
        margin-bottom: 1.2rem;
    }
    .hero-kicker {
        text-transform: uppercase;
        letter-spacing: 0.18em;
        font-size: 0.74rem;
        color: #0f766e;
        font-weight: 700;
        margin-bottom: 0.45rem;
    }
    .hero-title {
        font-size: 2.35rem;
        line-height: 1.05;
        margin: 0;
        color: #0f172a;
    }
    .hero-copy {
        margin-top: 0.6rem;
        color: #334155;
        font-size: 1rem;
        max-width: 68ch;
    }
    .pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-top: 1rem;
    }
    .pill {
        display: inline-block;
        padding: 0.45rem 0.75rem;
        border-radius: 999px;
        background: rgba(15, 118, 110, 0.08);
        color: #115e59;
        font-size: 0.82rem;
        font-weight: 600;
    }
    .metric-card {
        padding: 1rem 1.1rem;
    }
    .metric-label {
        color: #475569;
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.35rem;
    }
    .metric-value {
        color: #0f172a;
        font-size: 1.35rem;
        font-weight: 800;
        margin: 0;
    }
    .metric-sub {
        color: #64748b;
        font-size: 0.85rem;
        margin-top: 0.2rem;
    }
    .panel-card {
        padding: 1.2rem 1.2rem 1.35rem;
        margin-bottom: 1rem;
    }
    .panel-title {
        margin: 0 0 0.35rem;
        color: #0f172a;
        font-size: 1.4rem;
    }
    .panel-copy {
        margin: 0;
        color: #475569;
    }
    .result-card {
        padding: 1rem 1.1rem;
        margin-top: 1rem;
    }
    .result-success {
        border-left: 5px solid #16a34a;
        background: linear-gradient(135deg, rgba(220, 252, 231, 0.95), rgba(236, 253, 245, 0.9));
    }
    .result-warning {
        border-left: 5px solid #dc2626;
        background: linear-gradient(135deg, rgba(254, 226, 226, 0.96), rgba(255, 241, 242, 0.9));
    }
    .result-label {
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-size: 0.72rem;
        font-weight: 800;
        color: #334155;
        margin-bottom: 0.35rem;
    }
    .result-message {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0f172a;
        margin: 0;
    }
    .sidebar-card {
        padding: 1rem;
        margin-top: 1rem;
    }
    .sidebar-title {
        font-size: 1rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0.3rem;
    }
    .sidebar-note {
        color: #475569;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def render_hero():
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-kicker">Clinical decision support dashboard</div>
            <h1 class="hero-title">Multiple Disease Prediction System</h1>
            <p class="hero-copy">
                A cleaner, more interactive interface for diabetes, heart disease, and Parkinson's predictions.
                Use the sidebar to switch models, enter values with guided controls, and get an immediate result.
            </p>
            <div class="pill-row">
                <span class="pill">Interactive forms</span>
                <span class="pill">Responsive layout</span>
                <span class="pill">Model-backed predictions</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metrics():
    col1, col2, col3 = st.columns(3)
    cards = [
        (col1, "Diabetes", "8 inputs", "Uses the cleaned diabetes model"),
        (col2, "Heart", "13 inputs", "Encoded values with guided controls"),
        (col3, "Parkinson's", "22 inputs", "Structured in a compact form"),
    ]
    for col, label, value, subtitle in cards:
        with col:
            st.markdown(
                f"""
                <div class="hero-card metric-card">
                    <div class="metric-label">{label}</div>
                    <p class="metric-value">{value}</p>
                    <div class="metric-sub">{subtitle}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_result(is_positive, positive_text, negative_text):
    class_name = "result-warning" if is_positive else "result-success"
    message = positive_text if is_positive else negative_text
    st.markdown(
        f"""
        <div class="result-card {class_name}">
            <div class="result-label">Prediction Result</div>
            <p class="result-message">{message}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def int_input(label, value, min_value=None, max_value=None, help_text=None):
    return int(
        st.number_input(
            label,
            value=int(value),
            min_value=int(min_value) if min_value is not None else None,
            max_value=int(max_value) if max_value is not None else None,
            step=1,
            format="%d",
            help=help_text,
        )
    )


def float_input(label, value, min_value=None, max_value=None, step=0.1, help_text=None, format="%.3f"):
    return float(
        st.number_input(
            label,
            value=float(value),
            min_value=float(min_value) if min_value is not None else None,
            max_value=float(max_value) if max_value is not None else None,
            step=float(step),
            format=format,
            help=help_text,
        )
    )


render_hero()
render_metrics()

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-card">
            <div class="sidebar-title">Prediction Navigator</div>
            <div class="sidebar-note">
                Choose a disease model below. Inputs are organized as forms so you can review and submit in one step.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    selected = option_menu(
        "Select model",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
        icons=["activity", "heart", "person"],
        default_index=0,
        menu_icon="hospital",
    )
    st.markdown(
        """
        <div class="sidebar-card">
            <div class="sidebar-title">Quick Tip</div>
            <div class="sidebar-note">
                Use the sample-style defaults as a starting point, then adjust the controls to match the patient record.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if selected == "Diabetes Prediction":
    st.markdown(
        """
        <div class="panel-card">
            <h2 class="panel-title">Diabetes Prediction</h2>
            <p class="panel-copy">Enter the 8 clinical measures used by the model. The form layout makes the workflow faster and easier to scan.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("diabetes_form"):
        left, right = st.columns(2)
        with left:
            pregnancies = int_input("Pregnancies", 5, 0, 20, "Number of pregnancies")
            glucose = float_input("Glucose Level", 89, 0, 400, 1.0, "Plasma glucose concentration")
            blood_pressure = float_input("Blood Pressure", 72, 0, 300, 1.0, "Diastolic blood pressure")
            skin_thickness = float_input("Skin Thickness", 1, 0, 100, 1.0, "Triceps skin fold thickness")
        with right:
            insulin = float_input("Insulin Level", 175, 0, 1000, 1.0, "2-Hour serum insulin")
            bmi = float_input("BMI", 25.8, 0, 100, 0.1, "Body mass index")
            dpf = float_input("Diabetes Pedigree Function", 0.587, 0, 5, 0.001, "Family history score")
            age = int_input("Age", 51, 0, 120, "Age in years")

        submitted = st.form_submit_button("Run Diabetes Prediction", use_container_width=True)

    if submitted:
        prediction = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
        render_result(
            prediction[0] == 1,
            "Person is Diabetic",
            "Person is Not Diabetic",
        )


if selected == "Heart Disease Prediction":
    st.markdown(
        """
        <div class="panel-card">
            <h2 class="panel-title">Heart Disease Prediction</h2>
            <p class="panel-copy">This model expects encoded clinical features. The form keeps the interface structured while preserving the exact training inputs.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("heart_form"):
        left, right = st.columns(2)
        with left:
            age = int_input("Age", 54, 0, 120, "Age in years")
            sex = st.selectbox("Sex (encoded)", options=[0, 1], index=1, help="0 = female, 1 = male")
            cp = st.selectbox("Chest Pain Type (encoded)", options=[0, 1, 2, 3], index=2, help="Encoded chest pain category")
            trestbps = float_input("Resting Blood Pressure", 130, 0, 300, 1.0, "Resting blood pressure")
            chol = float_input("Serum Cholesterol", 246, 0, 700, 1.0, "Serum cholesterol in mg/dl")
            fbs = st.select_slider("Fasting Blood Sugar ", options=[0, 1], value=0, help="0 = false, 1 = true")
        with right:
            restecg = st.selectbox("Resting ECG", options=[0, 1, 2], index=1, help="Encoded resting ECG value")
            thalach = float_input("Maximum Heart Rate", 150, 0, 250, 1.0, "Maximum heart rate achieved")
            exang = st.select_slider("Exercise Induced Angina ", options=[0, 1], value=0, help="0 = no, 1 = yes")
            oldpeak = float_input("Oldpeak", 1.0, 0, 10, 0.1, "ST depression induced by exercise")
            slope = st.select_slider("Slope", options=[0, 1, 2], value=1, help="Encoded slope value")
            ca = int_input("CA", 0, 0, 4, "Number of major vessels")
            thal = st.select_slider("Thal (encoded)", options=[0, 1, 2, 3], value=2, help="Encoded thalassemia value")

        submitted = st.form_submit_button("Run Heart Prediction", use_container_width=True)

    if submitted:
        prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        render_result(
            prediction[0] == 1,
            "Person has Heart Disease",
            "Person does not have Heart Disease",
        )


if selected == "Parkinsons Prediction":
    st.markdown(
        """
        <div class="panel-card">
            <h2 class="panel-title">Parkinson's Disease Prediction</h2>
            <p class="panel-copy">The Parkinson's model uses 22 acoustic and speech measurements. The inputs are grouped into a denser but cleaner form.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("parkinsons_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            fo = float_input("MDVP:Fo(Hz)", 119.992, 0, 1000, 0.001)
            fhi = float_input("MDVP:Fhi(Hz)", 157.302, 0, 1000, 0.001)
            flo = float_input("MDVP:Flo(Hz)", 74.997, 0, 1000, 0.001)
            jitter_percent = float_input("MDVP:Jitter(%)", 0.00784, 0, 1, 0.0001)
            jitter_abs = float_input("MDVP:Jitter(Abs)", 0.00007, 0, 1, 0.00001)
            rap = float_input("MDVP:RAP", 0.00370, 0, 1, 0.0001)
            ppq = float_input("MDVP:PPQ", 0.00554, 0, 1, 0.0001)
            ddp = float_input("Jitter:DDP", 0.01109, 0, 1, 0.0001)
        with col2:
            shimmer = float_input("MDVP:Shimmer", 0.04374, 0, 1, 0.0001)
            shimmer_db = float_input("MDVP:Shimmer(dB)", 0.426, 0, 10, 0.001)
            apq3 = float_input("Shimmer:APQ3", 0.02182, 0, 1, 0.0001)
            apq5 = float_input("Shimmer:APQ5", 0.03130, 0, 1, 0.0001)
            apq = float_input("MDVP:APQ", 0.02971, 0, 1, 0.0001)
            dda = float_input("Shimmer:DDA", 0.06545, 0, 1, 0.0001)
            nhr = float_input("NHR", 0.02211, 0, 1, 0.0001)
            hnr = float_input("HNR", 21.033, 0, 100, 0.001)
        with col3:
            rpde = float_input("RPDE", 0.414783, 0, 1, 0.000001)
            dfa = float_input("DFA", 0.815285, 0, 1, 0.000001)
            spread1 = float_input("Spread1", -4.813, -50, 50, 0.001)
            spread2 = float_input("Spread2", 0.266482, -50, 50, 0.000001)
            d2 = float_input("D2", 2.301442, 0, 50, 0.001)
            ppe = float_input("PPE", 0.284654, 0, 1, 0.000001)

        submitted = st.form_submit_button("Run Parkinson's Prediction", use_container_width=True)

    if submitted:
        prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])
        render_result(
            prediction[0] == 1,
            "Person has Parkinson's Disease",
            "Person does not have Parkinson's Disease",
        )