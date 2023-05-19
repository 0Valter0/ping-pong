from pygame import *
font.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_weight, player_hight, player_speed, player_speed_x, player_speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_weight, player_hight))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.weight = player_weight
        self.hight = player_hight 
        self.speed = player_speed
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        ball.rect.x += self.speed_x
        ball.rect.y += self.speed_y
        if self.colliderect(platform_l.rect):
            self.speed_x *= -1
        if self.colliderect(platform_r.rect):
            self.speed_x *= -1  
        if self.rect.y > 450 or self.rect.y < 0:
            self.speed_y *= -1 

platform_l = Player('platform_l.png', 50, 50, 20, 100, 10, 4, 4)
platform_r = Player('platform_r.png', 650, 50, 20, 100, 10, 4, 4)
ball = Enemy('ball.png', 200, 100, 50, 50, 5, 4, 4)
win_width = 700
win_height = 500
font_1 = font.Font(None, 35)
lose_1 = font_1.render('PLAYER 2 WIN', True, (180, 0, 0))
lose_2 = font_1.render('PLAYER 1 WIN', True, (180, 0, 0))
back = transform.scale(image.load("background.jpg"), (win_width, win_height)) 
main_win = display.set_mode((win_width, win_height))
clock = time.Clock()

run = True
finish = False    
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        main_win.blit(back, (0, 0)) 
        
        platform_l.reset()
        platform_l.update_l()

        platform_r.reset()
        platform_r.update_r()
        
        ball.reset()
        ball.update()
        if ball.rect.x < 0:
            run = False
            main_win.blit(lose_1, (200, 200))
        if ball.rect.x > 650:
            run = False
            main_win.blit(lose_2, (200, 200))
        display.update()
    clock.tick(60) 
