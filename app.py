
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="给你一个小惊喜 💌",
    page_icon="💗",
    layout="centered"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg, #ffe1ec, #eee1ff, #fff0e5
    );
}

.main .block-container {
    max-width: 650px;
    padding-top: 5vh;
    padding-bottom: 5vh;
}

/* Center all buttons */

div[data-testid="stButton"] {
    display: flex;
    justify-content: center;
}

div[data-testid="stButton"] button {
    width: min(100%, 340px);
    min-height: 48px;
    border: 1px solid #f3b5d0;
    border-radius: 30px;
    background: linear-gradient(120deg, #ed9bbb, #bba0ee);
    color: white;
    font-size: 16px;
    font-weight: 600;
    transition: 0.3s;
}

div[data-testid="stButton"] button:hover {
    transform: translateY(-3px);
    border: 1px solid #d77aa9;
    color: white;
    box-shadow: 0 7px 20px #e8b5d0;
}

/* Main card */

[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.80);
    border: 1px solid rgba(255,255,255,0.9);
    border-radius: 28px;
    padding: 20px;
    box-shadow: 0 15px 45px rgba(160,90,140,0.13);
}

/* Titles */

h1 {
    color: #d45d91 !important;
    text-align: center;
    font-size: 31px !important;
}

h2, h3 {
    color: #c76b99 !important;
    text-align: center;
}

/* Chinese text */

p {
    text-align: center;
    color: #80516a;
    font-size: 17px;
    line-height: 1.9;
}

.small-text {
    color: #b78ba5;
    font-size: 13px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# ---------------- FLOATING HEARTS ----------------

components.html("""
<style>
.heart {
    position: fixed;
    bottom: -40px;
    animation: float 9s linear forwards;
    pointer-events: none;
    z-index: 999;
}

@keyframes float {
    to {
        transform: translateY(-110vh) rotate(360deg);
        opacity: 0;
    }
}
</style>

<script>
const symbols = ["💗", "💕", "💖", "🌸", "✨", "🦋"];

setInterval(() => {
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = symbols[
        Math.floor(Math.random() * symbols.length)
    ];

    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = (18 + Math.random() * 18) + "px";

    document.body.appendChild(heart);

    setTimeout(() => heart.remove(), 9000);
}, 650);
</script>
""", height=0)


# ---------------- SESSION STATE ----------------

if "page" not in st.session_state:
    st.session_state.page = 1

if "choice" not in st.session_state:
    st.session_state.choice = ""


def go_to(page):
    st.session_state.page = page


def select_answer(answer):
    st.session_state.choice = answer
    st.session_state.page = 6


# ---------------- PROGRESS ----------------

def progress():
    value = (st.session_state.page - 1) / 5

    st.progress(value)

    st.markdown(
        f"<p class='small-text'>第 {st.session_state.page} / 6 关 💗</p>",
        unsafe_allow_html=True
    )


# ---------------- WEBSITE ----------------

with st.container(border=True):

    progress()

    # PAGE 1

    if st.session_state.page == 1:

        st.markdown("# 💌")

        st.title("嗨，我亲爱的老公！")

        st.markdown("""
        <p>
        想我了吗？🥺<br>
        我可有点想你了哦！<br><br>
        我给你准备了一个小惊喜，<br>
        不许提前偷看！🤫💕
        </p>
        """, unsafe_allow_html=True)

        if st.button("好呀，我来看看！ →", key="p1"):
            go_to(2)
            st.rerun()


    # PAGE 2

    elif st.session_state.page == 2:

        st.markdown("# 🥰")

        st.title("第一个小问题！")

        st.markdown("""
        <p>
        你觉得我是什么样的人？🤭
        </p>
        """, unsafe_allow_html=True)

        if st.button("有一点点可爱！ 🌸", key="p2a"):
            go_to(3)
            st.rerun()

        if st.button("当然是特别可爱！ 💗", key="p2b"):
            go_to(3)
            st.rerun()

        st.markdown(
            "<p class='small-text'>提示：选第二个比较聪明哦！😂</p>",
            unsafe_allow_html=True
        )


    # PAGE 3

    elif st.session_state.page == 3:

        st.markdown("# 🤭")

        st.title("再问你一个！")

        st.markdown("""
        <p>
        如果我突然给你发消息，<br>
        你会怎么办？💕
        </p>
        """, unsafe_allow_html=True)

        if st.button("马上回复你！ 💌", key="p3a"):
            go_to(4)
            st.rerun()

        if st.button("立刻回复，还要逗逗你！ 😏", key="p3b"):
            go_to(4)
            st.rerun()


    # PAGE 4

    elif st.session_state.page == 4:

        st.markdown("# 📢")

        st.title("重要通知！")

        st.markdown("""
        <p>
        恭喜你！🎉<br><br>
        你已经正式成为我的<br>
        <b>专属开心果！💗</b>
        <br><br>
        你的工作包括：<br>
        陪我聊天、让我开心，<br>
        还有接受我的各种小调皮！😂
        <br><br>
        这份工作没有工资，<br>
        但是有很多很多惊喜！✨
        </p>
        """, unsafe_allow_html=True)

        if st.button("继续！我已经迫不及待了 →", key="p4"):
            go_to(5)
            st.rerun()


    # PAGE 5

    elif st.session_state.page == 5:

        st.markdown("# 🌷")

        st.title("最后一个问题！")

        st.markdown("""
        <p>
        你愿意继续陪我聊天，<br>
        让我偶尔捉弄你一下吗？😏💕
        </p>
        """, unsafe_allow_html=True)

        if st.button("当然愿意！💗", key="p5a"):
            select_answer("当然愿意！💗")
            st.rerun()

        if st.button("求之不得！😎", key="p5b"):
            select_answer("求之不得！😎")
            st.rerun()

        st.markdown(
            "<p class='small-text'>认真选哦！两个都是正确答案！🤭</p>",
            unsafe_allow_html=True
        )


    # PAGE 6 - FINAL REVEAL

    elif st.session_state.page == 6:

        st.balloons()

        st.markdown("# 🎉💗")

        st.title("哈哈哈哈！")

        st.markdown(
            f"<h3>{st.session_state.choice}</h3>",
            unsafe_allow_html=True
        )

        st.markdown("""
        <br>
        <h2>开个玩笑啦！😜</h2>

        <p>
        不过，逗你玩真的很有趣！💕
        <br><br>
        别太得意哦！🤭
        <br><br>
        希望你今天也能开心一点！🌸
        </p>

        <h2>拜拜啦，我的帅哥！💌</h2>

        <p class="small-text">
        秘密任务圆满完成！✨
        </p>
        """, unsafe_allow_html=True)

        if st.button("再玩一次 ↻", key="restart"):
            st.session_state.page = 1
            st.session_state.choice = ""
            st.rerun()
