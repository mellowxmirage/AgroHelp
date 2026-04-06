import pickle
import pandas as pd
import requests

ideal_npk_values = {
    "rice": [100, 50, 50],
    "maize": [120, 60, 40],
    "chickpea": [25, 50, 25],
    "kidneybeans": [30, 50, 30],
    "pigeonpeas": [25, 50, 25],
    "mothbeans": [25, 40, 25],
    "mungbean": [25, 50, 25],
    "blackgram": [25, 50, 25],
    "lentil": [30, 50, 25],
    "pomegranate": [180, 60, 180],
    "banana": [250, 80, 300],
    "mango": [300, 60, 300],
    "grapes": [200, 60, 200],
    "watermelon": [100, 50, 100],
    "muskmelon": [100, 50, 100],
    "apple": [300, 80, 300],
    "orange": [250, 60, 250],
    "papaya": [200, 60, 200],
    "coconut": [600, 120, 600],
    "cotton": [100, 50, 50],
    "jute": [80, 40, 40],
    "coffee": [150, 50, 150]
}

model=pickle.load(open("model/model.pkl","rb"))

def predict_crop(data):
    columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    
    input_df = pd.DataFrame([data], columns=columns)
    prediction= model.predict(input_df)
    return prediction [0]

def fertilizer_suggestion(crop,N,P,K):
    ideal=ideal_npk_values.get(crop,[])
    
    suggestions=[]

    if N < ideal[0]:
        suggestions.append(f"Add Nitrogen (Urea): +{ideal[0]-N}")
    if N > ideal[0]:
         suggestions.append(f"Reduce Nitrogen: excess of {N - ideal[0]}")

    if P < ideal[1]:
        suggestions.append(f"Add Phosphorus (DAP): +{ideal[1]-P}")
    if P > ideal[1]:
         suggestions.append(f"Reduce Nitrogen: excess of {P - ideal[1]}")

    if K < ideal[2]:
        suggestions.append(f"Add Potassium (MOP): +{ideal[2]-K}")
    if K > ideal[2]:
         suggestions.append(f"Reduce Nitrogen: excess of {N - ideal[0]}")

    if not suggestions:
         return ["Soil is well balanced"]

    return suggestions

API_KEY ="b73db496c2811f29b04d0cb4ce8a8093"

def get_Weather(City):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}&units=metric"
        response=requests.get(url)
        data = response.json()

        if "main" in data: 
             temp=data["main"]["temp"]
             humidity = data["main"]["humidity"]
             rainfall= data.get("rain",{}).get("1h",0)
             return temp,humidity,rainfall
        else:
             raise ValueError(f"Weather data not found for city: {City}, response: {data}")

def pest_risk(temp,humidity,rainfall):
     score=0
     if humidity > 70:
        score += 2
     if temp > 25:
         score += 2
     if rainfall>100:
          score+=1
    
     
     if score>=4:
          return ["High risk of pests🐛"]
     elif score>=2:
          return ["Moderate risk of pests🪱"]
     else:
          return ["Low Risk🥬"]

def yield_prediction(N,P,K,rainfall):
     base_yield=800
     if rainfall > 200:
        base_yield += 200
     elif N > 80:
        base_yield += 100
    
     return base_yield

def water_requirement(crop):
    water_data = {
        "rice": "High 💧💧💧",
        "wheat": "Medium 💧💧",
        "maize": "Low 💧"
    }
    return water_data.get(crop, "Medium")
     
     

