import pygame
x=1
w,h=800,600
WHITE =(255, 255, 255)
c1=pygame.color.Color(str(input("color1(推薦:#6ef3ff)")))
c2=pygame.color.Color(str(input("color2(推薦:#c338ff)")))
c3=pygame.color.Color(str(input("color3(推薦:#f9ff45)")))

size=(700,500)
a=1
b=1





screen = pygame.display.set_mode(size)
pygame.display.set_caption("Munker-White illution")
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen. fill (c3)
    pygame.draw.rect(screen,c2,[0,0,350,500])
    pygame.draw.circle(screen,c1,(175,250),100)
    pygame.draw.circle(screen,c1,(525,250),100)
    
    pygame.draw.circle(screen,c3,(0,0),10)
    pygame.draw.circle(screen,c3,(40,0),10)
    pygame.draw.circle(screen,c3,(80,0),10)
    pygame.draw.circle(screen,c3,(120,0),10)
    pygame.draw.circle(screen,c3,(160,0),10)
    pygame.draw.circle(screen,c3,(200,0),10)
    pygame.draw.circle(screen,c3,(240,0),10)
    pygame.draw.circle(screen,c3,(280,0),10)
    pygame.draw.circle(screen,c3,(320,0),10)
    pygame.draw.circle(screen,c3,(0,40),10)
    pygame.draw.circle(screen,c3,(40,40),10)
    pygame.draw.circle(screen,c3,(80,40),10)
    pygame.draw.circle(screen,c3,(120,40),10)
    pygame.draw.circle(screen,c3,(160,40),10)
    pygame.draw.circle(screen,c3,(200,40),10)
    pygame.draw.circle(screen,c3,(240,40),10)
    pygame.draw.circle(screen,c3,(280,40),10)
    pygame.draw.circle(screen,c3,(320,40),10)
    pygame.draw.circle(screen,c3,(0,80),10)
    pygame.draw.circle(screen,c3,(40,80),10)
    pygame.draw.circle(screen,c3,(80,80),10)
    pygame.draw.circle(screen,c3,(120,80),10)
    pygame.draw.circle(screen,c3,(160,80),10)
    pygame.draw.circle(screen,c3,(200,80),10)
    pygame.draw.circle(screen,c3,(240,80),10)
    pygame.draw.circle(screen,c3,(280,80),10)
    pygame.draw.circle(screen,c3,(320,80),10)
    pygame.draw.circle(screen,c3,(0,120),10)
    pygame.draw.circle(screen,c3,(40,120),10)
    pygame.draw.circle(screen,c3,(80,120),10)
    pygame.draw.circle(screen,c3,(120,120),10)
    pygame.draw.circle(screen,c3,(160,120),10)
    pygame.draw.circle(screen,c3,(200,120),10)
    pygame.draw.circle(screen,c3,(240,120),10)
    pygame.draw.circle(screen,c3,(280,120),10)
    pygame.draw.circle(screen,c3,(320,120),10)
    pygame.draw.circle(screen,c3,(0,160),10)
    pygame.draw.circle(screen,c3,(40,160),10)
    pygame.draw.circle(screen,c3,(80,160),10)
    pygame.draw.circle(screen,c3,(120,160),10)
    pygame.draw.circle(screen,c3,(160,160),10)
    pygame.draw.circle(screen,c3,(200,160),10)
    pygame.draw.circle(screen,c3,(240,160),10)
    pygame.draw.circle(screen,c3,(280,160),10)
    pygame.draw.circle(screen,c3,(320,160),10)
    pygame.draw.circle(screen,c3,(0,200),10)
    pygame.draw.circle(screen,c3,(40,200),10)
    pygame.draw.circle(screen,c3,(80,200),10)
    pygame.draw.circle(screen,c3,(120,200),10)
    pygame.draw.circle(screen,c3,(160,200),10)
    pygame.draw.circle(screen,c3,(200,200),10)
    pygame.draw.circle(screen,c3,(240,200),10)
    pygame.draw.circle(screen,c3,(280,200),10)
    pygame.draw.circle(screen,c3,(320,200),10)
    pygame.draw.circle(screen,c3,(0,240),10)
    pygame.draw.circle(screen,c3,(40,240),10)
    pygame.draw.circle(screen,c3,(80,240),10)
    pygame.draw.circle(screen,c3,(120,240),10)
    pygame.draw.circle(screen,c3,(160,240),10)
    pygame.draw.circle(screen,c3,(200,240),10)
    pygame.draw.circle(screen,c3,(240,240),10)
    pygame.draw.circle(screen,c3,(280,240),10)
    pygame.draw.circle(screen,c3,(320,240),10)
    pygame.draw.circle(screen,c3,(0,280),10)
    pygame.draw.circle(screen,c3,(40,280),10)
    pygame.draw.circle(screen,c3,(80,280),10)
    pygame.draw.circle(screen,c3,(120,280),10)
    pygame.draw.circle(screen,c3,(160,280),10)
    pygame.draw.circle(screen,c3,(200,280),10)
    pygame.draw.circle(screen,c3,(240,280),10)
    pygame.draw.circle(screen,c3,(280,280),10)
    pygame.draw.circle(screen,c3,(320,280),10)
    pygame.draw.circle(screen,c3,(0,320),10)
    pygame.draw.circle(screen,c3,(40,320),10)
    pygame.draw.circle(screen,c3,(80,320),10)
    pygame.draw.circle(screen,c3,(120,320),10)
    pygame.draw.circle(screen,c3,(160,320),10)
    pygame.draw.circle(screen,c3,(200,320),10)
    pygame.draw.circle(screen,c3,(240,320),10)
    pygame.draw.circle(screen,c3,(280,320),10)
    pygame.draw.circle(screen,c3,(320,320),10)
    pygame.draw.circle(screen,c3,(0,360),10)
    pygame.draw.circle(screen,c3,(40,360),10)
    pygame.draw.circle(screen,c3,(80,360),10)
    pygame.draw.circle(screen,c3,(120,360),10)
    pygame.draw.circle(screen,c3,(160,360),10)
    pygame.draw.circle(screen,c3,(200,360),10)
    pygame.draw.circle(screen,c3,(240,360),10)
    pygame.draw.circle(screen,c3,(280,360),10)
    pygame.draw.circle(screen,c3,(320,360),10)
    pygame.draw.circle(screen,c3,(0,400),10)
    pygame.draw.circle(screen,c3,(40,400),10)
    pygame.draw.circle(screen,c3,(80,400),10)
    pygame.draw.circle(screen,c3,(120,400),10)
    pygame.draw.circle(screen,c3,(160,400),10)
    pygame.draw.circle(screen,c3,(200,400),10)
    pygame.draw.circle(screen,c3,(240,400),10)
    pygame.draw.circle(screen,c3,(280,400),10)
    pygame.draw.circle(screen,c3,(320,400),10)
    pygame.draw.circle(screen,c3,(0,440),10)
    pygame.draw.circle(screen,c3,(40,440),10)
    pygame.draw.circle(screen,c3,(80,440),10)
    pygame.draw.circle(screen,c3,(120,440),10)
    pygame.draw.circle(screen,c3,(160,440),10)
    pygame.draw.circle(screen,c3,(200,440),10)
    pygame.draw.circle(screen,c3,(240,440),10)
    pygame.draw.circle(screen,c3,(280,440),10)
    pygame.draw.circle(screen,c3,(320,440),10)
    pygame.draw.circle(screen,c2,(360,0),10)
    pygame.draw.circle(screen,c2,(400,0),10)
    pygame.draw.circle(screen,c2,(440,0),10)
    pygame.draw.circle(screen,c2,(480,0),10)
    pygame.draw.circle(screen,c2,(520,0),10)
    pygame.draw.circle(screen,c2,(560,0),10)
    pygame.draw.circle(screen,c2,(600,0),10)
    pygame.draw.circle(screen,c2,(640,0),10)
    pygame.draw.circle(screen,c2,(680,0),10)
    pygame.draw.circle(screen,c2,(360,40),10)
    pygame.draw.circle(screen,c2,(400,40),10)
    pygame.draw.circle(screen,c2,(440,40),10)
    pygame.draw.circle(screen,c2,(480,40),10)
    pygame.draw.circle(screen,c2,(520,40),10)
    pygame.draw.circle(screen,c2,(560,40),10)
    pygame.draw.circle(screen,c2,(600,40),10)
    pygame.draw.circle(screen,c2,(640,40),10)
    pygame.draw.circle(screen,c2,(680,40),10)
    pygame.draw.circle(screen,c2,(360,80),10)
    pygame.draw.circle(screen,c2,(400,80),10)
    pygame.draw.circle(screen,c2,(440,80),10)
    pygame.draw.circle(screen,c2,(480,80),10)
    pygame.draw.circle(screen,c2,(520,80),10)
    pygame.draw.circle(screen,c2,(560,80),10)
    pygame.draw.circle(screen,c2,(600,80),10)
    pygame.draw.circle(screen,c2,(640,80),10)
    pygame.draw.circle(screen,c2,(680,80),10)
    pygame.draw.circle(screen,c2,(360,120),10)
    pygame.draw.circle(screen,c2,(400,120),10)
    pygame.draw.circle(screen,c2,(440,120),10)
    pygame.draw.circle(screen,c2,(480,120),10)
    pygame.draw.circle(screen,c2,(520,120),10)
    pygame.draw.circle(screen,c2,(560,120),10)
    pygame.draw.circle(screen,c2,(600,120),10)
    pygame.draw.circle(screen,c2,(640,120),10)
    pygame.draw.circle(screen,c2,(680,120),10)
    pygame.draw.circle(screen,c2,(360,160),10)
    pygame.draw.circle(screen,c2,(400,160),10)
    pygame.draw.circle(screen,c2,(440,160),10)
    pygame.draw.circle(screen,c2,(480,160),10)
    pygame.draw.circle(screen,c2,(520,160),10)
    pygame.draw.circle(screen,c2,(560,160),10)
    pygame.draw.circle(screen,c2,(600,160),10)
    pygame.draw.circle(screen,c2,(640,160),10)
    pygame.draw.circle(screen,c2,(680,160),10)
    pygame.draw.circle(screen,c2,(360,200),10)
    pygame.draw.circle(screen,c2,(400,200),10)
    pygame.draw.circle(screen,c2,(440,200),10)
    pygame.draw.circle(screen,c2,(480,200),10)
    pygame.draw.circle(screen,c2,(520,200),10)
    pygame.draw.circle(screen,c2,(560,200),10)
    pygame.draw.circle(screen,c2,(600,200),10)
    pygame.draw.circle(screen,c2,(640,200),10)
    pygame.draw.circle(screen,c2,(680,200),10)
    pygame.draw.circle(screen,c2,(360,240),10)
    pygame.draw.circle(screen,c2,(400,240),10)
    pygame.draw.circle(screen,c2,(440,240),10)
    pygame.draw.circle(screen,c2,(480,240),10)
    pygame.draw.circle(screen,c2,(520,240),10)
    pygame.draw.circle(screen,c2,(560,240),10)
    pygame.draw.circle(screen,c2,(600,240),10)
    pygame.draw.circle(screen,c2,(640,240),10)
    pygame.draw.circle(screen,c2,(680,240),10)
    pygame.draw.circle(screen,c2,(360,240),10)
    pygame.draw.circle(screen,c2,(400,240),10)
    pygame.draw.circle(screen,c2,(440,240),10)
    pygame.draw.circle(screen,c2,(480,240),10)
    pygame.draw.circle(screen,c2,(520,240),10)
    pygame.draw.circle(screen,c2,(560,240),10)
    pygame.draw.circle(screen,c2,(600,240),10)
    pygame.draw.circle(screen,c2,(640,240),10)
    pygame.draw.circle(screen,c2,(680,240),10)
    pygame.draw.circle(screen,c2,(360,280),10)
    pygame.draw.circle(screen,c2,(400,280),10)
    pygame.draw.circle(screen,c2,(440,280),10)
    pygame.draw.circle(screen,c2,(480,280),10)
    pygame.draw.circle(screen,c2,(520,280),10)
    pygame.draw.circle(screen,c2,(560,280),10)
    pygame.draw.circle(screen,c2,(600,280),10)
    pygame.draw.circle(screen,c2,(640,280),10)
    pygame.draw.circle(screen,c2,(680,280),10)     
    pygame.draw.circle(screen,c2,(360,320),10)
    pygame.draw.circle(screen,c2,(400,320),10)
    pygame.draw.circle(screen,c2,(440,320),10)
    pygame.draw.circle(screen,c2,(480,320),10)
    pygame.draw.circle(screen,c2,(520,320),10)
    pygame.draw.circle(screen,c2,(560,320),10)
    pygame.draw.circle(screen,c2,(600,320),10)
    pygame.draw.circle(screen,c2,(640,320),10)
    pygame.draw.circle(screen,c2,(680,320),10)
    pygame.draw.circle(screen,c2,(360,360),10)
    pygame.draw.circle(screen,c2,(400,360),10)
    pygame.draw.circle(screen,c2,(440,360),10)
    pygame.draw.circle(screen,c2,(480,360),10)
    pygame.draw.circle(screen,c2,(520,360),10)
    pygame.draw.circle(screen,c2,(560,360),10)
    pygame.draw.circle(screen,c2,(600,360),10)
    pygame.draw.circle(screen,c2,(640,360),10)
    pygame.draw.circle(screen,c2,(680,360),10)
    pygame.draw.circle(screen,c2,(360,400),10)
    pygame.draw.circle(screen,c2,(400,400),10)
    pygame.draw.circle(screen,c2,(440,400),10)
    pygame.draw.circle(screen,c2,(480,400),10)
    pygame.draw.circle(screen,c2,(520,400),10)
    pygame.draw.circle(screen,c2,(560,400),10)
    pygame.draw.circle(screen,c2,(600,400),10)
    pygame.draw.circle(screen,c2,(640,400),10)
    pygame.draw.circle(screen,c2,(680,400),10)
    pygame.draw.circle(screen,c2,(360,440),10)
    pygame.draw.circle(screen,c2,(400,440),10)
    pygame.draw.circle(screen,c2,(440,440),10)
    pygame.draw.circle(screen,c2,(480,440),10)
    pygame.draw.circle(screen,c2,(520,440),10)
    pygame.draw.circle(screen,c2,(560,440),10)
    pygame.draw.circle(screen,c2,(600,440),10)
    pygame.draw.circle(screen,c2,(640,440),10)
    pygame.draw.circle(screen,c2,(680,440),10)









































































































































































































        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()