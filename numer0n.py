import random

print("-ヌメロン-")
name = input("あなたの名前を入力してください：")
print(f"こんにちは！{name}さん")

#ランダムな数字3つ(重複ありok)
answer = [random.randint(0,9) for _ in range(3)]

# デバッグ
print(f"正解の番号：{answer}")

count = 0   #試行回数

while True:
    guess = input("3桁の数字を入力してください(例：123)：")

    #入力チェック
    if not guess.isdigit() or len(guess) !=3:
        print("⚠️ 3桁の数字を入力してください")
        continue

    guess_digits = [int(n)for n in guess]

#EAT/BITE 判定
#---EAT判定----
    eat = 0
    bite = 0
    temp_answer = answer.copy() #判定用コピー
    temp_guess = guess_digits.copy()

    #まずはEATをチェック
    for i in range(3):
        if temp_guess[i] == temp_answer[i]:
            eat += 1
            #判定済みの数字はNoneにしてBITE判定でカウントされないようにする
            temp_answer[i] = None
            temp_guess[i] = -1

    #次にBITEをチェック
    for i in range(3):
        if temp_guess[i] in temp_answer:
            bite += 1
            #カウント済みの数字は削除して重複カウントを防ぐ
            index = temp_answer.index(temp_guess[i])
            temp_answer[index] = None

    count += 1
    print(f"{eat} EAT, {bite}BITE")

#正解判定
    if eat == 3:
        print(f"正解です！{count}回目で当たりました")
        break


