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
        super().__init__(png,sx,sy,x,y,v)
        self.nplayer = nplayer
        
    def controls(self):
        keys_pressed = key.get_pressed()

        match self.nplayer:
            case 1:
                if keys_pressed[K_w]:
                    if self.rect.y < 0:
                        self.rect.y = 0
                    else:
                        self.rect.y -= self.v

                if keys_pressed[K_s]:
                    if self.rect.y > 450:
                        self.rect.y = 450
                    else:
                        self.rect.y += self.v
                    
            case 2:
                if keys_pressed[K_DOWN]:
                    if self.rect.y > 450:
                        self.rect.y = 450
                    else:
                        self.rect.y += self.v
                               
                if keys_pressed[K_UP]:
                    if self.rect.y < 0:
                        self.rect.y = 0
                    else:
                        self.rect.y -= self.v

class ball(GameSprite):
    def __init__(self,png,sx,sy,x,y,v,v_x,v_y):
        super().__init__(png,sx,sy,x,y,v)
        self.v_x = v_x
        self.v_y = v_y
    
    def update(self):
        if self.rect.y < 0 or self.rect.y > 480:
            self.v_y *= -1
            
        if self.rect.x < -20 or self.rect.x > 700:
            self.v_x *= -1
        
        self.rect.x += self.v_x
        self.rect.y += self.v_y
                

    '''    win = True
        window.blit(p1win,(xres/2,yres/2))
        case 720:
        win = True
        window.blit(p2win,(xres/2,yres/2))'''
                
p1 = player('p1.png',20,50,20,250,5,1)    
p2 = player('p2.png',20,50,660,250,5,2)

b = ball('b.png',25,25,350,250,0,3,3)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if win != True:
        
        window.fill((255,242,212))
        
        if sprite.collide_rect(p1,b) or sprite.collide_rect(p2,b):
            b.v_x *= -1
        
        p1.controls()
        p2.controls()
        b.update()
        
        p1.reset()
        p2.reset()
        b.reset()
        
        display.update()
  
    display.update()
    clock.tick(FPS)