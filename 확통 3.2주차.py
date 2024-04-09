import numpy as np
import pandas as pd 
import scipy.stats as ss

a = np.array([2,3,3,4,4,4,4,5,5,6])
b = (a-a.mean()) / a.std()   # 표준화 , 얘 숫자아니고 배열임 

z = ss.zscore(a) # 싸이파이는 표준화 자동으로 구해줌 , 얘도 배열 

print(f"표준화 후 배열 : {b}" )
print(f"표준화 후 평균 : {b.mean()}" ) # 반올림 하고싶으면 np.round(b.mean(),7)
print(f"표준화 후 표준편차 : {b.std()}\n")

print(f"표준화 후 배열 : {z}" )
print(f"표준화 후 평균 : {z.mean()}" ) # 반올림 하고싶으면 np.round(b.mean(),7)
print(f"표준화 후 표준편차 : {z.std()}\n")
print(type(z), "\n")

h = np.loadtxt("C:/Users/kiiti/Downloads/중학생_남자_키.txt")

print(h.size) # 소괄호 하면 안 됨
print(h.mean())
print(h.std(), "\n") 

# 내가 평균에서 얼마나 멀리 있나  -> 편차
# 다른 애들은 평균에서 얼마나 멀리 있나 -> 표준편차
# z 스코어 : 표준화 ? -> (편차 / 표준편차)

a = (180-175)/5  # 표준화, 1 , 표준에서 1 + 된 느낌 
# 구글에서 그래프 표 보면 0.84134 나옴 즉 , 왼쪽 그래프는 84.134 % , 나는 상위 15.866 % # 표준 정규 분포포

a = (90-53.73) / 29.85
b = (90-59.53)/22.97

print(f" {a}, {b}") 
print(f"a는 상위 : 11.31% , b는 상위 : 9.34% ") 

dul = (90-85)/5
proro = (77-85)/5


print(h.size) # 소괄호 하면 안 됨
print(h.mean())
print(h.std(), "\n") 

ff = (168 - h.mean())/h.std()

print(f"표준화 : {ff}")
print(f"상위 : {100-83.646} %")






