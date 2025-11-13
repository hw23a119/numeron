print("こんにちは")

name = input("あなたの名前を入力してください：")
print("こんにちは",name,"さん")

age = int(input(f"{name}の年齢を入力してください："))
print(f"{name}の年齢は",age,"ですね")

if age >= 20:
    print(name,"は大人です")
else:
    print(name,"は子供です")