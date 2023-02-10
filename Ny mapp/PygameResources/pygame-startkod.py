import pygame
from teknik1grafik import GrafikElement

#def hoppa():
#    print("Nu körs funktionen hoppa")

#def sova():
#    print("Nu körs funktionen sova")

#Startar pygame
pygame.init()

#Skapar en displayruta och en klocka, samt lagrar skärmens mått
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
screen_width, screen_height = screen.get_size()
#g1 = GrafikElement("/bilder/zohan.jpg", (0,100), "Zohan", hoppa)
#g2 = GrafikElement("/bilder/hansel.jpg", (300,100), "Hansel", sova)
#bilder = [g1, g2]

#Här är programmets while-loop som körs tills dess att displayrutan stängs. Loopens tre första rader har hand om avstängningen.
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Terminating program")
            open = False  

#        Om en musklick skett, undersöks här om klicket är på någon av dina bilder.
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            for x in bilder:
#                if(x.rect.collidepoint(pygame.mouse.get_pos()) == 1):
#                    x.pushFunction()
   
    #Displayrutan uppdateras med allt det som ritats dit sedan förra uppdateringen
#    screen.blit(g1.image, g1.pos)
#    screen.blit(g2.image, g2.pos)
    pygame.display.update()
    clock.tick(10)

#Programmets avslutas korrekt så att det inte belastar datorns minne
pygame.quit()
quit()