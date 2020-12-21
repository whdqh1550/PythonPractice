import pygame


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


#배경 이미지 불러오기
background = pygame.image.load("/Users/jongboim/Desktop/PythonPractice/pygame_basic/background.png")#배경화면 설정.

#스프라이트 불러오기(캐릭터 불러오기)

character = pygame.image.load("/Users/jongboim/Desktop/PythonPractice/pygame_basic/chracter.png")#캐릭터 이미지 설정
character_size = character.get_rect().size #이미지의 크기를 사각형 형태로 구해옴. 여기서 캐릭터는 사각형 이기때문에 그 사각형 의 가로 세로 길이를 가져온다.
character_width = character_size[0]# 이거는 위에 방법으로 가로 세로를 길이를 저장했는데 그중에 리스트 첫번째에 가로가 저장돼었기에 가로 길이를 캐릭터의 넓이로 가져온다
character_height = character_size[1]# 이거는 위의 character_size 의 세로 길이를 가져온다 그 세로길이는 리스트중 [1] 번칸에 있다 [0]번은 가로길이다.
character_x_pos = screen_width/2 -(character_width/2) # 가로 화면의 절반 크기에 해당하는 값. 그래서 화면 가로의 가운데로 온다.
character_y_pos = screen_height - character_height

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.3


#이벤트 루프
running = True #게임이 진행중인가?
while running:
    deltaTime = clock.tick(30)#게임 화면의 초당 프레임수를 설정 이걸 선언 하는것만으로도 fps 를 조절함. 
    # 만약 1 초에 100 을 가야한다고 쳤을때
    # 10 fps 는 속도 몇으로 가야하는가? 10 이다 한번의 움직임당 10 으로 가야 1초에 100 을 갈수있다
    # 10fps 는 1초동안 10 번을 동작한다는 것이다.
    #fps 와 상관 없이 이동 속도를 조절해야한다. 


    print("fps: " + str(clock.get_fps()))
    for event in pygame.event.get(): #이게 사용자의 인풋을 이벤트에 넣어서 작동하게 해준다. pygame.event.get() 은 input 을 받아오는 것이고 event 에 저장해서 게임속 캐릭터에게 전달해준다. 
        if event.type == pygame.QUIT:# 창이 닫히는 이벤트가 발생 하면 running 을 false 로 만들어 줘서 while loop 을 탈출하고 게임을 종료 하게된다. 
            running = False
        if event.type == pygame.KEYDOWN:# 어느 키보드든 눌려 있을경우, 키가 눌렸을경우
            if event.key == pygame.K_LEFT:
                to_x-= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        elif event.type == pygame.KEYUP: # 키보드가 눌렸다가 때어지는 순간.
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:#오른쪽이나 왼쪽 방향키가 떼지는 순간 가는 힘이 ㅅ0
                to_x = 0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                to_y = 0
        


    character_x_pos += to_x*deltaTime# 이렇게 delta Time 값을 곱해줌으로써 프레임에 따라 속도의 변화는 없다. 
    character_y_pos +=to_y*deltaTime

    if character_x_pos <= 0 :
        character_x_pos = 0
    elif character_x_pos >= screen_width- character_width:
        character_x_pos = screen_width - character_width
    
    if character_y_pos <= 0 :
        character_y_pos = 0
    elif character_y_pos >= screen_height - character_height:
        character_y_pos = screen_height - character_height

    


    #screen.fill((0,0,255))# RGB 값의로 해당됨 레드 0 그린 0 블루 맥스인 255 로 블루만 꽉참. 
    screen.blit(background,(0,0))#배경 그리기 # 게임이 완성되면 이 부분이 event loop 위로 올라 갈수 있는지 확인하기 
    
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 생성 

    pygame.display.update()# 게임 화면을 계속 다시 그리기. 반드시 들어가야함. 
#pygame 종료
pygame.quit()