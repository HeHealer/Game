
from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="zh-CN">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>给你一个小惊喜 💌</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    overflow: hidden;
    font-family: "Microsoft YaHei", sans-serif;
    background: linear-gradient(135deg, #ffe0eb, #eadfff, #fff0e5);
    color: #874563;
}

.card {
    background: rgba(255,255,255,0.92);
    max-width: 470px;
    width: 100%;
    padding: 38px 24px;
    border-radius: 28px;
    text-align: center;
    box-shadow: 0 12px 40px rgba(150,80,120,0.2);
    animation: appear 0.7s ease;
    z-index: 2;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(25px) scale(.95);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

h1 {
    color: #d45d91;
    font-size: 27px;
}

p {
    font-size: 17px;
    line-height: 1.9;
}

button {
    background: linear-gradient(120deg, #ed8bb5, #ba8be8);
    color: white;
    border: none;
    border-radius: 30px;
    padding: 13px 22px;
    margin: 9px;
    font-size: 15px;
    cursor: pointer;
    transition: .3s;
}

button:hover {
    transform: scale(1.08);
    box-shadow: 0 5px 15px #e7a8c9;
}

.hidden {
    display: none;
}

.emoji {
    font-size: 48px;
    margin-bottom: 12px;
}

.small {
    font-size: 13px;
    color: #b7839d;
}

.heart {
    position: fixed;
    bottom: -40px;
    font-size: 25px;
    animation: float 8s linear forwards;
    pointer-events: none;
    z-index: 1;
}

@keyframes float {
    to {
        transform: translateY(-110vh) rotate(360deg);
        opacity: 0;
    }
}

</style>
</head>

<body>

<div class="card">

    <!-- PAGE 1 -->

    <div id="page1">

        <div class="emoji">💌</div>

        <h1>嗨，我亲爱的老公！💕</h1>

        <p>
            想我了吗？<br>
            我可有点想你了哦！🥺<br>
            快点击下面的按钮，看看我给你准备了什么惊喜吧！
        </p>

        <button onclick="nextPage(2)">
            继续看看 →
        </button>

        <p class="small">一条非常重要的小消息！🤫</p>

    </div>


    <!-- PAGE 2 -->

    <div id="page2" class="hidden">

        <div class="emoji">🥰</div>

        <h1>先告诉你一件事！</h1>

        <p>
            我本来想今天乖一点的……<br>
            可是一想到你，<br>
            就忍不住想逗逗你了！🤭
        </p>

        <button onclick="nextPage(3)">
            然后呢？ →
        </button>

    </div>


    <!-- PAGE 3 -->

    <div id="page3" class="hidden">

        <div class="emoji">📢</div>

        <h1>重要通知！</h1>

        <p>
            恭喜你！🎉<br>
            你已经正式成为我的<br>
            <b>专属开心果！</b> 💗
            <br><br>
            你的工作包括：<br>
            让我开心、陪我聊天，<br>
            还有接受我的各种小调皮！😂
        </p>

        <button onclick="nextPage(4)">
            我准备好了 →
        </button>

    </div>


    <!-- PAGE 4 -->

    <div id="page4" class="hidden">

        <div class="emoji">🌷</div>

        <h1>现在，请认真回答！</h1>

        <p>
            你愿意继续宠着我，<br>
            让我一直缠着你吗？😏💕
        </p>

        <button onclick="finish('当然愿意！💗')">
            当然愿意！💗
        </button>

        <button onclick="finish('求之不得！😏')">
            求之不得！😏
        </button>

        <p class="small">
            两个答案都很可爱，你自己选吧！🤭
        </p>

    </div>


    <!-- FINAL PAGE -->

    <div id="page5" class="hidden">

        <div class="emoji">😂💗</div>

        <h1>哈哈哈哈！</h1>

        <p id="answer"></p>

        <h2>开个玩笑啦！😜</h2>

        <p>
            不过，逗你玩真的很有趣！💕
            <br><br>
            别太得意哦！🤭
        </p>

        <p class="small">
            好啦，秘密任务完成！✨
        </p>

    </div>

</div>


<script>

function nextPage(number) {

    for (let i = 1; i <= 5; i++) {

        document.getElementById("page" + i)
        .classList.add("hidden");

    }

    document.getElementById("page" + number)
    .classList.remove("hidden");

}


function finish(choice) {

    document.getElementById("answer").innerText =
        choice + " 你选得不错嘛！";

    nextPage(5);

    for (let i = 0; i < 20; i++) {
        setTimeout(createHeart, i * 120);
    }

}


function createHeart() {

    let heart = document.createElement("div");

    heart.className = "heart";

    let emojis = ["💗", "💕", "💖", "🌸", "✨"];

    heart.innerHTML =
        emojis[Math.floor(Math.random() * emojis.length)];

    heart.style.left = Math.random() * 100 + "vw";

    document.body.appendChild(heart);

    setTimeout(() => heart.remove(), 8000);

}


setInterval(createHeart, 900);

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)
