import streamlit as st

# 1. 앱 설정
st.set_page_config(page_title="당근마켓", page_icon="🥕", layout="wide")

# 2. 데이터 초기화
if 'items' not in st.session_state:
    st.session_state.items = [
        {"id": 1, "title": "맥북 에어 M2", "price": "1,100,000", "tag": "디지털", "desc": "깨끗해요", "img": None},
        {"id": 2, "title": "캠핑 의자", "price": "30,000", "tag": "생활", "desc": "편해요", "img": None}
    ]
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 3. 사이드바 메뉴
st.sidebar.title("🥕 당근마켓")
search_query = st.sidebar.text_input("🔍 검색", "")
menu = ["🏠 홈", "✍️ 판매", "💬 채팅", "👤 내정보"]
page = st.sidebar.radio("메뉴 선택", menu)

# --- [홈 화면] ---
if page == "🏠 홈":
    st.title("🍊 동네 매물")
    
    # 검색 필터링 (리스트 내포 방식을 안전하게 풀어서 씀)
    display_items = []
    for item in st.session_state.items:
        if search_query.lower() in item['title'].lower():
            display_items.append(item)

    if not display_items:
        st.info("매물이 없습니다.")
    else:
        cols = st.columns(2)
        for idx, item in enumerate(reversed(display_items)):
            with cols[idx %
