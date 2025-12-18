import streamlit as st

# 1. MBTI 데이터 구성 (진로 2가지, 추천 도서 1권)
mbti_data = {
    "ISTJ": {"careers": ["회계사", "공무원"], "book": "지적 대화를 위한 넓고 얕은 지식 (채사장)"},
    "ISFJ": {"careers": ["간호사", "초등교사"], "book": "나미야 잡화점의 기적 (히가시노 게이고)"},
    "INFJ": {"careers": ["상담심리사", "작가"], "book": "데미안 (헤르만 헤세)"},
    "INTJ": {"careers": ["데이터 과학자", "전략 기획가"], "book": "사피엔스 (유발 하라리)"},
    "ISTP": {"careers": ["엔지니어", "소프트웨어 개발자"], "book": "프로젝트 헤일메리 (앤디 위어)"},
    "ISFP": {"careers": ["예술가", "조경가"], "book": "달러구트 꿈 백화점 (이미예)"},
    "INFP": {"careers": ["상담가", "예술 치료사"], "book": "어린 왕자 (생텍쥐페리)"},
    "INTP": {"careers": ["연구원", "철학자"], "book": "이기적 유전자 (리처드 도킨스)"},
    "ESTP": {"careers": ["기업가", "스포츠 매니저"], "book": "부의 추월차선 (엠제이 드마코)"},
    "ESFP": {"careers": ["연예인", "이벤트 플래너"], "book": "인생의 마지막 순간에서 (샐리 티스데일)"},
    "ENFP": {"careers": ["마케터", "홍보 전문가"], "book": "연금술사 (파울로 코엘료)"},
    "ENTP": {"careers": ["변호사", "광고 기획자"], "book": "생각에 관한 생각 (대니얼 카너먼)"},
    "ESTJ": {"careers": ["경영자", "프로젝트 매니저"], "book": "원칙 (레이 달리오)"},
    "ESFJ": {"careers": ["홍보 담당자", "호텔리어"], "book": "인간관계론 (데일 카네기)"},
    "ENFJ": {"careers": ["비영리 단체장", "정치인"], "book": "정의란 무엇인가 (마이클 샌델)"},
    "ENTJ": {"careers": ["CEO", "경영 컨설턴트"], "book": "승자의 법칙 (잭 웰치)"},
}

# 2. 웹앱 UI 구성
st.set_page_config(page_title="MBTI 맞춤 추천 서비스", page_icon="📚")

st.title("✨ MBTI 맞춤 진로 & 도서 추천")
st.write("당신의 MBTI를 선택하면 가장 잘 어울리는 진로와 책을 추천해 드립니다.")

# 3. 사용자 입력 (MBTI 선택)
mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", mbti_list)

# 4. 결과 출력
if selected_mbti:
    result = mbti_data[selected_mbti]
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 추천 진로")
        for career in result["careers"]:
            st.write(f"- {career}")
            
    with col2:
        st.subheader("📖 추천 도서")
        st.info(f"**{result['book']}**")

    st.balloons()
