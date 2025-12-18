import streamlit as st

# 1. 앱 설정
st.set_page_config(page_title="당근마켓", layout="wide")

# 2. 데이터 유실 방지 (데이터가 없으면 즉시 빈 리스트로 생성)
if 'items' not in st.session_state or st.session_state.items is None:
    st.session_state.items = []

if 'msgs' not in st.session_state:
    st.session_state.msgs = []

# 3. 사이드바 메뉴
st.sidebar.title("🥕 당근마켓")
menu = ["홈", "판매하기", "채팅", "설정"]
page = st.sidebar.radio("이동", menu)

# --- [홈 화면] ---
if page == "홈":
    st.title("🍊 우리동네 매물")
    q = st.text_input("검색어를 입력하세요", "")
    
    # 데이터 안전하게 가져오기
    all_items = st.session_state.get('items', [])
    
    # 검색 필터링
    items = [i for i in all_items if q.lower() in i['title'].lower()]
    
    if not items:
        st.info("등록된 상품이 없습니다.")
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
                    if st.button("채팅하기", key=f"chat_{item['id']}"):
                        st.session_state.target = item['title']
                        st.toast("채팅방이 생성되었습니다!")

# --- [판매하기] ---
elif page == "판매하기":
    st.title("🎁 내 물건 팔기")
    with st.form("sell_form", clear_on_submit=True):
        t = st.text_input("제목")
        p = st.number_input("가격", min_value=0, step=1000)
        c = st.selectbox("카테고리", ["디지털", "생활", "가구", "기타"])
        i = st.file_uploader("사진 업로드", type=['jpg', 'png'])
        d = st.text_area("설명")
        
        if st.form_submit_button("등록 완료"):
            if t and d:
                new_item = {
                    "id": len(st.session_state.items) + 1,
                    "title": t,
                    "price": format(p, ','),
                    "tag": c,
                    "desc": d,
                    "img": i
                }
                st.session_state.items.append(new_item)
                st.success("상품이 등록되었습니다!")
                st.rerun()

# --- [채팅] ---
elif page == "채팅":
    st.title("💬 당근채팅")
    target = st.session_state.get('target', "판매자")
    st.caption(f"상대방: {target}")
    
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]):
            st.write(m["content"])
            
    if prompt := st.chat_input("메시지를 보내세요"):
        st.session_state.msgs.append({"role": "user", "content": prompt})
        st.session_state.msgs.append({"role": "assistant", "content": "문의 감사합니다! 곧 답변 드릴게요."})
        st.rerun()

# --- [설정] ---
else:
    st.title("👤 설정")
    if st.button("데이터 전체 초기화"):
        st.session_state.items = []
        st.session_state.msgs = []
        st.rerun()
