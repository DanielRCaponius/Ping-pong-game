from pygame import *

'''mixer.init()'''
font.init()

font = font.Font(None,35)
p1win = font.render('Player 1 wins!',True,(60,255,30))
p2win = font.render('Player 2 wins! ',True,(255,20,10))

xres = 700
yres = 500

clock = time.Clock()
FPS = 60

window = display.set_mode((xres,yres))
window.fill((255,242,212))

game = True
win = False

class GameSprite(sprite.Sprite):
    def __init__(self,png,sx,sy,x,y,v):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(png),(sx,sy))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.v = v

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class player(GameSprite):
    def __init__(self,png,sx,sy,x,y,v,nplayer):
        super().__init__()
        self.nplayer = nplayer
        
    
    def controls(self):
        keys_pressed = key.get_pressed()

        match self.nplayer:
            case 1:
                if keys_pressed[K_d]:
                    if self.rect.x > 620:
                        self.rect.x = 620
                    else:
                        self.rect.x += self.v

                if keys_pressed[K_a]:
                    if self.rect.x < 0:
                        self.rect.x == 0
                    else:
                        self.rect.x -= self.v
            case 2:
                if keys_pressed[K_d]:
                    if self.rect.x > 620:
                        self.rect.x = 620
                    else:
                        self.rect.x += self.v

                if keys_pressed[K_a]:
                    if self.rect.x < 0:
                        self.rect.x == 0
                    else:
                        self.rect.x -= self.v

class ball(GameSprite):
    def update(self):
        self.rect.y += self.v
        self.rect.x += self.v
        
        match self.rect.y:
            case 0, yres:
                self.rect.y *= -1
        
        match self.rect.x:
            case -20:
                win = True
                window.blit
                
        

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if win != True:
    
        display.update()
  
        

    display.update()
    clock.tick(FPS)