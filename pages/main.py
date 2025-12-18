import streamlit as st

# 1. 오류 방지를 위해 가장 심플하게 시작
st.title("MBTI 진로 & 도서 추천")

# 2. 데이터 정의
mbti_info = {
    "ISTJ": {"jobs": ["회계사", "공무원"], "book": "지적 대화를 위한 넓고 얕은 지식"},
    "ISFJ": {"jobs": ["간호사", "사서"], "book": "나미야 잡화점의 기적"},
    "INFJ": {"jobs": ["상담가", "작가"], "book": "데미안"},
    "INTJ": {"jobs": ["데이터 과학자", "전략가"], "book": "사피엔스"},
    "ISTP": {"jobs": ["엔지니어", "파일럿"], "book": "프로젝트 헤일메리"},
    "ISFP": {"jobs": ["디자이너", "작곡가"], "book": "달러구트 꿈 백화점"},
    "INFP": {"jobs": ["상담가", "예술가"], "book": "어린 왕자"},
    "INTP": {"jobs": ["연구원", "프로그래머"], "book": "이기적 유전자"},
    "ESTP": {"jobs": ["경찰관", "사업가"], "book": "부의 추월차선"},
    "ESFP": {"jobs": ["연예인", "홍보 전문가"], "book": "인생의 마지막 순간에서"},
    "ENFP": {"jobs": ["마케터", "작가"], "book": "연금술사"},
    "ENTP": {"jobs": ["변호사", "기획자"], "book": "생각에 관한 생각"},
    "ESTJ": {"jobs": ["경영자", "관리자"], "book": "원칙"},
    "ESFJ": {"jobs": ["교사", "상담원"], "book": "인간관계론"},
    "ENFJ": {"jobs": ["정치인", "강사"], "book": "정의란 무엇인가"},
    "ENTJ": {"jobs": ["CEO", "컨설턴트"], "book": "승자의 법칙"}
}

# 3. 화면 구성
st.write("당신의 MBTI에 맞는 최적의 진로와 책을 확인하세요.")

mbti_list = list(mbti_info.keys())
choice = st.selectbox("MBTI를 선택
