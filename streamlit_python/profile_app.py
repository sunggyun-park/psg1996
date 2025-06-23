import streamlit as st
import base64

st.set_page_config(page_title="개인 프로필", layout="wide")

# 배경 이미지를 base64로 인코딩하는 함수
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

# 배경 이미지 설정
bg_image = get_base64_of_bin_file("data/background.jpeg")

if bg_image:
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 10px;
        backdrop-filter: blur(20px);
    }}
    
    .stApp, .stApp p, .stApp div, .stApp span, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, .stApp li {{
        color: black !important;
    }}
    
    .stMarkdown, .stMarkdown p, .stMarkdown div, .stMarkdown span, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6, .stMarkdown li {{
        color: black !important;
    }}
    
    .detail-content {{
        font-size: 18px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 1페이지
# 제목을 먼저 배치
st.markdown("<h3 style='text-align: right; color: black;'>No Pains, No Gains.</h3>", unsafe_allow_html=True)

# 사진과 개인정보를 같은 컬럼 구조로 배치
col1, col2 = st.columns([1, 1])

with col1:
    st.image("data/profile_photo.png", caption="개인 사진", width=350) #width를 조정 하면 이미지 비율에 따라서 높이가 자동으로 조절됩니다.
    
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("<h3 style='text-align: right; color: black; margin: 5px 0;'>이름: 박성균</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right; color: black; margin: 5px 0;'>전공: 재난소방안전</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right; color: black; margin: 5px 0;'>학교: 건양대학교 안보대학원</h3>", unsafe_allow_html=True)

st.markdown("---")

# 2페이지
col3, col4 = st.columns([1.5, 1.5])

with col3:
    st.markdown("### 학력사항")
    st.markdown('<div class="detail-content">- 청주공업고등학교<br>- 국가평생교육진흥원 정보처리학<br>- 고려사이버대학교 <strong>소방방재학과</strong><br>- 건양대학교 <strong>안보대학원</strong> 재난소방안전학 재학</div>', unsafe_allow_html=True)

    st.markdown("### 경력사항")
    st.markdown('<div class="detail-content">- 건강보험공단 청년인턴<br>- 대한민국 공군 병753기<br>- 대한민국 공군 부사관 226기/div>', unsafe_allow_html=True)

    st.markdown("### 수상경력")
    st.markdown('<div class="detail-content">- 국방부장관 개인상장<br>- 37사단장 개인표창<br>- 공군 제17전투비행단장 개인상장</div>', unsafe_allow_html=True)

    st.markdown("### 자격사항")
    st.markdown('<div class="detail-content">- 지게차운전기능사<br>- 전자기기기능사<br>- 정보처리기능사<br>- 산업안전산업기사/기사</div>', unsafe_allow_html=True)

with col4:
    st.image("data/profile_photo.png", caption="개인 사진", width=300) #width를 조정 하면 이미지 비율에 따라서 높이가 자동으로 조절됩니다.
