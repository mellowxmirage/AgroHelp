import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df=pd.read_csv("data/Crop_recommendation.csv")
X=df.drop('label',axis=1)
y=df['label']
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.2)
model=RandomForestClassifier()
model.fit(X_train,y_train)

with open("model/model.pkl","wb") as f :
    pickle.dump(model,f)
print("yipee")