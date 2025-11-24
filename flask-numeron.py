from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# ランダム答え（重複なし） — シャッフル方式
numbers = list(range(10))
random.shuffle(numbers)
answer = numbers[:3]
print(f"(デバッグ) 答え: {answer}")

# 履歴を保持（最新5件）
history = []

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

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

            # 履歴追加
            history.insert(0, {"guess": guess, "eat": eat, "bite": bite})
            if len(history) > 5:
                history.pop()

    return render_template("index.html", result=result, history=history)

@app.route("/reset")
def reset():
    global answer, history
    last_answer = ''.join(map(str, answer))

    # 新しい答え（重複なし） — シャッフル方式
    numbers = list(range(10))
    random.shuffle(numbers)
    answer = numbers[:3]

    history = []
    print(f"(デバッグ) 新しい答え: {answer}")
    return redirect(url_for("index", last=last_answer))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
