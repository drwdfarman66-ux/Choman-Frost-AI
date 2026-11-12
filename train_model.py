import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# خوێندنەوەی داتاکە
df = pd.read_csv("choman_weather.csv")

# دیاریکردنی شەختە (ئەگەر پلەی گەرمیی نزم لە 0 کەمتر بوو = 1، ئەگەر نەخێر = 0)
df["Frost"] = (df["temperature_2m_min"] < 0).astype(int)

X = df[["temperature_2m_max", "temperature_2m_min", "wind_speed_10m_max"]]
y = df["Frost"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ڕاهێنانی مۆدێلەکە
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# پاشەکەوتکردنی مۆدێلەکە
with open("frost_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("مۆدێلەکە بە سەرکەوتوویی ڕاهێنرا و فایلی 'frost_model.pkl' دروستبوو!")