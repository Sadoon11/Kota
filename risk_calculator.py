import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

class RiskCalculator:
    def display_risk_assessment(self):
        st.subheader("تقييم مخاطر الاستثمار")
        
        # Risk Tolerance Quiz
        st.write("**استبيان تحمل المخاطر**")
        risk_questions = [
            "كم عمرك؟",
            "ما هو دخلك السنوي؟",
            "كم نسبة دخلك المستعد للاستثمار؟",
            "ما مدى تحملك لخسارة جزء من استثمارك؟"
        ]
        
        risk_scores = []
        for question in risk_questions:
            score = st.slider(question, 1, 10, 5)
            risk_scores.append(score)
        
        # Calculate Risk Profile
        total_risk_score = sum(risk_scores)
        risk_profile = self._determine_risk_profile(total_risk_score)
        
        st.subheader(f"ملف المخاطر: {risk_profile}")
        
        # Recommended Asset Allocation
        allocation = self._get_asset_allocation(risk_profile)
        st.subheader("توزيع الأصول الموصى به")
        
        # Visualization
        allocation_df = pd.DataFrame.from_dict(allocation, orient='index', columns=['النسبة'])
        st.bar_chart(allocation_df)
    
    def _determine_risk_profile(self, score):
        if score <= 15:
            return "محافظ جداً"
        elif 15 < score <= 25:
            return "محافظ"
        elif 25 < score <= 35:
            return "معتدل"
        else:
            return "مغامر"
    
    def _get_asset_allocation(self, risk_profile):
        allocations = {
            "محافظ جداً": {
                "السندات الحكومية": 70,
                "النقد": 20,
                "الأسهم": 10
            },
            "محافظ": {
                "السندات الحكومية": 50,
                "النقد": 20,
                "الأسهم": 30
            },
            "معتدل": {
                "السندات الحكومية": 30,
                "النقد": 10,
                "الأسهم": 60
            },
            "مغامر": {
                "السندات الحكومية": 10,
                "النقد": 10,
                "الأسهم": 80
            }
        }
        return allocations.get(risk_profile, allocations["معتدل"])
