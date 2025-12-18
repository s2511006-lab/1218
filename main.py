import streamlit as st
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(page_title="당근마켓 프로", page_icon="🥕", layout="wide")

# 2. 데이터 초기화 (상품 및 채팅 데이터)
if 'items' not in st.session_state:
    st.session_state.items = [
        {"id": 1, "title": "맥북 에어 M2", "price": "1,100,000", "tag": "디지털기기", "desc": "실사용 적어요.", "img": None},
        {"id": 2, "title": "캠핑용 램프", "price": "30,000", "tag": "생활용품", "desc": "감성 캠핑 가능!", "img": None}
    ]
if 'messages' not in st.session_state:
    st.session_state.messages = [] # 채팅 기록 저장

# 3. 사이드바 메뉴 및 검색
st.sidebar.title("🥕 당근마켓")
search_query = st.sidebar.text_input("🔍 상품 검색", placeholder="무엇을 찾으시나요?")
page = st.sidebar.radio("메뉴", ["🏠 홈", "✍️ 판매하기", "💬 당근채팅", "👤 내 정보"])

# --- [페이지 1: 홈 화면 (검색/필터 포함)] ---
if page == "🏠 홈":
    st.title("🍊 우리 동네 인기 매물")
    
    # 검색 로직 적용
    display_items = [
        item for item in st.session_state.items 
        if search_query.lower() in item['title'].lower() or search_query.lower() in item['desc'].lower()
    ]

    if not display_items:
        st.info("검색 결과가 없습니다.")
    else:
        # 그리드 레이아웃 (한 줄에 2개
