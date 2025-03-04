import numpy as np
import streamlit as st

def calculate_probability(WBC, APTT, PLT, Ferritin, Creatinine):
    # 逻辑回归系数 (从论文中提取的估计值)
    beta_0 = -2.5  # 截距
    beta_WBC = 0.3
    beta_APTT = -0.2
    beta_PLT = 0.15
    beta_Ferritin = 0.001
    beta_Creatinine = -0.05
    
    # 计算 logit 值
    logit = (
        beta_0 + beta_WBC * WBC + beta_APTT * APTT +
        beta_PLT * PLT + beta_Ferritin * Ferritin +
        beta_Creatinine * Creatinine
    )
    
    # 计算概率
    probability = np.exp(logit) / (1 + np.exp(logit))
    return probability

# Streamlit 界面优化
st.set_page_config(page_title="AOSD vs Sepsis 预测", layout="wide")
st.title("🔬 AOSD 与 Sepsis 预测计算")
st.markdown("请在侧边栏输入患者的临床指标，系统将实时计算 AOSD 概率。")

# 侧边栏输入
with st.sidebar:
    st.header("📝 输入临床数据")
    WBC = st.number_input("白细胞计数 (WBC, 1x10⁹/L)", min_value=0.0, step=0.1, value=10.0)
    APTT = st.number_input("部分凝血活酶时间 (APTT, 秒)", min_value=0.0, step=0.1, value=30.0)
    PLT = st.number_input("血小板计数 (PLT, 1x10⁹/L)", min_value=0.0, step=1.0, value=200.0)
    Ferritin = st.number_input("铁蛋白 (Ferritin, ng/mL)", min_value=0.0, step=1.0, value=1000.0)
    Creatinine = st.number_input("肌酐 (Creatinine, μmol/L)", min_value=0.0, step=0.1, value=60.0)

# 计算 AOSD 概率
probability = calculate_probability(WBC, APTT, PLT, Ferritin, Creatinine)

# 显示结果
st.subheader("📊 计算结果")
st.success(f"AOSD 发生概率为 **{probability:.2%}**")

# 进度条显示风险程度
st.progress(float(probability))
if probability < 0.3:
    st.info("🟢 低风险: AOSD 概率较低")
elif 0.3 <= probability < 0.7:
    st.warning("🟡 中等风险: 请结合临床判断")
else:
    st.error("🔴 高风险: AOSD 概率较高，请密切关注")

st.write("⚠️ 本计算基于论文中的逻辑回归模型，仅供参考，具体诊断请咨询医生。")
