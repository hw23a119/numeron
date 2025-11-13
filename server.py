import socket
import random

# サーバー設定
host = "0.0.0.0"
port = 50001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print("待機中...")

conn, addr = server.accept()
print(f"{addr} が接続しました")

# --- ① 答えを決定 ---
answer = [random.randint(0, 9) for _ in range(3)]
print(f"（デバッグ用）答え: {answer}")

# --- ② メインループ ---
while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    print(f"相手の推測: {data}")
    guess_digits = [int(n) for n in data if n.isdigit()]

    # --- 入力チェック ---
    if len(guess_digits) != 3:
        conn.send("⚠️ 3桁の数字を送ってください。".encode())
        continue

    # --- EAT / BITE 判定 ---
    eat = sum(1 for i in range(3) if guess_digits[i] == answer[i])
    bite = sum(1 for i in range(3) if guess_digits[i] in answer) - eat

    # --- 結果送信 ---
    if eat == 3:
        conn.send("🎉 正解！おめでとうございます！".encode())
        break
    else:
        msg = f"{eat} EAT, {bite} BITE"
        conn.send(msg.encode())

print("ゲーム終了。接続を閉じます。")
conn.close()
server.close()
