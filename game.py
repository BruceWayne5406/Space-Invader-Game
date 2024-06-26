#pygame module is used for making games in python
import pygame
import random
import math
from pygame import mixer#module dealing with music inside pygame

pygame.init() #initialisng pygame module

screen=pygame.display.set_mode((600,400))# creating the screen
pygame.display.set_caption("space inavders") # setting title

mixer.music.load("background.wav")
mixer.music.play(-1)# -1 is added so that the music plays on loop

icon=pygame.image.load("spaceship-2.png")
pygame.display.set_icon(icon)

bullet_img=pygame.image.load("bullet.png")

bg=pygame.image.load("15695187_5557922.jpg")
bulletX=0
bulletY=330#bulletY is equal to playerY
bullet_state="ready"#in this state you cant see the bullet on the screen
bulletY_change= -0.3

player_img=pygame.image.load("spaceship.png")
playerX=150
playerY=330

enemy_img=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
num_of_enemies=5
score_value=0

font=pygame.font.Font('freesansbold.ttf',22)
textX=10
textY=10

over_font=pygame.font.Font("freesansbold.ttf",44)

for i in range(num_of_enemies):

     enemy_img.append(pygame.image.load("ufo-2.png"))
     enemyX.append(random.randint(0,600))
     enemyY.append(random.randint(0,150))
     enemyX_change.append(0.1)

def show_score(x,y):
     score=font.render(f"SCORE:{score_value} ",True,(255,255,255))
     screen.blit(score,(x,y))


def player():
    screen.blit(player_img,(playerX,playerY))#screen.blit draws the player image after we loaded it above



def enemy(x,y,i):
    
    screen.blit(enemy_img[i],(enemyX[i],enemyY[i]))#screen.blit draws the player image after we loaded it above

def fire_bullet(x,y):
     global bullet_state
     bullet_state="fire"#in this state bullet has been fired from the spaceship
     
     #x+16 and y+10 has been done so that the bullet appears right below the spaceship
     screen.blit(bullet_img,(x+16,y+10))

def is_collision(enemyX,enemyY,bulletX,bulletY):
     distance=math.sqrt(math.pow(bulletY-enemyY,2)+math.pow(bulletX-enemyX,2))
     if distance<25:
          return True
     else:
          return False


def game_over_text():
      over_text=font.render("GAME OVER ",True,(255,255,255))
      screen.blit(over_text,(200,250))

     


running=True


#infinite screen running loop or game loop
while running==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running==False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("left arrow is pressed")
                playerX=playerX-10
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("right arrow is pressed")
                playerX=playerX+10

           #Resetting the bullet position for shooting multiple bullets
            if bulletY<0:
                 bullet_state="ready"
                 bulletY=330
            
            if event.key==pygame.K_SPACE and bullet_state is "ready":
                 print("bullet is fired")
                 bullet_state="fire"
                 bullet_sound=mixer.Sound("laser.wav")
                 bullet_sound.play()
       


    screen.blit(bg,(0,0))   
   

    screen.fill((0,0,0))#putting r,g,b values for background ranging from 0 to 255
   #to move the player continuosly to the left we are changing the x coordinates inside the while loop
    
  
    
    
    if playerX<=0:
            playerX=0
        
    elif playerX>=569:
            playerX=569

    for i in range(num_of_enemies):
          if enemyY[i]>330:
               for j in range(num_of_enemies):
                    enemyY[j]=2000
          
               game_over_text()
               break
          
          enemyX[i]=enemyX[i]+enemyX_change[i]
          if enemyX[i]<=0:
                    enemyX_change[i]=0.1
                    enemyY[i]=enemyY[i]+4
               
          elif enemyX[i]>=600:
                    enemyX_change[i]= -0.1
                    enemyY[i]=enemyY[i]+4
    
    
          collision=is_collision(enemyX[i],enemyY[i],bulletX,bulletY)

          if collision:
               bullet_state="ready"
               bulletY=330
               score_value+=1
               print(f"you destroyed the enemy!,your score is now {score_value} ")
               enemyX[i]=random.randint(0,600)
               enemyY[i]=random.randint(0,150)
               explosion_sound=mixer.Sound("explosion.wav")
               explosion_sound.play()
       

          enemy(enemyX[i],enemyY[i],i)
          
          
          
          
    
    if bullet_state is "ready":
         bulletX=playerX
    
    if bullet_state is "fire":
         bulletY=bulletY+bulletY_change
         fire_bullet(bulletX,bulletY)
         
       

   
    player()
    show_score(textX,textY)
    pygame.display.update()

    
    




    



