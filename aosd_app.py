import numpy as np
import streamlit as st

def calculate_probability(WBC, APTT, PLT, Ferritin, Creatinine):
    beta_0 = -2.5
    beta_WBC = 0.3
    beta_APTT = -0.2
    beta_PLT = 0.15
    beta_Ferritin = 0.001
    beta_Creatinine = -0.05
    logit = beta_0 + beta_WBC*WBC + beta_APTT*APTT + beta_PLT*PLT + beta_Ferritin*Ferritin + beta_Creatinine*Creatinine
    return 1 / (1 + np.exp(-logit))

st.title("AOSD 预测工具")
st.write("输入实验室指标：")
WBC = st.number_input("WBC (x10⁹/L)", min_value=0.0, value=10.0)
APTT = st.number_input("APTT (秒)", min_value=0.0, value=30.0)
PLT = st.number_input("PLT (x10⁹/L)", min_value=0.0, value=200.0)
Ferritin = st.number_input("铁蛋白 (ng/mL)", min_value=0.0, value=500.0)
Creatinine = st.number_input("肌酐 (μmol/L)", min_value=0.0, value=80.0)

if st.button("计算"):
    prob = calculate_probability(WBC, APTT, PLT, Ferritin, Creatinine)
    st.success(f"AOSD 概率：{prob:.1%}")
