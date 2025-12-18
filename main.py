import streamlit as st

# 1. 앱 설정
st.set_page_config(page_title="동근: 동덕여고 장터", page_icon="🏫", layout="wide")

# 2. 데이터 초기화 (최상단에서 데이터 존재 여부를 강력하게 체크)
if 'items' not in st.session_state or st.session_state.items is None:
    st.session_state.items = []

if 'msgs' not in st.session_state:
    st.session_state.msgs = []

# 3. 사이드바 메뉴
st.sidebar.title("🏫 동근 (DD-Geun)")
st.sidebar.caption("동덕여고 학생 전용 안전 장터")
menu = ["🏠 동근 홈", "✍️ 판매글 올리기", "💬 동근채팅", "👤 마이페이지"]
page = st.sidebar.radio("메뉴 이동", menu)

st.sidebar.divider()
search_query = st.sidebar.text_input("🔎 물건 검색", "")

# --- [1. 홈 화면] ---
if page == "🏠 동근 홈":
    st.title("🍊 오늘 올라온 교내 물건")
    
    # 데이터 안전하게 가져오기
    current_items = st.session_state.get('items', [])
    items = [i for i in current_items if search_query.lower() in i['title'].lower()]
    
    if not items:
        st.info("아직 등록된 물건이 없어요!")
    else:
        cols = st.columns(2)
        for idx, item in enumerate(reversed(items)):
            with cols[idx % 2]:
                with st.container(border=True):
                    if item.get('img'):
                        st.image(item['img'], use_container_width=True)
                    st.subheader(item['title'])
                    st.write(f"**{item['price']}원**")
                    st.caption(f"{item['tag']} | {item['desc']}")
                    if st.button("문의하기", key=f"chat_{item['id']}"):
                        st.session_state.target = item['title']
                        st.success("채팅 메뉴로 이동해 주세요!")

# --- [2. 판매하기] ---
elif page == "✍️ 판매글 올리기":
    st.title("📝 물건 내놓기")
    with st.form("sell_form", clear_on_submit=True):
        t = st.text_input("상품 제목")
        p = st.number_input("가격", min_value=0, step=500)
        c = st.selectbox("분류", ["도서/참고서", "의류/교복", "문구", "기타"])
        i = st.file_uploader("사진", type=['jpg', 'png'])
        d = st.text_area("상세 설명")
        if st.form_submit_button("동근에 등록"):
            if t and d:
                new_item = {"id": len(st.session_state.items)+1, "title": t, "price": format(p, ','), "tag": c, "desc": d, "img": i}
                st.session_state.items.append(new_item)
                st.success("등록되었습니다!")
                st.rerun()

# --- [3. 채팅창] ---
elif page == "💬 동근채팅":
    st.title("💬 동근채팅")
    target = st.session_state.get('target', "친구")
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]):
            st.write(m["content"])
    if prompt := st.chat_input("메시지 입력"):
        st.session_state.msgs.append({"role": "user", "content": prompt})
        st.session_state.msgs.append({"role": "assistant", "content": f"'{target}' 거래 문의 확인했습니다!"})
        st.rerun()

# --- [4. 마이페이지: 에러 수정 지점] ---
else:
    st.title("👤 마이페이지")
    st.write("---")
    st.metric("나의 매너 점수", "100점")
    
    # 에러 방지: 데이터가 있는지 확인하고 길이를 잽니다.
    my_items_count = len(st.session_state.items) if st.session_state.items is not None else 0
    st.write(f"내가 올린 판매글 수: **{my_items_count}개**")
    
    if st.button("🛠️ 앱 전체 초기화"):
        st.session_state.items = []
        st.session_state.msgs = []
        st.rerun()
