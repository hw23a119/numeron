import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.text import LabelBase

# 日本語フォントを登録
# macOSの場合の例
LabelBase.register(name="MSGothic", fn_regular="/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc")
# Windowsの場合は以下のように置き換え
# LabelBase.register(name="MSGothic", fn_regular="C:\\Windows\\Fonts\\msgothic.ttc")

class NumeronApp(App):
    def build(self):
        # ランダムで答えを作成（0～9の3桁、重複あり）
        self.answer = [random.randint(0, 9) for _ in range(3)]
        print(f"(デバッグ) 答え: {self.answer}")

        # 画面のレイアウト（縦並び）
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # ラベル：説明文
        self.info_label = Label(
            text="3桁の数字を入力してね（例：523）",
            font_name="MSGothic"
        )
        layout.add_widget(self.info_label)

        # TextInput：数字入力欄
        self.input_box = TextInput(
            hint_text="数字を入力",
            multiline=False,
            input_filter='int',
            font_name="MSGothic"
        )
        layout.add_widget(self.input_box)

        # ボタン：送信
        submit_button = Button(text="送信", font_name="MSGothic")
        submit_button.bind(on_press=self.check_guess)
        layout.add_widget(submit_button)

        # ラベル：結果表示
        self.result_label = Label(text="", font_name="MSGothic")
        layout.add_widget(self.result_label)

        return layout

    def check_guess(self, instance):
        guess = self.input_box.text
        # 入力チェック
        if len(guess) != 3 or not guess.isdigit():
            self.result_label.text = "⚠️ 3桁の数字を入力してください"
            return

        guess_digits = [int(n) for n in guess]

        # EAT / BITE 判定
        eat = sum(1 for i in range(3) if guess_digits[i] == self.answer[i])
        bite = sum(1 for i in range(3) if guess_digits[i] in self.answer) - eat

        if eat == 3:
            self.result_label.text = f"🎉 正解！ 答えは {''.join(map(str, self.answer))}"
        else:
            self.result_label.text = f"{eat} EAT, {bite} BITE"

        # 入力欄をクリア
        self.input_box.text = ""

if __name__ == "__main__":
    NumeronApp().run()
