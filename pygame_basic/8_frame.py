import pygame

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




#이벤트 루프
running = True #게임이 진행중인가?
while running:
    deltaTime = clock.tick(60)#게임 화면의 초당 프레임수를 설정 이걸 선언 하는것만으로도 fps 를 조절함. 
    # 만약 1 초에 100 을 가야한다고 쳤을때
    # 10 fps 는 속도 몇으로 가야하는가? 10 이다 한번의 움직임당 10 으로 가야 1초에 100 을 갈수있다
    # 10fps 는 1초동안 10 번을 동작한다는 것이다.
    #fps 와 상관 없이 이동 속도를 조절해야한다. 


    #2 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get(): #이게 사용자의 인풋을 이벤트에 넣어서 작동하게 해준다. pygame.event.get() 은 input 을 받아오는 것이고 event 에 저장해서 게임속 캐릭터에게 전달해준다. 
        if event.type == pygame.QUIT:# 창이 닫히는 이벤트가 발생 하면 running 을 false 로 만들어 줘서 while loop 을 탈출하고 게임을 종료 하게된다. 
            running = False
       

    # 3. 게임캐릭터 위치 정의
    
    #4. 충돌 처리
    
    
    #5. 화면에 그리기


   

    pygame.display.update()# 게임 화면을 계속 다시 그리기. 반드시 들어가야함. 

pygame.time.delay(2000)# 게임끝나고 2초 정도 기달리고 는디ㅏ.
  

#pygame 종료
pygame.quit()