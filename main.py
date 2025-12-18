import streamlit as st

# 1. 앱 설정 및 테마 느낌 (학교 상징성을 고려한 설정)
st.set_page_config(page_title="동근: 동덕여고 근처", page_icon="🏫", layout="wide")

# 2. 데이터 유실 방지 및 초기화
if 'items' not in st.session_state or st.session_state.items is None:
    # 샘플 데이터 (학교 생활 관련)
    st.session_state.items = [
        {"id": 1, "title": "수능완성 미개봉 판매", "price": "5,000", "tag": "도서/참고서", "desc": "깨끗한 새 책입니다. 2층 복도에서 직거래해요!", "img": None},
        {"id": 2, "title": "동덕 체육복 상의(L)", "price": "10,000", "tag": "의류/교복", "desc": "세탁 완료했습니다. 상태 좋아요.", "img": None}
    ]

if 'msgs' not in st.session_state:
    st.session_state.msgs = []

# 3. 사이드바 메뉴 디자인
st.sidebar.title("🏫 동근 (DD-Geun)")
st.sidebar.caption("동덕여자고등학교 학생 전용 장터")
menu = ["🏠 동근 홈", "✍️ 판매글 올리기", "💬 동근채팅", "👤 마이페이지"]
page = st.sidebar.radio("메뉴 이동", menu)

# 검색창을 사이드바 하단에 배치
st.sidebar.divider()
search_query = st.sidebar.text_input("🔎 필요한 물건 검색", "")

# --- [1. 홈 화면: 물건 구경하기] ---
if page == "🏠 동근 홈":
    st.title("🍊 오늘 올라온 교내 물건")
    st.write(f"우리 학교 학생들끼리 안전하게 거래하세요!")
    
    # 데이터 가져오기 및 검색 필터링
    all_items = st.session_state.get('items', [])
    items = [i for i in all_items if search_query.lower() in i['title'].lower()]
    
    if not items:
        st.info("찾으시는 물건이 아직 없어요. 첫 번째 주인공이 되어보세요!")
    else:
        # 그리드 배치 (2열)
        cols = st.columns(2)
        for idx, item in enumerate(reversed(items)):
            with cols[idx % 2]:
                with st.container(border=True):
                    if item.get('img'):
                        st.image(item['img'], use_container_width=True)
                    else:
                        st.write("📸 등록된 사진이 없습니다")
                    
                    st.subheader(item['title'])
                    st.write(f"**가격: {item['price']}원**")
                    st.caption(f"분류: {item['tag']} | {item['desc']}")
                    
                    if st.button("구매 문의하기", key=f"chat_{item['id']}"):
                        st.session_state.target = item['title']
                        st.success("채팅 메뉴로 이동하면 대화를 시작할 수 있습니다!")
                        st.toast(f"'{item['title']}' 채팅 연결 성공!")

# --- [2. 판매하기: 글 작성] ---
elif page == "✍️ 판매글 올리기":
    st.title("📝 물건 내놓기")
    st.info("판매글을 등록하면 친구들이 홈 화면에서 볼 수 있어요.")
    
    with st.form("sell_form", clear_on_submit=True):
        t = st.text_input("상품 제목", placeholder="예: 생물 요점정리 노트")
        p = st.number_input("희망 가격", min_value=0, step=500)
        c = st.selectbox("카테고리", ["도서/참고서", "의류/교복", "문구/팬시", "기타"])
        i = st.file_uploader("사진 첨부", type=['jpg', 'png'])
        d = st.text_area("상세 설명", placeholder="거래 희망 장소(매점 앞, 정문 등)를 적어주면 좋아요!")
        
        if st.form_submit_button("동근에 등록하기"):
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
                st.success("등록 완료! 홈 화면에서 확인해 보세요.")
                st.balloons()
            else:
                st.error("제목과 설명을 작성해 주세요.")

# --- [3. 채팅창: 소통하기] ---
elif page == "💬 동근채팅":
    st.title("💬 동근채팅")
    target = st.session_state.get('target', "친구")
    st.caption(f"대화 상대: {target}")
    
    # 채팅 내역 표시
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]):
            st.write(m["content"])
            
    if prompt := st.chat_input("메시지를 입력해 보세요."):
        st.session_state.msgs.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        # 가상 답변
        reply = f"반가워요! '{target}' 거래 가능할까요? 점심시간에 만나요!"
        st.session_state.msgs.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)

# --- [4. 설정: 데이터 관리] ---
else:
    st.title("👤 마이페이지")
    st.write("---")
    st.metric("나의 매너 점수", "100점", "최고에요!")
    st.write(f"내가 올린 판매글 수: **{len(st.session_state.items)}개**")
    
    if st.button("🛠️ 앱 초기화 (테스트 데이터 삭제)"):
        st.session_state.items = []
        st.session_state.msgs = []
        st.rerun()
