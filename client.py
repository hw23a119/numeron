import socket

host = input("接続先のIPアドレス: ")
port = 50001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print("サーバーに接続しました！")

while True:
    # --- 数字入力 ---
    guess = input("あなたの推測（3桁の数字）: ")

    # --- 送信 ---
    client.send(guess.encode())

    # --- サーバーの返信を受信 ---
    data = client.recv(1024).decode()
    print(f"サーバー: {data}")

    # --- 正解なら終了 ---
    if "正解" in data:
        print("🎉 ゲームクリア！終了します。")
        break

client.close()
