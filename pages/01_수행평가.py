import streamlit as st

st.set_page_config(page_title="MBTI Typing", page_icon="🧠")

st.title("🧠 MBTI 성격 유형 분석")
st.write("원하는 MBTI 유형을 입력하거나 선택하세요!")

# MBTI 옵션
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# Selectbox UI
selected_mbti = st.selectbox("MBTI 유형 선택", mbti_types, index=8)

# MBTI 설명 데이터
mbti_descriptions = {
    "ESTP": """
### 🔥 ESTP — 모험을 즐기는 해결사
- 현실적이고 실용적이며 빠른 문제 해결 능력을 가짐  
- 즉흥적이고 행동력이 뛰어남  
- 새로운 경험을 좋아하고 위험을 즐기는 경향  
- 사람들과 쉽게 친해지고 에너지가 넘침  
""",
    "ENFP": "### ENFP 설명...",
    "INTJ": "### INTJ 설명...",
    # 필요에 따라 추가 작성
}

# 결과 출력
st.subheader(f"🔎 {selected_mbti} 유형 분석 결과")
if selected_mbti in mbti_descriptions:
    st.markdown(mbti_descriptions[selected_mbti])
else:
    st.write("해당 MBTI 설명이 등록되지 않았습니다.")

