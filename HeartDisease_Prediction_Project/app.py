import streamlit as st
import pandas as pd
import joblib
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)
model=joblib.load("KNN_heart.pkl")
scaler=joblib.load("scaler.pkl")
expected_columns=joblib.load("columns.pkl")


st.markdown(
    "<h1 style='text-align: center;'>❤️ Heart Disease Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: gray;'>Enter your health details to get a prediction</p>",
    unsafe_allow_html=True
)
st.markdown("### 🩺 Patient Information")
st.caption("Please provide the patient's basic health details.")

st.markdown("""
<style>

    /* Main App Background */
    background: linear-gradient(
        135deg,
        #c5d0df 0%,
        #dbe3ed 50%,
        #b8c5d6 100%
    );
    padding-top: 3rem;

    /* Main Content */
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Title */
    h1 {
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 0.3rem;
    }

    /* Section Heading */
    h3 {
        margin-top: 2rem;
        margin-bottom: 0.2rem;
        font-weight: 700;
    }

    /* Input Labels */
    label {
        font-weight: 600 !important;
    }

    /* Input Boxes */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        border-radius: 10px;
    }

    /* Sliders */
    div[data-testid="stSlider"] {
        padding-top: 5px;
    }

    /* Predict Button */
    div[data-testid="stButton"] button {
        width: 100%;
        height: 3.2rem;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 700;
        border: none;
        transition: 0.2s;
    }

    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    }

    /* Success / Error Result */
    div[data-testid="stAlert"] {
        border-radius: 12px;
        padding: 1rem;
        margin-top: 1.5rem;
    }

    /* Caption */
    .stCaption {
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)



col1, col2 = st.columns(2)
with col1:
    age = st.slider("Age", 18, 100, 40)

with col2:
    sex = st.selectbox("SEX", ["M", "F"])


col1, col2 = st.columns(2)
with col1:
    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["ATA", "NAP", "TA", "ASY"]
    )

with col2:
    resting_bp = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        80, 200, 120
    )


col1, col2 = st.columns(2)
with col1:
    cholesterol = st.number_input(
        "Cholesterol (mg/dL)",
        100, 600, 200
    )

with col2:
    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dL",
        [0, 1]
    )


col1, col2 = st.columns(2)
with col1:
    resting_ecg = st.selectbox(
        "Resting ECG",
        ["Normal", "ST", "LVH"]
    )

with col2:
    max_hr = st.slider(
        "Max Heart Rate",
        60, 220, 150
    )


col1, col2 = st.columns(2)
with col1:
    exercise_angina = st.selectbox(
        "Exercise-Induced Angina",
        ["Y", "N"]
    )

with col2:
    oldpeak = st.slider(
        "Oldpeak (ST Depression)",
        0.0, 6.0, 1.0
    )


st_slope=st.selectbox("ST Slope",["Up","Flat","Down"])

if st.button("🔍 Predict Heart Disease", use_container_width=True):
    raw_input={
        "Age":age,
        "RestingBP":resting_bp,
        "Cholestrol":cholesterol,
        "FastingBS":fasting_bs,
        "MaxHR":max_hr,
        "Oldpeak":oldpeak,
        "Sex_"+sex:1,
        "ChestPainType_"+chest_pain:1,
        "RestingECG_"+resting_ecg:1,
        "ExerciseAngina_"+exercise_angina:1,
        "ST_Slope_"+st_slope:1
    }

    input_df=pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col]=0

    input_df=input_df[expected_columns]

    scaled_input=scaler.transform(input_df)
    prediction=model.predict(scaled_input)[0]

    if prediction == 1:
        st.error(
            "⚠️ **High Risk of Heart Disease**\n\n"
            "Please consult a healthcare professional for further evaluation."
        )
    else:
        st.success(
            "✅ **Low Risk of Heart Disease**\n\n"
            "The model predicts a lower risk based on the provided details."
        )

