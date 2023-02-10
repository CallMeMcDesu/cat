import pygame
from teknik1grafik import GrafikElement
import random
#def hoppa():
#    print("Nu körs funktionen hoppa")
pygame.mixer.init()
pygame.font.init()

#def sova():
#    print("Nu körs funktionen sova")
nysiffra = 0
siffra = 0
def nummer():
    global nysiffra
    global siffra
    nysiffra = nysiffra + 1
    return nysiffra

typsnitt1 = pygame.font.Font("freesansbold.ttf", 48)
infoTextruta = typsnitt1.render(str(nysiffra),True, (255,0,0))     

def test():
    g1.setNewPos((random.randint(1, 900), random.randint(1, 900)))
    pygame.mixer.Channel(0).play(s1)
    
def test1():
    g2.setNewPos((random.randint(1, 900), random.randint(1, 900)))
    pygame.mixer.Channel(2).play(s3)
def test2():
    g3.setNewPos((random.randint(1, 900), random.randint(1, 900)))
    pygame.mixer.Channel(1).play(s2)
def katt():
    g4.setNewPos((random.randint(1, 900), random.randint(1, 900)))
    pygame.mixer.Channel(5).play(s5)
def musikpå():
    pygame.mixer.Channel(4).play(s4)
def musikav():
    pygame.mixer.Channel(4).stop()
#Startar pygame
pygame.init()
#Skapar en displayruta och en klocka, samt lagrar skärmens mått
screen = pygame.display.set_mode((1920,1080))
clock = pygame.time.Clock()
screen_width, screen_height = screen.get_size()
s1 = pygame.mixer.Sound("sfx/Unreal Tournament Voice SFX/8.mp3")
s2 = pygame.mixer.Sound("sfx/Unreal Tournament Voice SFX/1.mp3")
s3 = pygame.mixer.Sound("sfx/Unreal Tournament Voice SFX/3.mp3")
s4 = pygame.mixer.Sound("musik/R-Type Remix.mp3")
s5 = pygame.mixer.Sound("sfx/meow.mp3")
g1 = GrafikElement("/bilder/zohan.jpg", (0,100), "Zohan", test)
g2 = GrafikElement("/bilder/hansel.jpg", (300,100), "Hansel", test1)
g3 = GrafikElement("/bilder/dodge.jpg", (600,100),"Dodge", test2)
g4 = GrafikElement("/bilder/Katt.jpg", (700, 100),"Katt", katt  )
knapp1 = GrafikElement("/bilder/knapp.jpg", (600, 600), "knapp", musikpå)
knapp2 = GrafikElement("/bilder/knapp.jpg", (500, 600), "knapp", musikav)
bilder = [g1, g2, g3, knapp1, knapp2, g4]
#pygame.mixer.Channel(4).play(s4)
knapp1.scale(20)
knapp2.scale(20)
g1.scale(50)
g2.scale(50)
g3.scale(50)
#g4.scale(10)
#g4 = pygame.transform.rotate(g4, 45)
#Här är programmets while-loop som körs tills dess att displayrutan stängs. Loopens tre första rader har hand om avstängningen.
while open:
    screen.fill((0,0,0))
    infoTextruta = typsnitt1.render(str(nysiffra),True, (255,0,0)) 
    screen.blit(g1.image, g1.pos)
    screen.blit(g2.image, g2.pos)
    screen.blit(g3.image, g3.pos)
    screen.blit(knapp1.image, knapp1.pos)
    screen.blit(knapp2.image, knapp2.pos)
    screen.blit(infoTextruta, (200,600))
    screen.blit(g4.image, g4.pos)
     
    #g1.scale(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Terminating program")
            open = False  
      #  elif event.type == pygame.MOUSEBUTTONDOWN:
      #      test()

#        Om en musklick skett, undersöks här om klicket är på någon av dina bilder.
        elif event.type == pygame.MOUSEBUTTONDOWN:
             for x in bilder:
                 if(x.rect.collidepoint(pygame.mouse.get_pos()) == 1):
                     x.pushFunction()
                     nummer()
                     pygame.display.flip()
        #elif event.type == pygame.MOUSEBUTTONDOWN:
        #    nummer()
   
    #Displayrutan uppdateras med allt det som ritats dit sedan förra uppdateringen
   # screen.fill(255,100,1)
    pygame.display.update()
    clock.tick(10)

#Programmets avslutas korrekt så att det inte belastar datorns minne
pygame.quit()
quit()