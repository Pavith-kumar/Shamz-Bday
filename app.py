import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Happy Birthday 💛", page_icon="💛", layout="centered")

# -------- UI + THEME --------

st.markdown("""
<style>

/* hide streamlit menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* yellow background */

[data-testid="stAppViewContainer"] {
background: linear-gradient(135deg,#ffd43b,#fab005);
}

/* center content */

.block-container {
max-width:600px;
margin:auto;
padding-top:20px;
}

/* white text */

h1,h2,h3,p,span,div {
color:white !important;
text-align:center;
}

/* buttons */

.stButton>button {
background:white;
color:#fab005;
border-radius:25px;
padding:12px 30px;
font-size:18px;
border:none;
font-weight:bold;
}

.stButton>button:hover {
background:#fff3bf;
}

/* floating hearts */

.heart {
position: fixed;
bottom: -20px;
font-size: 25px;
animation: floatUp 6s linear infinite;
color: #fff3bf;
opacity: 0.9;
}

@keyframes floatUp {
0% {
transform: translateY(0);
opacity: 1;
}
100% {
transform: translateY(-100vh);
opacity: 0;
}
}

</style>
""", unsafe_allow_html=True)

# -------- HEART ANIMATION SCRIPT --------

st.markdown("""
<script>

function createHeart(){
const heart = document.createElement("div");
heart.className = "heart";
heart.innerHTML = "💛";

heart.style.left = Math.random() * 100 + "vw";
heart.style.fontSize = (20 + Math.random() * 30) + "px";

document.body.appendChild(heart);

setTimeout(() => {
heart.remove();
}, 6000);
}

setInterval(createHeart, 400);

</script>
""", unsafe_allow_html=True)

# -------- HEADER --------

st.markdown(
"<h1 style='font-size:50px'>💛 Happy Birthday My Love 💛</h1>",
unsafe_allow_html=True
)

st.write("You make my world brighter every day ☀️")

# -------- SURPRISE BUTTON --------

if st.button("Tap to open your surprise 🎁"):

    st.subheader("💌 A Message For You")

    message = """From the day you came into my life,
everything became brighter.

Your smile lights up my world.
Your love makes my life beautiful.

I feel so lucky to have you.

Happy Birthday to the most amazing girl
I could ever ask for 💛"""

    placeholder = st.empty()

    typed = ""

    for char in message:
        typed += char
        placeholder.write(typed)
        time.sleep(0.03)

    st.divider()

    # -------- PHOTO GALLERY --------

    st.subheader("📸 Our Beautiful Memories")

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

    captions = [
        "Mah Girl 💛",
        "One of my favorite girl in this world ☀️",
        "Your beautiful smile 💛",
        "This is you with my love",
        "A moment I will never forget",
        "Another beautiful memory",
        "My forever favorite photo 💛",
        "Our First Memory"
    ]

    st.image(images, caption=captions)

    st.divider()

    # -------- LOVE TIMER --------

    st.subheader("⏳ Time With You")

    start = datetime(2021,4,30)
    today = datetime.now()

    days = (today - start).days

    st.write(f"We have been together for **{days} beautiful days 💛**")

    st.divider()

    # -------- GIFT --------

    st.subheader("🎁 Your Birthday Gift")

    if st.button("Open Gift 🎀"):

        st.balloons()

        st.markdown(
        "<h1 style='text-align:center'>🎂🎂🎂</h1>",
        unsafe_allow_html=True
        )

        st.image("gift.jpg")

        st.success("Happy Birthday My Love 💛")

    st.divider()

    # -------- PROPOSAL --------

    st.subheader("💍 One More Question")

    st.write("Will you stay with me forever? 💛")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💛"):
            st.balloons()
            st.success("You just made me the happiest person alive 💛")

    with col2:
        if st.button("Maybe 🤭"):
            st.warning("Take your time… my answer will always be YES for you 💛")