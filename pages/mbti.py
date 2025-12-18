import streamlit as st
from datetime import datetime

# 1. 페이지 설정 (최상단)
st.set_page_config(page_title="오픈 마켓", page_icon="🛍️", layout="centered")

# 2. 데이터 저장소(Session State) 초기화
# 앱이 처음 실행될 때 'items' 리스트가 없으면 생성합니다.
if "items" not in st.session_state:
    st.session_state["items"] = []

# 3. 사이드바: 상품 등록 양식
with st.sidebar:
    st.header("🎁 내 물건 팔기")
    with st.form("upload_form", clear_on_submit=True):
        name = st.text_input("판매자 닉네임")
        title = st.text_input("물건 이름")
        price = st.text_input("가격 (원)")
        img_file = st.file_uploader("사진 업로드", type=['jpg', 'png', 'jpeg'])
        submit_btn = st.form_submit_button("등록 완료")
        
        if submit_btn:
            if name and title and img_file:
                # 새 아이템 생성
                new_post = {
                    "id": len(st.session_state["items"]),
                    "seller": name,
                    "title": title,
                    "price": price,
                    "image": img_file.read(),
                    "chats": [],
                    "time": datetime.now().strftime("%H:%M")
                }
                # 최신글이 위로 오게 저장
                st.session_state["items"].insert(0, new_post)
                st.success("물건이 등록되었습니다!")
            else:
                st.error("모든 항목을 입력하고 사진을 올려주세요.")

# 4. 메인 화면: 물건 목록 및 채팅
st.title("🛍️ 우리동네 중고장터")
st.write("등록된 물건을 확인하고 댓글로 대화해보세요.")
st.divider()

# 데이터가 없을 때 메시지
if not st.session_state["items"]:
    st.info("아직 등록된 물건이 없습니다. 왼쪽 메뉴에서 물건을 등록해보
