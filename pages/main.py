import streamlit as st

# 1. 페이지 설정을 가장 먼저 실행하되, 중복 호출 방지를 위해 단순화
st.set_page_config(page_title="MBTI 진로 추천", layout="centered")

# 2. 데이터 (외부 라이브러리 미사용)
mbti_db = {
    "ISTJ": ["회계사", "공무원", "지적 대화를 위한 넓고 얕은 지식"],
    "ISFJ": ["간호사", "교사", "나미야 잡화점의 기적"],
    "INFJ": ["상담가", "작가", "데미안"],
    "INTJ": ["데이터 과학자", "전략가", "사피엔스"],
    "ISTP": ["엔지니어", "개발자", "프로젝트 헤일메리"],
    "ISFP": ["예술가", "디자이너", "달러구트 꿈 백화점"],
    "INFP": ["작가", "상담가", "어린 왕자"],
    "INTP": ["연구원", "철학자", "이기적 유전자"],
    "ESTP": ["기업가", "마케터", "부의 추월차선"],
    "ESFP": ["배우", "이벤트 기획자", "인생의 마지막 순간에서"],
    "ENFP": ["홍보 전문가", "카피라이터", "연금술사"],
    "ENTP": ["변호사", "발명가", "생각에 관한 생각"],
    "ESTJ": ["경영자", "관리자", "원칙"],
    "ESFJ": ["호텔리어", "상담사", "인간관계론"],
    "ENFJ": ["교사", "정치인", "정의란 무엇인가"],
    "ENTJ": ["CEO", "컨설턴트", "승자의 법칙"]
}

# 3. UI 구현
st.title("💡 MBTI별 추천 진로 & 도서")
st.info("자신의 MBTI를 선택하면 맞춤형 정보를 제공합니다.")

# 드롭다운 메뉴
mbti_list = sorted(list(mbti_db.keys()))
user_choice = st.selectbox("MBTI 유형을 선택하세요", mbti_list)

if user_choice:
    data = mbti_db[user_choice]
    
    st.markdown("---")
    st.subheader(f"✨ {user_choice} 유형 결과")
    
    # 결과
