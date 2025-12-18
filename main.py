import streamlit as st

st.set_page_config(page_title="당근마켓", layout="wide")

# 데이터 저장소 초기화
if 'items' not in st.session_state:
    st.session_state.items = [
        {"id": 1, "title": "맥북", "price": "1,100,000", "tag": "디지털", "desc": "상태굿", "img": None},
        {"id": 2, "title": "의자", "price": "30,000", "tag": "생활", "desc": "편함", "img": None}
    ]
if 'msgs' not in st.session_state:
    st.session_state.msgs = []

# 사이드바
st.sidebar.title("🥕 당근")
menu = ["홈", "판매", "채팅", "관리"]
page = st.sidebar.radio("메뉴", menu)

# 1. 홈 화면
if page == "홈":
    st.title("🍊 동네 매물")
    q = st.text_input("검색어 입력")
    
    # 필터링
    items = [i for i in st.session_state.items if q.lower() in i['title'].lower()]
    
    if not items:
        st.info("매물이 없어요.")
    else:
        cols = st.columns(2)
        for idx, item in enumerate(reversed(items)):
            with cols[idx % 2]:
                with st.container(border=True):
                    if item['img']:
                        st.image(item['img'], use_container_width=True)
                    st.subheader(item['title'])
                    st.write(f"**{item['price']}원**")
                    st.caption(f"{item['tag']} | {item['desc']}")
                    if st.button("채팅하기", key=f"b_{item['id']}"):
                        st.session_state.target = item['title']
                        st.toast("채팅방 생성!")

# 2. 판매하기
elif page == "판매":
    st.title("🎁 물건 팔기")
    with st.form("f", clear_on_submit=True):
        t = st.text_input("제목")
        p = st.number_input("가격", min_value=0)
        c = st.selectbox("분류", ["디지털", "생활", "가구"])
        i = st.file_uploader("사진", type=['jpg', 'png'])
        d = st.text_area("설명")
        if st.form_submit_button("등록"):
            new = {"id":len(st.session_state.items)+1, "title":t, "price":format(p,','), "tag":c, "desc":d, "img":i}
            st.session_state.items.append(new)
            st.success("등록 완료!")
            st.rerun()

# 3. 채팅
elif page == "채팅":
    st.title("💬 채팅")
    tgt = st.session_state.get('target', "판매자")
    st.caption(f"{tgt}님과의 대화")
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]):
            st.write(m["content"])
    if prmpt := st.chat_input("메시지"):
        st.session_state.msgs.append({"role": "user", "content": prmpt})
        st.session_state.msgs.append({"role": "assistant", "content": f"문의 감사합니다!"})
        st.rerun()

# 4. 관리
else:
    st.title("👤 설정")
    if st.button("초기화"):
        st.session_state.items = []
        st.session_state.msgs = []
        st.rerun()
