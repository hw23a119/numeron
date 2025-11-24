from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# ランダム答え（重複あり）
answer = [random.randint(0, 9) for _ in range(3)]
print(f"(デバッグ) 答え: {answer}")

# 履歴を保存するリスト（最大5件）
history = []   # ← 追加

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    # ✅ リセット時に送られてくる値（なければ空欄）
    last_answer = request.args.get("last", "")

    if request.method == "POST":
        guess = request.form.get("guess", "")

        if len(guess) != 3 or not guess.isdigit():
            result = "⚠️ 3桁の数字を入力してください"
        else:
            guess_digits = [int(n) for n in guess]
            eat = sum(1 for i in range(3) if guess_digits[i] == answer[i])
            bite = sum(1 for i in range(3) if guess_digits[i] in answer) - eat

            if eat == 3:
                result = f"🎉 正解！ 答えは {''.join(map(str, answer))}"
            else:
                result = f"{eat} EAT, {bite} BITE"

            # ✅ 履歴に追加
            history.insert(0, {"guess": guess, "eat": eat, "bite": bite})
            if len(history) > 5:
                history.pop()

    # ✅ last_answer と history をHTMLに渡すよう変更！
    return render_template(
        "index.html",
        result=result,
        answer=''.join(map(str, answer)),
        last_answer=last_answer,
        history=history
    )


@app.route("/reset")
def reset():
    global answer, history

    # 直前の答えを保存
    last_answer = ''.join(map(str, answer))

    # 新しい答えを生成
    answer = [random.randint(0, 9) for _ in range(3)]

    # 履歴リセット
    history = []

    # 「前回の答え」をURLパラメータで渡す
    return redirect(url_for("index", last=last_answer))