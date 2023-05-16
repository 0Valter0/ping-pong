from pygame import *
pygame.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_weight, player_hight, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_weight, player_hight))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.weight = player_weight
        self.hight = player_hight 
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < 620:
            self.rect.x += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < 620:
            self.rect.x += self.speed

class Enemy(GameSprite):
    if self.colliderect(platform_l.rect):
        speed_x *= -1
    if self.colliderect(platform_r.rect):
        speed_x *= -1   
    if self.rect.y > 450 or self.rect.y < 0:
        speed_x *= -1
    if self.rect.y < 0:
        speed_y *= -1  

platform_l = Player('platform.png', 50, 50, 20, 100, 10)
platform_r = Player('platform.png', 50, 50, 20, 100, 10)
ball = Enemy('ball.png', 350, 250, 50, 50, 5)
win_width = 700
win_height = 500
back = transform.scale(image.load("background.jpeg"), (win_width, win_height)) 
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
        platform_l.update_l

        platform_r.reset()
        platform_r.update_r
        
        ball.reset()
        
        display.update()
    clock.tick(60)       
