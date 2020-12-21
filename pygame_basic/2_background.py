import pygame


pygame.init()# 초기화 반드시 필요함.


#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")#게임 이름

#배경 이미지 불러오기
background = pygame.image.load("/Users/jongboim/Desktop/PythonPractice/pygame_basic/background.png")#배경화면 설정.
#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #이게 사용자의 인풋을 이벤트에 넣어서 작동하게 해준다. pygame.event.get() 은 input 을 받아오는 것이고 event 에 저장해서 게임속 캐릭터에게 전달해준다. 
        if event.type == pygame.QUIT:# 창이 닫히는 이벤트가 발생 하면 running 을 false 로 만들어 줘서 while loop 을 탈출하고 게임을 종료 하게된다. 
            running = False

    #screen.fill((0,0,255))# RGB 값의로 해당됨 레드 0 그린 0 블루 맥스인 255 로 블루만 꽉참. 
    screen.blit(background,(0,0))#배경 그리기 # 게임이 완성되면 이 부분이 event loop 위로 올라 갈수 있는지 확인하기 
    pygame.display.update()# 게임 화면을 계속 다시 그리기. 반드시 들어가야함. 
#pygame 종료
pygame.quit()