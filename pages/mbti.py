import streamlit as st

# 에러 방지를 위해 텍스트 기반의 단순한 제목을 사용합니다.
st.markdown("# 🧬 MBTI 진로 & 도서 추천")
st.write("선택하신 MBTI 유형에 딱 맞는 커리어와 책을 추천해 드립니다.")

# 데이터베이스
mbti_data = {
    "ISTJ": {"jobs": ["회계사", "공무원"], "book": "지적 대화를 위한 넓고 얕은 지식"},
    "ISFJ": {"jobs": ["간호사", "사서"], "book": "나미야 잡화점의 기적"},
    "INFJ": {"jobs": ["상담가", "작가"], "book": "데미안"},
    "INTJ": {"jobs": ["데이터 과학자", "전략가"], "book": "사피엔스"},
    "ISTP": {"jobs": ["엔지니어", "소프트웨어 개발자"], "book": "프로젝트 헤일메리"},
    "ISFP": {"jobs": ["예술가", "디자이너"], "book": "달러구트 꿈 백화점"},
    "INFP": {"jobs": ["작가", "상담심리사"], "book": "어린 왕자"},
    "INTP": {"jobs": ["연구원", "철학자"], "book": "이기적 유전자"},
    "ESTP": {"jobs": ["기업가", "스포츠 매니저"], "book": "부의 추월차선"},
    "ESFP": {"jobs": ["연예인", "이벤트 플래너"], "book": "인생의 마지막 순간에서"},
    "ENFP": {"jobs": ["마케터", "홍보 전문가"], "book": "연금술사"},
    "ENTP": {"jobs": ["변호사", "광고 기획자"], "book": "생각에 관한 생각"},
    "ESTJ": {"jobs": ["경영자", "프로젝트 매니저"], "book": "원칙"},
    "ESFJ": {"jobs": ["초등교사", "호텔리어"], "book": "인간관계론"},
    "ENFJ": {"jobs": ["정치인", "시민단체 활동가"], "book": "정의란 무엇인가"},
    "ENTJ": {"jobs": ["CEO", "경영 컨설턴트"], "book": "승자의 법칙"}
}

# MBTI 선택 박스
choice = st.selectbox("당신의 MBTI를 선택하세요", sorted(mbti_data.keys()))

# 결과 출력 영역
if choice:
    res = mbti_data[choice]
    
    st.write("---")
    st.subheader(f"🔍 {choice} 유형을 위한 맞춤 정보")
    
    # 레이아웃 나누기
    left, right = st.columns(2)
    
    with left:
        st.info("🎯 **추천 진로**")
        st.write(f"1. {res['jobs'][0]}")
        st.write(f"2. {res['jobs'][1]}")
        
    with right:
        st.warning("📖 **추천 도서**")
        st.write(f"『{res['book']}』")

    # 디자인 효과
    st.balloons()
