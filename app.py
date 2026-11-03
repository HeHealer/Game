
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="给你一个小惊喜 💌",
    page_icon="💗",
    layout="centered"
)

# ---------- CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe0eb, #eadfff, #fff0e5);
}

.main .block-container {
    max-width: 650px;
    padding-top: 7vh;
}

h1 {
    color: #d45d91 !important;
    text-align: center;
}

p {
    color: #874563;
    font-size: 19px;
    text-align: center;
    line-height: 1.9;
}

div.stButton > button {
    background: linear-gradient(120deg, #ed8bb5, #ba8be8);
    color: white;
    border: none;
    border-radius: 30px;
    padding: 12px;
    font-size: 16px;
    width: 100%;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.04);
    color: white;
    border: none;
    box-shadow: 0 5px 15px #e7a8c9;
}

.card {
    background: rgba(255,255,255,0.85);
    padding: 30px 20px;
    border-radius: 25px;
    box-shadow: 0 10px 35px rgba(150,80,120,0.15);
    text-align: center;
}

.small {
    color: #b7839d;
    font-size: 13px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# ---------- FLOATING HEARTS ----------
components.html("""
<div id="hearts"></div>

<style>
body {
    overflow: hidden;
}
.heart {
    position: fixed;
    bottom: -30px;
    font-size: 24px;
    animation: float 8s linear forwards;
    pointer-events: none;
}
@keyframes float {
    to {
        transform: translateY(-110vh) rotate(360deg);
        opacity: 0;
    }
}
</style>

<script>
const symbols = ["💗", "💕", "💖", "🌸", "✨"];

setInterval(() => {
    let heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = symbols[
        Math.floor(Math.random() * symbols.length)
    ];
    heart.style.left = Math.random() * 100 + "vw";
    document.body.appendChild(heart);

    setTimeout(() => heart.remove(), 8000);
}, 600);
</script>
""", height=0)


# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 1

if "choice" not in st.session_state:
    st.session_state.choice = ""


def next_page(number):
    st.session_state.page = number


# ---------- MAIN CARD ----------
st.markdown('<div class="card">', unsafe_allow_html=True)


# PAGE 1
if st.session_state.page == 1:

    st.markdown("# 💌")
    st.title("嗨，我亲爱的老公！💕")

    st.markdown("""
    <p>
    想我了吗？<br>
    我可有点想你了哦！🥺<br>
    快点击下面的按钮，看看我给你准备了什么惊喜吧！
    </p>
    """, unsafe_allow_html=True)

    if st.button("继续看看 →"):
        next_page(2)
        st.rerun()

    st.markdown('<p class="small">一条非常重要的小消息！🤫</p>',
                unsafe_allow_html=True)


# PAGE 2
elif st.session_state.page == 2:

    st.markdown("# 🥰")
    st.title("先告诉你一件事！")

    st.markdown("""
    <p>
    我本来想今天乖一点的……<br>
    可是一想到你，<br>
    就忍不住想逗逗你了！🤭
    </p>
    """, unsafe_allow_html=True)

    if st.button("然后呢？ →"):
        next_page(3)
        st.rerun()


# PAGE 3
elif st.session_state.page == 3:

    st.markdown("# 📢")
    st.title("重要通知！")

    st.markdown("""
    <p>
    恭喜你！🎉<br>
    你已经正式成为我的<br>
    <b>专属开心果！💗</b>
    <br><br>
    你的工作包括：<br>
    让我开心、陪我聊天，<br>
    还有接受我的各种小调皮！😂
    </p>
    """, unsafe_allow_html=True)

    if st.button("我准备好了 →"):
        next_page(4)
        st.rerun()


# PAGE 4
elif st.session_state.page == 4:

    st.markdown("# 🌷")
    st.title("现在，请认真回答！")

    st.markdown("""
    <p>
    你愿意继续宠着我，<br>
    让我一直缠着你吗？😏💕
    </p>
    """, unsafe_allow_html=True)

    if st.button("当然愿意！💗"):
        st.session_state.choice = "当然愿意！💗"
        next_page(5)
        st.rerun()

    if st.button("求之不得！😏"):
        st.session_state.choice = "求之不得！😏"
        next_page(5)
        st.rerun()

    st.markdown(
        '<p class="small">两个答案都很可爱，你自己选吧！🤭</p>',
        unsafe_allow_html=True
    )


# PAGE 5
elif st.session_state.page == 5:

    st.balloons()

    st.markdown("# 😂💗")
    st.title("哈哈哈哈！")

    st.markdown(
        f"<h3 style='text-align:center;color:#d45d91;'>{st.session_state.choice}</h3>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <h2 style="text-align:center;color:#d45d91;">
    开个玩笑啦！😜
    </h2>

    <p>
    不过，逗你玩真的很有趣！💕<br><br>
    别太得意哦！🤭
    </p>

    <p class="small">
    好啦，秘密任务完成！✨
    </p>
    """, unsafe_allow_html=True)

    if st.button("再看一次 ↻"):
        next_page(1)
        st.rerun()


st.markdown('</div>', unsafe_allow_html=True)
