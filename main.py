import streamlit as st

# 1. 앱 설정
st.set_page_config(page_title="당근마켓 클론", page_icon="🥕", layout="wide")

# 2. 세션 상태 초기화 (데이터 저장소)
if 'items' not in st.session_state:
    st.session_state.items = [
        {"id": 1, "title": "맥북 에어 M2", "price": "1,100,000", "tag": "디지털기기", "desc": "상태 좋아요.", "img": None},
        {"id": 2, "title": "캠핑용 램프", "price": "30,000", "tag": "생활용품", "desc": "밤에 예뻐요.", "img": None}
    ]
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 3. 사이드바 - 이 부분에서 따옴표 오류가 나지 않도록 주의하세요!
st.sidebar.title("🥕 당근마켓")
search_query = st.sidebar.text_input("🔍 상품 검색", "")
# 메뉴 리스트를 변수로 따로 빼서 가독성을 높였습니다.
menu_options = ["🏠 홈", "✍️ 판매하기", "💬 당근채팅", "👤 내 정보"]
page = st.sidebar.radio("메뉴", menu_options)

# --- [페이지 1: 홈 화면] ---
if page == "🏠 홈":
    st.title("🍊 우리 동네 매물")
    
    # 검색어 필터링 (제목에 검색어가 포함된 것만 추출)
    display_items = [
        item for item in st.session_state.items
