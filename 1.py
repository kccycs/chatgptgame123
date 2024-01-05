import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 設定窗口大小
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jumping Ball Game")

# 定義顏色
white = (255, 255, 255)
black = (0, 0, 0)

# 定義球和障礙物的初始位置
ball_size = 30
ball_x, ball_y = width // 4, height - ball_size - 10
ball_velocity = 8

obstacle_width = 50
obstacle_height = 20
obstacle_velocity = 5
obstacle_gap = 150
obstacle_frequency = 25
obstacles = []

# 設定字體
font = pygame.font.Font(None, 36)

# 設定分數
score = 0

# 主遊戲迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 移動球
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x > 0:
        ball_x -= ball_velocity
    if keys[pygame.K_RIGHT] and ball_x < width - ball_size:
        ball_x += ball_velocity

    # 移動障礙物
    for obstacle in obstacles:
        obstacle[1] += obstacle_velocity

        # 檢查碰撞
        if (
            ball_x < obstacle[0] < ball_x + ball_size or
            ball_x < obstacle[0] + obstacle_width < ball_x + ball_size
        ) and (
            ball_y < obstacle[1] < ball_y + ball_size or
            ball_y < obstacle[1] + obstacle_height < ball_y + ball_size
        ):
            # 遊戲結束
            pygame.quit()
            sys.exit()

    # 生成新的障礙物
    if random.randint(1, obstacle_frequency) == 1:
        obstacle_x = random.randint(0, width - obstacle_width)
        obstacles.append([obstacle_x, 0])

    # 移除超出螢幕的障礙物
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < height]

    # 清除畫面
    screen.fill(black)

    # 繪製球
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    # 繪製障礙物
    for obstacle in obstacles:
        pygame.draw.rect(screen, white, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    # 更新分數
    score += 1

    # 顯示分數
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    # 更新畫面
    pygame.display.flip()

    # 控制遊戲更新速率
    pygame.time.Clock().tick(30)
