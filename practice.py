# scores = {"Math":50,"Englis":70,"Code":100}

# for subjects,grade in scores.items():
  
#     print(subjects.ljust(8),str(grade).rjust(4),sep=":") # ljust 왼쪽정렬 rjust 오른쪽 정렬 sep = 컴마 로 갈른곳마다 뭐가들어갈까 정렬뒤의 숫자는 총 몇칸중에 좌/우 로 정렬할까.

for i in range(1,21):
    print("대기번호 : "+ str(i).zfill(3))# zfill 은 zerofill 이다 그옆에 숫자는 몇자리인지 물어보는거다. 숫자가 없는 빈곳에는 zero 로 채워준다. 