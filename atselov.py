from pygame import *
from random import randint

win_width= 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('bogatstvo.py')
background = transform.scale(image.load('phon.jpg'), (win_width, win_height))


font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
   
lost = 0
score = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.kill()
            lost = lost+1
            self = Enemy('bomb.png', randint(80, win_width - 60), -40, randint(1,5), 90, 65)
            enemys.add(self)
        
class Money(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
           self.rect.x = randint(60, win_width -60)
           self.rect.y = 0
           
player=Player('basket.png', 5, win_height - 100,  10, 65, 65)




enemys = sprite.Group()
for i in range(1,3):
    enemy = Enemy('bomb.png', randint(80, win_width - 60), -40, randint(1,5), 90, 65)
    enemys.add(enemy)

moneys = sprite.Group()
for i in range(1,8):
    money = Money('egg.png', randint(80, win_width - 60), -40, randint(1,5), 90, 65)
    
    moneys.add(money)

health = 3

finish = False
run = True
clock = time.Clock()
FPS = 60 
font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 36)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish: 
        window.blit(background, (0, 0))

        player.update()
        player.reset()
        enemys.update()
        enemys.draw(window)
        moneys.update()
        moneys.draw(window)

        
            
        if sprite.spritecollide(player, enemys, False) or lost>=10:
            finish = True
            window.blit(lose, (200, 200))
        if score >= 20:
            finish = True
            window.blit(win, (200, 200))
        if sprite.spritecollide(player, moneys, True):
            score+=1
            money = Money('egg.png', randint(80, win_width - 60), -40, randint(1,5), 90, 65)
            moneys.add(money)

        if health == 0:
            finish = True
            window.blit(lose, (200, 200))
            
        
       



        text_score = font2.render('Счётчик:' + str(score), 2, (255, 55, 255))
        window.blit(text_score, (10, 20))
        text_lose = font1.render('Пропущено:' + str(lost), 1, (255, 55, 255))
        window.blit(text_lose, (10, 50))
   
        

   
        display.update()

    clock.tick(FPS)
