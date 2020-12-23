import pygame
import random
#################################

pygame.init()# 초기화 반드시 필요함.


#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")#게임 이름

#FPS
clock = pygame.time.Clock()
#################################

#1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트,속도, 시간 등)

background = pygame.image.load("/Users/jongboim/Desktop/PythonPractice/pygame_basic/background.png")


character = pygame.image.load("/Users/jongboim/Desktop/PythonPractice/pygame_basic/chracter.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

enemy = pygame.image.load("/Users/jongboim/Desktop/PythonPractice/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0,480-enemy_width)
enemy_y_pos = 0

font = pygame.font.Font(None,40)

speed = 0.3

to_x = 0
to_y = 0

start_time = pygame.time.get_ticks()

score = 0




#이벤트 루프
running = True #게임이 진행중인가?
while running:
    deltaTime = clock.tick(30)#게임 화면의 초당 프레임수를 설정 이걸 선언 하는것만으로도 fps 를 조절함. 
    # 만약 1 초에 100 을 가야한다고 쳤을때
    # 10 fps 는 속도 몇으로 가야하는가? 10 이다 한번의 움직임당 10 으로 가야 1초에 100 을 갈수있다
    # 10fps 는 1초동안 10 번을 동작한다는 것이다.
    #fps 와 상관 없이 이동 속도를 조절해야한다. 


    #2 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get(): #이게 사용자의 인풋을 이벤트에 넣어서 작동하게 해준다. pygame.event.get() 은 input 을 받아오는 것이고 event 에 저장해서 게임속 캐릭터에게 전달해준다. 
        if event.type == pygame.QUIT:# 창이 닫히는 이벤트가 발생 하면 running 을 false 로 만들어 줘서 while loop 을 탈출하고 게임을 종료 하게된다. 
            running = False
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x-= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
        


    # 3. 게임캐릭터 위치 정의
    


    fallingspeed = random.randrange(1,10)
    enemy_y_pos += fallingspeed
    character_x_pos += to_x*deltaTime

    if enemy_y_pos >= screen_height:
        enemy_y_pos = 0 - enemy_height
        enemy_x_pos = random.randrange(0,480-enemy_width)
        score +=1
    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos >= (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    
    #4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("game over")
        running = False
    
    
    #5. 화면에 그리기

    disscore = font.render(str(score), True,(255,255,255))

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    screen.blit(disscore,(10,10))
   

    pygame.display.update()# 게임 화면을 계속 다시 그리기. 반드시 들어가야함. 


  

#pygame 종료
pygame.quit()