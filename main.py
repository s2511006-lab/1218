import streamlit as st

# 1. 앱 기본 설정
st.set_page_config(page_title="동근: 동덕여고 장터", page_icon="🏫", layout="wide")

# 2. 세션 상태 초기화 (에러 방지용 최우선 실행)
if 'items' not in st.session_state:
    st.session_state['items'] = []
if 'msgs' not in st.session_state:
    st.session_state['msgs'] = []

# 3. 사이드바 구성 (마이페이지 삭제)
st.sidebar.title("🏫 동근 (DD-Geun)")
st.sidebar.caption("동덕여고 학생들을 위한 안전 장터")

# 상단에 간략한 내 정보 표시 (마이페이지 대신)
item_count = len(st.session_state['items'])
st.sidebar.info(f"👤 내 판매글: {item_count}개 | 매너: 100점")

menu = ["🏠 동근 홈", "✍️ 판매글 올리기", "💬 동근채팅"]
page = st.sidebar.radio("메뉴 이동", menu)

st.sidebar.divider()
search_query = st.sidebar.text_input("🔎 물건 검색", "")

# --- [1. 홈 화면] ---
if page == "🏠 동근 홈":
    st.title("🍊 오늘 우리 동네 매물")
    
    # 데이터 필터링
    all_items = st.session_state['items']
    items = [i for i in all_items if search_query.lower() in i['title'].lower()]
    
    if not items:
        st.info("현재 등록된 물건이 없어요. 첫 번째 물건을 등록해 보세요!")
    else:
        cols = st.columns(2)
        for idx, item in enumerate(reversed(items)):
            with cols[idx % 2]:
                with st.container(border=True):
                    if item.get('img'):
                        st.image(item['img'], use_container_width=True)
                    else:
                        st.subheader("🖼️")
                    
                    st.subheader(item['title'])
                    st.write(f"**{item['price']}원**")
                    st.caption(f"분류: {item['tag']} | {item['desc']}")
                    
                    if st.button("문의하기", key=f"chat_{item['id']}"):
                        st.session_state.target = item['title']
                        st.toast("채팅방이 열렸습니다. 메뉴에서 확인하세요!")

# --- [2. 판매하기] ---
elif page == "✍️ 판매글 올리기":
    st.title("📝 물건 내놓기")
    with st.form("sell_form", clear_on_submit=True):
        t = st.text_input("상품 제목")
        p = st.number_input("가격 (원)", min_value=0, step=500)
        c = st.selectbox("분류", ["도서/참고서", "의류/교복", "문구", "기타"])
        i = st.file_uploader("사진", type=['jpg', 'png'])
        d = st.text_area("상세 설명")
        
        if st.form_submit_button("동근에 등록"):
            if t and d:
                new_item = {
                    "id": len(st.session_state['items']) + 1,
                    "title": t, 
                    "price": format(p, ','), 
                    "tag": c, 
                    "desc": d, 
                    "img": i
                }
                st.session_state['items'].append(new_item)
                st.success("매물이 성공적으로 등록되었습니다!")
                st.rerun()
            else:
                st.warning("제목과 설명을 적어주세요.")

# --- [3. 채팅창] ---
elif page == "💬 동근채팅":
    st.title("💬 동근채팅")
    target = st.session_state.get('target', "친구")
    st.caption(f"상대방: {target}")

    for m in st.session_state['msgs']:
        with st.chat_message(m["role"]):
            st.write(m["content"])
            
    if prompt := st.chat_input("메시지 입력"):
        st.session_state['msgs'].append({"role": "user", "content": prompt})
        st.session_state['msgs'].append({"role": "assistant", "content": f"'{target}' 거래 문의 확인했습니다! 어디서 만날까요?"})
        st.rerun()

# 데이터 초기화 버튼을 사이드바 맨 밑으로 이동
if st.sidebar.button("⚠️ 전체 데이터 삭제"):
    st.session_state['items'] = []
    st.session_state['msgs'] = []
    st.rerun()
