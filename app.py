import streamlit as st
import pickle
import numpy as np

# خوێندنەوەی مۆدێلە ڕاهێنراوەکە
model = pickle.load(open("frost_model.pkl", "rb"))

st.title("❄️ سیستەمی پێشبینیکردنی شەختە لە چۆمان")
st.write("ئەم پڕۆژەیە یارمەتی جووتیارانی باڵەکایەتی دەدات پێشبینی مەترسی سەرمای توند و شەختە بکەن.")

# خانەکانی وەگرتنی زانیاری لە بەکارهێنەر
temp_max = st.number_input("بەرزترین پلەی گەرمی بۆ سبەی (Celsius):", value=10.0)
temp_min = st.number_input("نزمترین پلەی گەرمی بۆ سبەی (Celsius):", value=-2.0)
wind_speed = st.number_input("خێرایی با (km/h):", value=15.0)

# دوگمەی پشکنین
if st.button("پشکنینی مەترسی شەختە"):
    # دروستکردنی داتا بۆ مۆدێلەکە
    input_data = np.array([[temp_max, temp_min, wind_speed]])
    prediction = model.predict(input_data)

    # نیشاندانەوەی ئەنجام
    if prediction[0] == 1:
        st.error("⚠️ ئاگاداری! مەترسی شەختە و زوقم هەیە بۆ سبەی شەو. پێویستە ڕکارەکان بپارێزرێن!")
    else:
        st.success("✅ مەترسی شەختە نییە، کەشوهەوا ئاساییە.")