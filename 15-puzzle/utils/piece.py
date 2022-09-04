from .settings import *

class piece:
    def __init__(self,x,y,number,newX,newY):
        self.x = x
        self.y = y
        self.number = number
        self.newX = newX
        self.newY = newY
    
    def show(self,screen,x,y,number):
        if number == 16:
            pygame.draw.rect(screen,WHITE,(x,y,PIXEL_SIZE,PIXEL_SIZE))
        else:
            pygame.draw.rect(screen,WHITE,(x,y,PIXEL_SIZE,PIXEL_SIZE))
            # font = get_font(50)
            # txt = font.render(str(number),True,BLACK)
            # screen.blit(txt,(x+10,y+10))
  

