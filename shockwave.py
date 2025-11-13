import pygame
import random
import math

# 初期化
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Firework Effect - Enhanced")

# 火花クラス
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = random.randint(40, 80)

        # 🔥 色のバリエーション（黄色〜赤系）
        color_options = [
            (255, random.randint(200, 230), 50),   # 明るい金色
            (255, random.randint(150, 200), 0),    # 橙色
            (255, random.randint(80, 150), 0),     # 濃いオレンジ〜赤
            (255, 255, random.randint(100, 180)),  # 白っぽい火花
        ]
        self.color = random.choice(color_options)

        self.size = random.randint(2, 4)

    def update(self):
        # 重力
        self.vy += 0.15
        # 位置更新
        self.x += self.vx
        self.y += self.vy
        # 摩擦で少しずつ減速
        self.vx *= 0.98
        self.vy *= 0.98
        # 寿命減少
        self.life -= 1

    def draw(self, surface):
        if self.life > 0:
            alpha = max(0, min(255, int(255 * (self.life / 80))))
            color = (*self.color, alpha)
            s = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            pygame.draw.circle(s, color, (self.size, self.size), self.size)
            surface.blit(s, (self.x - self.size, self.y - self.size))

# メインループ
particles = []
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # クリックで爆発
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for _ in range(100):
                particles.append(Particle(x, y))

    # 火花更新＆描画
    for p in particles[:]:
        p.update()
        p.draw(screen)
        if p.life <= 0:
            particles.remove(p)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
