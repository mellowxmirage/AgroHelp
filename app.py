import streamlit as st
from utils import predict_crop, fertilizer_suggestion , get_Weather , pest_risk , yield_prediction, water_requirement

st.set_page_config(
    page_title="AgroHelp | Smart AI Platform",
    page_icon="🌱",
    #layout="wide"
)
st.title("🌾 AI-Based Smart Agriculture System")

st.header("Enter Soil Details")

# Inputs
N = st.number_input("Nitrogen (N)", min_value=0)
P = st.number_input("Phosphorus (P)", min_value=0)
K = st.number_input("Potassium (K)", min_value=0)

temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH Value")
rainfall = st.number_input("Rainfall (mm)")
city= st.text_input("Enter City for Weather Data")

# Button
if st.button("Predict Crop"):

    temp, humidity, rainfall_api = get_Weather(city)

    data = [N, P, K, temp, humidity, ph, rainfall_api]

    crop = predict_crop(data)
    fertilizer = fertilizer_suggestion(crop,N, P, K)
    risk=pest_risk(temp,humidity,rainfall_api)
    water = water_requirement(crop)
    yield1=yield_prediction(N,P,K,rainfall_api)

    st.success(f"🌾 Recommended Crop: {crop}")
    st.write(f"🐛 Pest Risk: {risk}")
    st.write(f"📈 Expected Yield: {yield1} kg/hectare")#you have to apply ml logic here
    st.write(f"💧 Water Requirement: {water}")
    st.write("🌱 Fertilizer Suggestions:")
    
    
    
    for f in fertilizer:
        st.write("-", f)
