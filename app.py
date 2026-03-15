import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Happy Birthday 💛", page_icon="💛", layout="centered")

# -------- YELLOW MOBILE UI --------

st.markdown("""
<style>

/* hide streamlit menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* full yellow background */
[data-testid="stAppViewContainer"] {
background:#FFD43B;
}

/* center content */
.block-container {
max-width:420px;
margin:auto;
padding-top:30px;
}

/* white text */
h1,h2,h3,p,div,span {
color:white !important;
text-align:center;
}

/* buttons */
.stButton>button {
background:#FAB005;
color:white;
border:none;
border-radius:20px;
padding:12px 25px;
font-size:18px;
width:100%;
margin-top:10px;
}

/* button hover */
.stButton>button:hover {
background:#E0A800;
color:white;
}

</style>
""", unsafe_allow_html=True)

# -------- HEADER --------

st.markdown(
"<h1 style='font-size:42px'>💛 Happy Birthday My Love 💛</h1>",
unsafe_allow_html=True
)

st.write("You make my world brighter every day ☀️")

# -------- SURPRISE --------

if st.button("Tap to open your surprise 🎁"):

    st.subheader("💌 A Message For You")

    message = """From the day you came into my life,
everything became brighter.

Your smile lights up my world.
Your love makes my life beautiful.

Happy Birthday to the most amazing girl
I could ever ask for 💛"""

    placeholder = st.empty()
    text=""

    for char in message:
        text += char
        placeholder.write(text)
        time.sleep(0.03)

    st.divider()

    # -------- PHOTO GALLERY --------

    st.subheader("📸 Our Memories")

    images = [
        "photo 1.jpg",
        "photo 2.jpg",
        "photo 3.jpg",
        "photo 4.jpg",
        "photo 5.jpg",
        "photo 6.jpg",
        "photo 7.jpg",
        "photo 8.jpg"
    ]

    st.image(images)

    st.divider()

    # -------- DAYS COUNTER --------

    st.subheader("⏳ Time With You")

    start = datetime(2021,4,10)
    today = datetime.now()

    days = (today-start).days

    st.write(f"We have been together for **{days} days 💛**")

    st.divider()

    # -------- GIFT --------

    st.subheader("🎁 Your Birthday Gift")

    if st.button("Open Gift 🎀"):

        st.balloons()

        st.markdown("<h1>🎂</h1>", unsafe_allow_html=True)

        st.image("gift.jpg")

        st.write("Happy Birthday My Love 💛")

    st.divider()

    # -------- PROPOSAL --------

    st.subheader("💍 One More Question")

    st.write("Will you stay with me forever? 💛")

    col1,col2 = st.columns(2)

    with col1:
        if st.button("YES 💛"):
            st.balloons()
            st.write("You made me the happiest person alive 💛")

    with col2:
        if st.button("Maybe 🤭"):
            st.write("Take your time… my answer will always be YES 💛")
