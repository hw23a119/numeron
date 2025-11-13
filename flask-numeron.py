from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# ランダムで答えを作成（0～9の3桁、重複あり）
answer = [random.randint(0, 9) for _ in range(3)]
print(f"(デバッグ) 答え: {answer}")

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
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
