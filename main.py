import streamlit as st
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(page_title="당근 마켓 클론", page_icon="🥕")

# 2. 데이터 초기화 (앱 실행 중 데이터 유지)
if 'items' not in st.session_state:
    st.session_state.items = [
        {
            "id": 1,
            "title": "아이폰 13 급처합니다",
            "price": "500,000",
            "content": "상태 깨끗해요. 직거래 선호합니다.",
            "time": "10분 전"
        },
        {
            "id": 2,
            "title": "캠핑용 의자 판매",
            "price": "25,000",
            "content": "두 번 사용했습니다. 가벼워요!",
            "time": "1시간 전"
        }
    ]

# 3. 사이드바 메뉴
menu = st.sidebar.selectbox("메뉴", ["홈", "판매하기", "내 정보"])

# --- 홈 화면 ---
if menu == "홈":
    st.title("🥕 당근 동네장터")
    st.write("우리 동네 따뜻한 거래를 경험해보세요.")
    st.divider()

    if not st.session_state.items:
        st.info("현재 등록된 매물이 없습니다.")
    else:
        for item in reversed(st.session_state.items):
            with st.container():
                col
