import random

print("--数字あてゲーム--")
name = input("あなたの名前を入力してください：")

print(f"こんにちは。{name}さん!\n1から100の中で数字を当ててみてください")

#ランダムに数字を選ぶ
answer = random.randint(1,100)

count = 0 #試行回数

while True:
    guess = int(input("数字を入力："))
    count += 1

    if guess < answer:
        print("もっと大きい数字です！：")
    elif guess > answer:
        print("もっと小さい数字です！")
    else:
        print(f"正解!{count}回目で当たりました!")
        break