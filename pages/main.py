import streamlit as st

# 페이지 설정 (가장 상단에 위치해야 함)
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🚀")

# 1. 데이터 베이스 (외부 라이브러리 없이 딕셔너리로 구현)
data = {
    "ISTJ": {"job": ["회계사", "물류 관리자"], "book": "지적 대화를 위한 넓고 얕은 지식"},
    "ISFJ": {"job": ["간호사", "사서"], "book": "나미야 잡화점의 기적"},
    "INFJ": {"job": ["상담가", "작가"], "book": "데미안"},
    "INTJ": {"job": ["전략가", "시스템 분석가"], "book": "사피엔스"},
    "ISTP": {"job": ["엔지니어", "파일럿"], "book": "프로젝트 헤일메리"},
    "ISFP": {"job": ["디자이너", "작곡가"], "book": "달러구트 꿈 백화점"},
    "INFP": {"job": ["사회복지사", "예술가"], "book": "어린 왕자"},
    "INTP": {"job": ["연구원", "프로그래머"], "book": "이기적 유전자"},
    "ESTP": {"job": ["경찰관", "영업사원"], "book": "부의 추월차선"},
    "ESFP": {"job": ["연예인", "이벤트 기획자"], "book": "인생의 마지막 순간에서"},
    "ENFP": {"job": ["카피라이터", "여행 작가"], "book": "연금술사"},
    "ENTP": {"job": ["발명가", "광고 디렉터"], "book": "생각에 관한 생각"},
    "ESTJ": {"job": ["관리자", "군 장교"], "book": "원칙 (레이 달리오)"},
    "ESFJ": {"job": ["초등교사", "상담사"], "book": "인간관계론"},
    "ENFJ": {"job": ["정치인", "교사"], "book": "정의란 무엇인가"},
    "ENTJ": {"job": ["기업가", "변호사"], "book": "승자의 법칙"}
}

# 2. 메인 화면 구성
st.title("🔍 MBTI 맞춤 진로 & 도서 추천")
st.markdown("---")

# 3. 사용자 선택 UI
mbti_list = sorted(list(data.keys()))
choice = st.selectbox("본인의 MBTI를 선택해 주세요.", mbti_list)

# 4. 결과 표시
if choice:
    st.write(f"### 💡 **{choice}** 유형을 위한 추천")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("🎯 **추천 진로**")
