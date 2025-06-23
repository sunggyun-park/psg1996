import streamlit as st
import base64
import os

# 페이지 설정
st.set_page_config(page_title="개인 프로필", layout="wide")

# 배경 이미지 base64 인코딩
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

# background.jpeg 불러오기
bg_image = get_base64_of_bin_file("background.jpeg")

# 배경 이미지 설정
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
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }}

    .stApp, .stApp * {{
        color: black !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 제목
st.markdown("<h3 style='text-align: right;'>No Pains, No Gains.</h3>", unsafe_allow_html=True)

# 사진 + 기본 정보
col1, col2 = st.columns([1, 1])

with col1:
    img_path = os.path.abspath("성균.png")
    if os.path.exists(img_path):
        st.image(img_path, caption="개인 사진", width=350)
    else:
        st.error("❌ 성균.png 파일이 존재하지 않습니다. 경로를 다시 확인하세요.")

with col2:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right;'>이름: 박성균</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right;'>전공: 재난소방안전</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right;'>학교: 건양대학교 안보대학원</h3>", unsafe_allow_html=True)

st.markdown("---")

# 학력, 경력, 수상, 자격
col3, col4 = st.columns([1.5, 1.5])

with col3:
    st.markdown("### 학력사항")
    st.markdown("""
    - 청주공업고등학교  
    - 국가평생교육진흥원 정보처리학  
    - 고려사이버대학교 **소방방재학과**  
    - 건양대학교 **안보대학원** 재난소방안전학 재학
    """)

    st.markdown("### 경력사항")
    st.markdown("""
    - 건강보험공단 청년인턴  
    - 대한민국 공군 병 753기  
    - 대한민국 공군 부사관 226기
    """)

    st.markdown("### 수상경력")
    st.markdown("""
    - 국방부장관 개인상장  
    - 37사단장 개인표창  
    - 공군 제17전투비행단장 개인상장
    """)

    st.markdown("### 자격사항")
    st.markdown("""
    - 지게차운전기능사  
    - 전자기기기능사  
    - 정보처리기능사  
    - 산업안전산업기사 / 기사
    """)