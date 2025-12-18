import streamlit as st

# [중요] 에러 방지를 위해 st.set_page_config()를 과감히 생략하거나 
# 아주 단순하게 타이틀만 설정합니다.
st.title("MBTI 진로 & 도서 추천")

# 1. 데이터 사전
mbti_db = {
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

# 2. UI 구성
st.write("나의 MBTI를 선택하면 어울리는 진로와 책을 추천해 드립니다.")

# 가나다순 정렬하여 선택 박스 생성
mbti_list = sorted(list(mbti_db.keys()))
selected = st.selectbox("당신의 MBTI는?", mbti_list)

if selected:
    info = mbti_db[selected]
    
    st.write("---")
    st.header(f"✨ {selected} 유형을 위한 추천")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 추천 진로")
        st.write(f"1. {info['jobs'][0]}")
        st.write(f"2. {info['jobs'][1]}")
        
    with col2:
        st.subheader("📖 추천 도서")
        st.info(f"**{info['book']}**")

    # 성공 효과
    st.balloons()
