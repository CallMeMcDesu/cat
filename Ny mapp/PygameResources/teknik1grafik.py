import pygame, os

class GrafikElement(pygame.sprite.Sprite):
    def __init__(self, link, pos, name = None, pushFunction = None, info = None):
        self.name = name
        self.link = link
        self.pos = pos  
        self.pushFunction = pushFunction  
        self.info = info    
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(os.path.dirname(__file__) + link)      
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def setNewPos(self, newPos):
        self.pos = newPos
        self.rect.x = newPos[0]
        self.rect.y = newPos[1]     

    def scale(self, procentIn):
        procent = procentIn/100
        self.image = pygame.image.load(os.path.dirname(__file__) + self.link)             
        self.image = pygame.transform.smoothscale(self.image, (self.rect.width * procent, self.rect.height * procent))  
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]