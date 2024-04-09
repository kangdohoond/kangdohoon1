import pandas as pd
import numpy as np

# 대푯값 : 데이터의 중심위치를 나타내는 값이 그 데이터를 대표한다고 보는 것, ex ) 평균, 중앙값, 최빈값
# 산포도 : 데이터들이 흩어진 정도, ex) 분산, 표준편차, 사분위편차
# 이 두개 외워야함 중요 

# 평균의 단점 : 극단적인 값이 평균이 왜곡 될 수도 있음
# 시험 중앙값 중요 / 메소드 안 쓰고 구하기
# 중앙값 : 중간에 있는 사람 -> a = 1,2,3,4,5 - > (a.size // 2) 홀수일 때 , 메소드 : median, 시험 median 안 쓰고 중앙값 구하기
# 짝수일 떄 : 
# 중앙값은 평균과는 달리 극단적인 값에 영향을 받진 않지만 가운데 위치하는 한 개 또는 두 개의 값으로만 
# 계산된다는 단점도 있음

# 최빈값 : 가장 많이 나온 값 ex ) 1 3 4 3 2 3 5 -> 최빈값 : 3
# 최빈값을 구할 때 넘파이 말고 scipt.stats 써야 편함 메소드 있어서

# from scipy import stats

# x = pd.read_excel("C:/Users/kiiti/Downloads/중학생_남자_몸무게/중학생_남자_몸무게.xlsx", header = None) # 헤더 넌 : 
# print(f"평균 : {np.mean(x)} \n")
# print(f"중앙값 : {np.median(x)} \n")
# print(f"최빈값 : {stats.mode(x)}\n") # 46이 40번 나왔다는 뜻
# print(f"{np.average(x)}\n")   # mean 말고 이것도 평균 구하는 거임 가중치도 줄 수 있다고 함 (가중치 안 주면 mean이랑 같음)

# print("\n")

# a = np.array([[1,2], [3,4]])
# print(f"평균 : {a.mean()}")
# print(f"axis = 0 일때 평균 : {np.mean(a, axis=0)}") # 행 많아지는 거
# print(f"axis = 1 일때 평균 : {np.mean(a, axis=1)}")

# print("\n")

# w = np.array([[0.1, 0.2], [0.3,0.4]])
# print(f"aver : {np.average(a)}")
# print(f"가중평균 : {np.average(a, weights = w)}")

# a = np.reshape(a, -1)
# w = np.reshape( w, -1)
# print(f"{a}")
# print(f"{w}")

# # 과제 9번 
# # 중앙값 5.5 , 최빈값 7 , 
# print(("\n"))
# a = np.array([10,2,3,3,7,7,7,7,1,4])
# # print(a)
# # a.sort()
# # print(a)
# print(f"{np.median(a)}")
# # 짝수 

# if (a.size%2 == 0):
#     result = ((a.size/2) +((a.size/2)+1))/2
    
# elif (a.size%2==1):
#     result = (a.size+1)/2
    
# print(result)

# a = np.array([2,3,3,7,7,7,7,1,4])
# a.sort()

# print(f"{np.median(a)}")
# # 홀수

# if (a.size%2 == 0):
#     result = ((a.size/2) +((a.size/2)+1))/2
    
# elif (a.size%2==1):
#     result = (a.size+1)/2
      
# print(result)

a = np.array([10,2, 3, 3, 7, 7, 7, 7, 1, 4])
a_sort = np.sort(a)

# n = len(a_sort)
# print(n)
m = a_sort.size
# print(m)
if m % 2 != 0:  # 홀수일 떄
    curr = a_sort[m // 2]
else: # 짝수일 떄
    prev = a_sort[m // 2] # 4
    tail = a_sort[m // 2 - 1] # 3 
    curr = (prev+tail)/2


print("중앙값:", curr)


a = np.array([2, 3, 3, 7, 7, 7, 7, 1, 4])
a_sort = np.sort(a)

# m = len(a_sort)
# print(m)
m = a_sort.size
# print(m)
if m % 2 != 0:  # 홀수일 떄
    curr = a_sort[m // 2]
else: # 짝수일 떄
    prev = a_sort[m // 2] # 4
    tail = a_sort[m // 2 - 1] # 3 
    curr = (prev+tail)/2


print("중앙값:", curr)










