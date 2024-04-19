def Na():
    
    print("/////")
    return 1
    
import numpy as np 
a = np.array([1,2,3,4,5])
print (a*2)   # 1번


a = np.array([1,2,'A'])
print(a)    # 2번 
Na()# 하나만 문자여도 전부다 문자로 출력됨

a = np.array([1,2,3.14])
print(a)    # 3번 
Na() # 3.14가 소수라서 나머지도 소수로 나옴

# a = np.array([[1,2,3],[4,5,6]])
# print(a.shape) # 몇 행 몇 열인지 알려주는 메소드
# Na()

a = np.arange(0, 0.8, 0.2) # 4번
print(a) # 시작값 끝값 증감값 , 증감값은 미만 
Na()

a = np.arange(3)  # 5 
print(a) # 시작 , 끝 , 증감 0 ~ 3 ~ 1 , 끝값은 미만 
Na()

# a = np.tile('A',3)
# print(a) # A를 3번 출력해라는 뜻 , 이건 과제아님 
# Na()

a = np.tile(7,3) # 6
print(a) # 7을 3번 출력함
Na()

a = np.full(7,3) # 7 
print(a) # 이건 tile이랑 다르게 3을 7번 출력한다는 뜻
Na()

a = np.zeros([2,3]) # 8
print(a) # 0을 2행 3열로 출력한다는 뜻 , 프로그래머 입장에선 1행 2열 
Na()

# a = np.array([1,2,3,4,5])
# print(a[0]) # 과제아님 , 0번쨰 객체 출력하라는 뜻뜻
# Na()

print(a[1:3]) # 1 번째 객체 ~ 3 번쨰 객체 미만까지 출력 
Na() # 9

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[0][3]) # 0행 2열 출력하라는 뜻 프로그래머 입장  , 질문 : a[0][3] = a[0,3] ?? 
Na() # 10

print(a[1, 2:4]) # 프로그래머 입장에서 1행 에서 2열 , 3열 출력하라는 뜻
Na() # 10

# DateFrame : array는 2차원 가능하지만 데이터프레임을 쓰는 이유는 array는 다른 자료형을 같이 못씀 , 하지만 DateFrame는 가능

# 주의 : col 명에 작은 따옴표 꼭 해야함 , 중괄호로 감싸기 , 컬럼 끝나면 반점 붙이기 , 딕셔너리 처럼 컬럼과 값 사이에 : 쓰기

# import pandas as pd 

# file = pd.read_csv("C:/Users/kiiti/Downloads/sample1.csv")
# print(file)

