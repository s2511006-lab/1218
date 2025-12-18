import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="당근마켓 클론", page_icon="🥕", layout="wide")

# 2. 데이터 초기화 (오류 방지를 위해 최상단 배치)
if 'items' not in st.session_state:
    st.session_state.items = [
        {"id": 1, "title": "맥북 에어 M2", "price": "1,100,000", "tag": "디지털기기", "desc": "상태 좋아요.", "img": None},
        {"id": 2, "title": "캠핑용 램프", "price": "30,000", "tag": "생활용품", "desc": "밤에 예뻐요.", "img": None}
    ]
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 3. 사이드바 메뉴
st.sidebar.title("🥕 당근마켓")
search_query = st.sidebar.text_input("🔍 상품 검색", "")
page = st.sidebar.radio("메뉴", ["🏠 홈", "✍️ 판매하기", "💬
