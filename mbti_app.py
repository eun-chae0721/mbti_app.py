import streamlit as st

st.set_page_config(page_title="AI가 뽑은 나의 MBTI", layout="centered")

st.title("💡나의 MBTI는?💡")
st.subheader("데이터클라우드공학과 체험 부스")
st.write("아래 질문을 통해 MBTI를 확인해보세요!")

st.markdown("---")

# 질문지와 성향 매핑
questions = [
    ("나는 새로운 사람 만나는 게 좋아🥳", "EI", "E"),
    ("혼자 보내는 시간이 중요해🥱", "EI", "I"),
    ("인생은 꿈과 달라! 현실이지🥴", "SN", "S"),
    ("만약에~ 상상하는 재미!🤔", "SN", "N"),
    ("난 논리적으로 생각하는 게 좋아😎", "TF", "T"),
    ("나 우울해서 빵 샀어😭 왜 우울한지 궁금", "TF", "F"),
    ("내 인생은 계획대로🤫", "JP", "J"),
    ("여기까지 놀러왔는데 그냥 아무데나 들어가😋", "JP", "P")
]

scores = {
    "E": 0, "I": 0,
    "S": 0, "N": 0,
    "T": 0, "F": 0,
    "J": 0, "P": 0
}

st.markdown("### 질문에 1-5점으로 답해주세요 (1: 전혀 아니다, 5: 매우 그렇다)")

for q_text, axis, trait in questions:
    score = st.slider(q_text, 1,5,3, step=1, format="%d", key=q_text)
    scores[trait] += score

# 결과 계산
def get_mbti(scores):
    mbti = ''
    mbti += 'E' if scores['E'] >= scores['I'] else 'I'
    mbti += 'S' if scores['S'] >= scores['N'] else 'N'
    mbti += 'T' if scores['T'] >= scores['F'] else 'F'
    mbti += 'J' if scores['J'] >= scores['P'] else 'P'
    return mbti

if st.button("📊 결과 보기"):
    mbti = get_mbti(scores)
    st.markdown("---")
    st.success(f"당신의 MBTI는 🩵**{mbti}**🩵 입니다!")

    # 적합 유형
    recommended = ['INTJ', 'ENTP', 'ISTP', 'INFP']
    if mbti in recommended:
        st.info("✅ 당신은 데이터클라우드공학과와 잘 어울리는 유형이에요!")
    else:
        st.info("💡 다양한 관점에서 기술을 배우며 멋지게 성장할 수 있어요!")

    # 설명 예시
    mbti_explanations = {
        "ISTJ": "엑셀 안 맞으면 못 견디는 데이터 정리왕🗂️ AWS 콘솔도 깔끔하게 정리해놓는 성격",
        "ISFJ": "백엔드 깔끔한 사람은 따로🧹 남들 안 보는 부분까지 꼼꼼하게 챙기는 당신, 팀플 MVP",
        "INFJ": "데이터 속 숨은 의미까지 캐치하는 직관 보스📑 사용자 로그에서도 인류애를 찾는 천상 데이터 이상주의자",
        "INTJ": "파이썬, SQL, 인생 플랜까지 완벽 설계형🗓️ AI 프로젝트를 기획부터 배포까지 혼자 다 할 기세",
        "ISTP": "클라우드 인프라? 그냥 셋팅해봄☁️ 문제 생기면 튜닝하고 고치면서 배우는 기술 장인",
        "ISFP": "감성+데이터=시각화 천재🎨 워드 클라우드 하나에도 감정선은 심는 사람",
        "INFP": "의미 없는 데이터는 하기 싫어요👩🏻‍💻 가치있는 데이터만 분석하고 싶은, 세상을 바꾸고 싶은 마음",
        "INTP": "이 알고리즘은 왜 이렇게 동작하지?💭 논리로 세상을 해석하는 데이터 해커",
        "ESTP": "일단 돌리고 보자! 데이터는 현장에서 느껴야지👷🏻 현장 중심 분석가",
        "ESFP": "데이터도 사람처럼 다 다르잖아~👨🏻‍🏫 시각화 센스 넘치는 발표 장인",
        "ENFP": "왜 이 과를 선택했냐고? 재밌어 보이잖아!🎢 기획부터 배포까지 신박한 아이디어 폭발",
        "ENTP": "노코드 자동화 vs API 직접 연결? 비교 끝🎙️ 끊임없이 개선하고 비교하는 분석 마니아",
        "ESTJ": "Jupyter 노트북 구조가 이게 맞아야지📊 프로젝트 일정표를 Gantt Chart로 관리하는 실행리더",
        "ESFJ": "팀플에서 갈등요소 사전 조율 완료🧩 모두가 어울리는 환경을 만드는 부드러운 설계",
        "ENTJ": "파이프라인 구성은 이렇게, PM 역할은 나👑 스타트업 CEO 각",
        "ENFJ": "AI도 결국 사람을 위한 거잖아🤖 데이터 기반으로 사람을 돕고 싶은 리더형"
    }

    if mbti in mbti_explanations:
        st.write(f"🧠 {mbti_explanations[mbti]} 🧠")
    else:
        st.write("✨ MBTI에 맞는 특성과 함께 데이터 세상에 한 발 더 다가가보세요!")
